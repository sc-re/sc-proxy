"""PySide6 Wireshark-style packet inspector for the StarConflict proxy.

Subscribes to packet_bus and renders captured packets in a live table.
Click a row to view its decoded line, hex dump, and TGP header. The
existing console logger keeps running in parallel — this UI is an
additional sink, not a replacement.

Threading: the three sub-proxies live on background daemon threads;
publish() is invoked from those threads. We cross over to the GUI
thread via a queued Qt signal so the model is only mutated where Qt
expects it.
"""
from __future__ import annotations
import re
import sys
import time

from PySide6 import QtCore, QtGui, QtWidgets

import packet_bus


# ── helpers ─────────────────────────────────────────────────────────────────

_ANSI = re.compile(r"\x1b\[[0-9;]*m")


def _strip_ansi(s: str) -> str:
    return _ANSI.sub("", s or "")


def _hexdump(data: bytes, width: int = 16) -> str:
    lines = []
    for i in range(0, len(data), width):
        chunk = data[i:i + width]
        hx = " ".join(f"{b:02x}" for b in chunk)
        asc = "".join(chr(b) if 32 <= b < 127 else "." for b in chunk)
        lines.append(f"{i:06x}  {hx:<{width*3}}  {asc}")
    return "\n".join(lines)


# ── model ───────────────────────────────────────────────────────────────────

class PacketModel(QtCore.QAbstractTableModel):
    """Owns the list of PacketRecords backing the table.

    publish() runs on a proxy worker thread; new_record is emitted from
    that thread but connected to _on_record with Qt.QueuedConnection so
    the actual append + signal happens on the GUI thread.
    """

    COLUMNS = ("#", "time", "tag", "pkt", "sub", "uid", "len")

    new_record = QtCore.Signal(object)  # PacketRecord

    def __init__(self, parent: QtCore.QObject | None = None):
        super().__init__(parent)
        self._records: list[packet_bus.PacketRecord] = []
        self.new_record.connect(self._on_record, QtCore.Qt.QueuedConnection)
        packet_bus.subscribe(lambda r: self.new_record.emit(r))
        for r in packet_bus.history():
            self._append(r)

    # ---- internal -------------------------------------------------------

    def _on_record(self, r: packet_bus.PacketRecord) -> None:
        self._append(r)

    def _append(self, r: packet_bus.PacketRecord) -> None:
        row = len(self._records)
        self.beginInsertRows(QtCore.QModelIndex(), row, row)
        self._records.append(r)
        self.endInsertRows()

    # ---- QAbstractTableModel API ---------------------------------------

    def rowCount(self, parent=QtCore.QModelIndex()) -> int:
        return 0 if parent.isValid() else len(self._records)

    def columnCount(self, parent=QtCore.QModelIndex()) -> int:
        return 0 if parent.isValid() else len(self.COLUMNS)

    def data(self, index: QtCore.QModelIndex, role=QtCore.Qt.DisplayRole):
        if not index.isValid():
            return None
        r = self._records[index.row()]
        col = index.column()
        if role == QtCore.Qt.DisplayRole:
            if col == 0: return r.idx
            if col == 1: return time.strftime("%H:%M:%S", time.localtime(r.ts))
            if col == 2: return r.tag
            if col == 3: return f"0x{r.pkt_type:02x} {r.pkt_name}"
            if col == 4:
                if r.sub_id is not None:
                    return f"0x{r.sub_id:02x} {r.sub_name or ''}".rstrip()
                return ""
            if col == 5: return "" if r.uid is None else str(r.uid)
            if col == 6: return r.body_len
        elif role == QtCore.Qt.ForegroundRole and not r.ok:
            return QtGui.QColor("#cc4040")
        elif role == QtCore.Qt.UserRole:
            return r
        return None

    def headerData(self, section, orient, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return None
        if orient == QtCore.Qt.Horizontal:
            return self.COLUMNS[section]
        return None


# ── filter ──────────────────────────────────────────────────────────────────

class FilterProxy(QtCore.QSortFilterProxyModel):
    """Applies text + direction filters."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._text = ""
        self._dirs = {"S→C": True, "C→S": True}

    def set_text_filter(self, text: str) -> None:
        self._text = (text or "").lower()
        self.invalidateFilter()

    def set_direction(self, direction: str, enabled: bool) -> None:
        self._dirs[direction] = enabled
        self.invalidateFilter()

    def filterAcceptsRow(self, src_row, src_parent) -> bool:
        m = self.sourceModel()
        idx = m.index(src_row, 0, src_parent)
        r: packet_bus.PacketRecord | None = m.data(idx, QtCore.Qt.UserRole)
        if r is None:
            return True
        if not self._dirs.get(r.direction, True):
            return False
        if self._text:
            haystack = " ".join(filter(None, [
                r.tag, r.pkt_name, r.sub_name or "",
                str(r.uid) if r.uid is not None else "",
                _strip_ansi(r.decoded_line),
            ])).lower()
            if self._text not in haystack:
                return False
        return True


# ── main window ─────────────────────────────────────────────────────────────

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StarConflict proxy — packet inspector")
        self.resize(1280, 800)

        # Model + proxy
        self.model = PacketModel(self)
        self.proxy = FilterProxy(self)
        self.proxy.setSourceModel(self.model)

        # Filter bar
        self.filter_edit = QtWidgets.QLineEdit(placeholderText="filter…")
        self.filter_edit.setClearButtonEnabled(True)
        self.filter_edit.textChanged.connect(self.proxy.set_text_filter)
        self.dir_sc = QtWidgets.QCheckBox("S→C"); self.dir_sc.setChecked(True)
        self.dir_cs = QtWidgets.QCheckBox("C→S"); self.dir_cs.setChecked(True)
        self.dir_sc.toggled.connect(lambda v: self.proxy.set_direction("S→C", v))
        self.dir_cs.toggled.connect(lambda v: self.proxy.set_direction("C→S", v))
        self.follow_box = QtWidgets.QCheckBox("Follow tail")
        self.follow_box.setChecked(True)
        bar = QtWidgets.QHBoxLayout()
        bar.addWidget(QtWidgets.QLabel("Filter:"))
        bar.addWidget(self.filter_edit, 1)
        bar.addWidget(self.dir_sc)
        bar.addWidget(self.dir_cs)
        bar.addWidget(self.follow_box)

        # Table
        self.table = QtWidgets.QTableView()
        self.table.setModel(self.proxy)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)
        mono = QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont)
        self.table.setFont(mono)
        for c, w in enumerate([60, 80, 110, 220, 240, 100, 70]):
            self.table.setColumnWidth(c, w)
        self.table.selectionModel().currentRowChanged.connect(self._on_row)

        # Detail tabs
        self.decoded_text = QtWidgets.QPlainTextEdit(readOnly=True)
        self.decoded_text.setFont(mono)
        self.decoded_text.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.hex_text = QtWidgets.QPlainTextEdit(readOnly=True)
        self.hex_text.setFont(mono)
        self.hex_text.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.header_text = QtWidgets.QPlainTextEdit(readOnly=True)
        self.header_text.setFont(mono)
        self.header_text.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.tabs = QtWidgets.QTabWidget()
        self.tabs.addTab(self.decoded_text, "Decoded")
        self.tabs.addTab(self.hex_text, "Hex")
        self.tabs.addTab(self.header_text, "Header")

        # Splitter
        splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        splitter.addWidget(self.table)
        splitter.addWidget(self.tabs)
        splitter.setStretchFactor(0, 3)
        splitter.setStretchFactor(1, 2)

        central = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(central)
        layout.setContentsMargins(6, 6, 6, 6)
        layout.addLayout(bar)
        layout.addWidget(splitter, 1)
        self.setCentralWidget(central)

        # Status bar shows shown/total
        self._status = self.statusBar()
        self.model.rowsInserted.connect(self._update_status)
        self.proxy.rowsInserted.connect(self._update_status)
        self.proxy.rowsRemoved.connect(self._update_status)
        self.proxy.modelReset.connect(self._update_status)
        self.model.rowsInserted.connect(self._maybe_scroll)
        self._update_status()

    # ---- slots ----------------------------------------------------------

    def _update_status(self, *_):
        self._status.showMessage(
            f"{self.proxy.rowCount()} shown / {self.model.rowCount()} captured"
        )

    def _maybe_scroll(self, *_):
        if self.follow_box.isChecked():
            self.table.scrollToBottom()

    def _on_row(self, current: QtCore.QModelIndex, _previous):
        if not current.isValid():
            return
        r: packet_bus.PacketRecord | None = self.proxy.data(
            current, QtCore.Qt.UserRole)
        if r is None:
            return
        self.decoded_text.setPlainText(_strip_ansi(r.decoded_line))
        self.hex_text.setPlainText(_hexdump(r.body))
        hdr_lines = [
            f"send_counter      = 0x{r.send_counter:04x}",
            f"echo_send_counter = 0x{r.echo_send_counter:04x}",
            f"scmd_pkt_type     = 0x{r.pkt_type:04x} ({r.pkt_name})",
            f"checksum          = 0x{r.checksum:04x}",
            f"body_len          = {r.body_len}",
        ]
        if r.sub_id is not None:
            hdr_lines.append(
                f"sub_id            = 0x{r.sub_id:02x} ({r.sub_name or ''})")
        if r.uid is not None:
            hdr_lines.append(f"uid               = {r.uid}")
        hdr_lines += [
            f"tag               = {r.tag}",
            f"direction         = {r.direction}",
            f"timestamp         = "
            f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(r.ts))}",
        ]
        self.header_text.setPlainText("\n".join(hdr_lines))


# ── entry point ─────────────────────────────────────────────────────────────

def run() -> int:
    app = QtWidgets.QApplication.instance() or QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(run())
