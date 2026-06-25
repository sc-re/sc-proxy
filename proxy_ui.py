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
import scmd_decoders
import session_loader


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


_BIT_RANGE_ROLE = QtCore.Qt.UserRole + 1


def _error_color() -> QtGui.QColor:
    """Red for unparsed / error rows, picked for the active theme.

    The original muted red (#cc4040) is too dark to read against a dark
    background, so brighten it when the palette is dark and use a deeper
    red on light themes where a pale red would wash out.
    """
    pal = QtWidgets.QApplication.palette()
    dark = pal.color(QtGui.QPalette.Base).lightnessF() < 0.5
    return QtGui.QColor("#ff6b6b") if dark else QtGui.QColor("#c0211b")


def _mono_font() -> QtGui.QFont:
    """A readable, anti-aliased monospace font.

    The platform 'fixed' font on Windows is often Courier New, which
    renders poorly at UI sizes; prefer a modern programming monospace when
    one is installed. PreferAntialias forces smoothing on regardless of
    the font's default style strategy.
    """
    families = set(QtGui.QFontDatabase.families())
    for name in ("Cascadia Mono", "Cascadia Code", "Consolas",
                 "JetBrains Mono", "DejaVu Sans Mono"):
        if name in families:
            font = QtGui.QFont(name)
            break
    else:
        font = QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont)
    font.setPointSize(10)
    font.setStyleStrategy(
        QtGui.QFont.PreferAntialias | QtGui.QFont.PreferQuality)
    return font


def _node_to_item(node: scmd_decoders.DecodeNode) -> QtWidgets.QTreeWidgetItem:
    """Convert a DecodeNode subtree into a QTreeWidgetItem subtree.

    Stashes node.bit_range on the item via _BIT_RANGE_ROLE so the row's
    bytes can be highlighted in the hex pane on selection.
    """
    item = QtWidgets.QTreeWidgetItem([node.name, node.value, node.wire_type])
    if node.bit_range is not None:
        item.setData(0, _BIT_RANGE_ROLE, node.bit_range)
    if node.wire_type == "error":
        for col in range(3):
            item.setForeground(col, _error_color())
    for child in node.children:
        item.addChild(_node_to_item(child))
    return item


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
        # When live, incoming bus records are appended; when showing a
        # loaded session, live records are buffered (still captured by the
        # proxy threads) but not shown until the user switches back.
        self._live = True
        self.new_record.connect(self._on_record, QtCore.Qt.QueuedConnection)
        packet_bus.subscribe(lambda r: self.new_record.emit(r))
        for r in packet_bus.history():
            self._append(r)

    # ---- internal -------------------------------------------------------

    def _on_record(self, r: packet_bus.PacketRecord) -> None:
        if self._live:
            self._append(r)

    # ---- session switching ---------------------------------------------

    def show_live(self) -> None:
        """Switch back to the live view, backfilling from bus history."""
        self.beginResetModel()
        self._records = list(packet_bus.history())
        self._live = True
        self.endResetModel()

    def show_session(self,
                     records: list[packet_bus.PacketRecord]) -> None:
        """Replace the table contents with a loaded session's records and
        stop appending live traffic until show_live() is called."""
        self.beginResetModel()
        self._live = False
        self._records = list(records)
        self.endResetModel()

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
            return _error_color()
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

        # Session selector — "Live" plus every on-disk capture session.
        # Picking an older session loads it into the table; picking Live
        # resumes showing freshly captured traffic.
        self.session_combo = QtWidgets.QComboBox()
        self.session_combo.setMinimumWidth(260)
        self.session_combo.setToolTip("Load an older capture session")
        self.reload_btn = QtWidgets.QToolButton()
        self.reload_btn.setText("⟳")
        self.reload_btn.setToolTip("Rescan capture directories")
        self.reload_btn.clicked.connect(self._refresh_sessions)
        self._refresh_sessions()
        self.session_combo.currentIndexChanged.connect(self._on_session_pick)

        bar = QtWidgets.QHBoxLayout()
        bar.addWidget(QtWidgets.QLabel("Filter:"))
        bar.addWidget(self.filter_edit, 1)
        bar.addWidget(self.dir_sc)
        bar.addWidget(self.dir_cs)
        bar.addWidget(self.follow_box)
        bar.addWidget(QtWidgets.QLabel("Session:"))
        bar.addWidget(self.session_combo)
        bar.addWidget(self.reload_btn)

        # Table
        self.table = QtWidgets.QTableView()
        self.table.setModel(self.proxy)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)
        mono = _mono_font()
        self.table.setFont(mono)
        for c, w in enumerate([60, 80, 110, 312, 448, 100, 70]):
            self.table.setColumnWidth(c, w)
        self.table.selectionModel().currentRowChanged.connect(self._on_row)

        # Detail panes — Wireshark-style: a collapsible decode tree and the
        # raw hex dump, side by side. The TGP header is folded into the tree
        # as its own top-level branch.
        self.tree = QtWidgets.QTreeWidget()
        self.tree.setHeaderLabels(["Field", "Value", "Type"])
        self.tree.setFont(mono)
        self.tree.setColumnWidth(0, 340)
        self.tree.setColumnWidth(1, 380)
        self.tree.setAlternatingRowColors(True)

        self.hex_text = QtWidgets.QPlainTextEdit(readOnly=True)
        self.hex_text.setFont(mono)
        self.hex_text.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)

        # Wireshark-style: select a tree node → highlight the matching
        # bytes (and ASCII glyphs) in the hex pane.
        self.tree.currentItemChanged.connect(self._on_tree_node)

        # Right-click menus — copy field values / packet bytes to clipboard.
        self.table.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self._on_table_menu)
        self.tree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self._on_tree_menu)

        # Stash the current packet's body / record so the tree-menu's
        # "Copy bytes" can slice it without going back to the packet model.
        self._current_body: bytes = b""
        self._current_record: packet_bus.PacketRecord | None = None

        detail = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        detail.addWidget(self.tree)
        detail.addWidget(self.hex_text)
        detail.setStretchFactor(0, 3)
        detail.setStretchFactor(1, 2)

        # Splitter — packet table above, detail panes below.
        splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        splitter.addWidget(self.table)
        splitter.addWidget(detail)
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
        scope = "live" if self.model._live else "session"
        self._status.showMessage(
            f"{self.proxy.rowCount()} shown / {self.model.rowCount()} "
            f"{scope}"
        )

    # ---- session loading ------------------------------------------------

    def _refresh_sessions(self) -> None:
        """(Re)populate the session combo from disk. Index 0 is always the
        live view; the rest are on-disk sessions newest-first. Each item's
        userData is the session path (None for Live)."""
        keep_path = self.session_combo.currentData()
        self.session_combo.blockSignals(True)
        self.session_combo.clear()
        self.session_combo.addItem("● Live", None)
        for s in session_loader.list_sessions():
            self.session_combo.addItem(s.label, s.path)
        # Restore the previously-selected session if it still exists.
        if keep_path is not None:
            i = self.session_combo.findData(keep_path)
            if i >= 0:
                self.session_combo.setCurrentIndex(i)
        self.session_combo.blockSignals(False)

    def _on_session_pick(self, _index: int) -> None:
        path = self.session_combo.currentData()
        if path is None:
            self.model.show_live()
            self.follow_box.setEnabled(True)
            self._update_status()
            return
        # Loading reads + decodes every body; show a wait cursor since a
        # large session can take a moment.
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        try:
            records = session_loader.load_session(path)
        finally:
            QtWidgets.QApplication.restoreOverrideCursor()
        self.model.show_session(records)
        # A loaded session is static — tail-following is meaningless, so
        # disable it and jump to the top.
        self.follow_box.setEnabled(False)
        self.table.scrollToTop()
        self._update_status()

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
        self.hex_text.setPlainText(_hexdump(r.body))
        # Drop any prior highlight — its cursors point at the previous
        # document which setPlainText() just replaced.
        self.hex_text.setExtraSelections([])
        self.tree.clear()
        self._current_body = r.body
        self._current_record = r

        # TGP header branch — always present.
        hdr_fields = [
            ("send_counter", f"0x{r.send_counter:04x}"),
            ("echo_send_counter", f"0x{r.echo_send_counter:04x}"),
            ("scmd_pkt_type", f"0x{r.pkt_type:04x} ({r.pkt_name})"),
            ("checksum", f"0x{r.checksum:04x}"),
            ("body_len", str(r.body_len)),
        ]
        if r.sub_id is not None:
            hdr_fields.append(("sub", f"0x{r.sub_id:02x} ({r.sub_name or ''})"))
        if r.uid is not None:
            hdr_fields.append(("uid", str(r.uid)))
        hdr_fields += [
            ("tag", r.tag),
            ("direction", r.direction),
            ("timestamp",
             time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(r.ts))),
        ]
        hdr_item = QtWidgets.QTreeWidgetItem(["TGP header", "", ""])
        for k, v in hdr_fields:
            hdr_item.addChild(QtWidgets.QTreeWidgetItem([k, v, ""]))
        self.tree.addTopLevelItem(hdr_item)

        # Decoded payload branch — structured tree when a decoder exists,
        # else the flat log line as a single leaf.
        node = scmd_decoders.decode_structured(r.pkt_type, r.body, r.direction)
        if node is not None:
            self.tree.addTopLevelItem(_node_to_item(node))
        elif r.body:
            self.tree.addTopLevelItem(QtWidgets.QTreeWidgetItem(
                ["payload", _strip_ansi(r.decoded_line), ""]))

        self.tree.expandToDepth(1)

    def _on_tree_node(self,
                      current: QtWidgets.QTreeWidgetItem | None,
                      _previous: QtWidgets.QTreeWidgetItem | None) -> None:
        """Highlight the wire bytes the selected tree node was decoded
        from, in both the hex column and the ASCII glyph column."""
        if current is None:
            self.hex_text.setExtraSelections([])
            return
        bit_range = current.data(0, _BIT_RANGE_ROLE)
        if not bit_range:
            self.hex_text.setExtraSelections([])
            return
        bit_start, bit_end = bit_range
        byte_start = bit_start // 8
        byte_end = (bit_end + 7) // 8     # round up — sub-byte fields highlight their byte
        self._highlight_hex_bytes(byte_start, byte_end)

    def _highlight_hex_bytes(self, byte_start: int, byte_end: int) -> None:
        """Apply ExtraSelections to the hex pane covering bytes
        [byte_start, byte_end). The hex pane format (see _hexdump) is
        16 bytes per line:

            OFFSET  HH HH HH ... HH    ASCII   ← cols 0..6  8..56  58..74

        so we can compute the cursor positions per intersecting line.
        Scrolls the pane so the first highlighted byte is in view.
        """
        sels: list[QtWidgets.QTextEdit.ExtraSelection] = []
        width = 16
        # ASCII column = 6-char offset + "  " + 16×3=48-char hex chunk + "  ".
        ascii_col = 8 + width * 3 + 2
        doc = self.hex_text.document()
        block = doc.firstBlock()
        first_cursor: QtGui.QTextCursor | None = None
        while block.isValid():
            text = block.text()
            if len(text) >= 6:
                try:
                    line_off = int(text[:6], 16)
                except ValueError:
                    block = block.next()
                    continue
                line_end = line_off + width
                if byte_start < line_end and line_off < byte_end:
                    a = max(line_off, byte_start) - line_off
                    b = min(line_end, byte_end) - line_off
                    # Hex chunk: byte i occupies cols [8+i*3, 8+i*3+2).
                    hex_sel = _make_selection(block, 8 + a * 3, 8 + b * 3 - 1)
                    # ASCII column: byte i = col ascii_col+i.
                    asc_sel = _make_selection(block, ascii_col + a,
                                              ascii_col + b)
                    sels.append(hex_sel)
                    sels.append(asc_sel)
                    if first_cursor is None:
                        first_cursor = hex_sel.cursor
            block = block.next()
        # Scroll so the first highlight is visible — otherwise a deep
        # field in a 240 kB body looks like "no highlight" to the user.
        if first_cursor is not None:
            scroll_cursor = QtGui.QTextCursor(first_cursor)
            scroll_cursor.clearSelection()
            self.hex_text.setTextCursor(scroll_cursor)
            self.hex_text.ensureCursorVisible()
        self.hex_text.setExtraSelections(sels)

    # ---- context menus ------------------------------------------------

    def _on_tree_menu(self, pos: QtCore.QPoint) -> None:
        """Right-click on a decode-tree row → copy field name / value /
        bytes to the clipboard."""
        item = self.tree.itemAt(pos)
        if item is None:
            return
        name, value, type_ = item.text(0), item.text(1), item.text(2)
        clip = QtWidgets.QApplication.clipboard()
        menu = QtWidgets.QMenu(self.tree)

        if value:
            menu.addAction(f"Copy value  ({_elide(value)})",
                           lambda v=value: clip.setText(v))
        menu.addAction(f"Copy field name  ({_elide(name)})",
                       lambda n=name: clip.setText(n))
        if value:
            menu.addAction("Copy 'name = value'",
                           lambda: clip.setText(f"{name} = {value}"))
        menu.addAction("Copy field path",
                       lambda it=item: clip.setText(_tree_path(it)))
        if type_:
            menu.addAction(f"Copy wire type  ({type_})",
                           lambda t=type_: clip.setText(t))

        bit_range = item.data(0, _BIT_RANGE_ROLE)
        if bit_range and self._current_body:
            bs = bit_range[0] // 8
            be = (bit_range[1] + 7) // 8
            chunk = self._current_body[bs:be]
            menu.addSeparator()
            menu.addAction(
                f"Copy bytes  ({len(chunk)} B, {bit_range[1] - bit_range[0]} bits)",
                lambda c=chunk: clip.setText(c.hex()))

        menu.exec(self.tree.viewport().mapToGlobal(pos))

    def _on_table_menu(self, pos: QtCore.QPoint) -> None:
        """Right-click on a packet row → copy the decoded line / hex body."""
        idx = self.table.indexAt(pos)
        if not idx.isValid():
            return
        r: packet_bus.PacketRecord | None = self.proxy.data(
            idx, QtCore.Qt.UserRole)
        if r is None:
            return
        clip = QtWidgets.QApplication.clipboard()
        menu = QtWidgets.QMenu(self.table)
        menu.addAction("Copy decoded line",
                       lambda: clip.setText(_strip_ansi(r.decoded_line)))
        menu.addAction(f"Copy body as hex  ({len(r.body)} B)",
                       lambda: clip.setText(r.body.hex()))
        menu.addAction("Copy hex dump",
                       lambda: clip.setText(_hexdump(r.body)))
        menu.addAction(f"Copy packet name  ({r.pkt_name})",
                       lambda: clip.setText(r.pkt_name))
        if r.sub_name:
            menu.addAction(f"Copy sub name  ({r.sub_name})",
                           lambda: clip.setText(r.sub_name))
        if r.uid is not None:
            menu.addAction(f"Copy uid  ({r.uid})",
                           lambda: clip.setText(str(r.uid)))
        menu.exec(self.table.viewport().mapToGlobal(pos))


# Highlight colour used for hex-pane byte selections. Bright enough to be
# visible against both light and dark hex-pane backgrounds.
_HIGHLIGHT_BG = QtGui.QColor(255, 220, 80)
_HIGHLIGHT_FG = QtGui.QColor(0, 0, 0)


# ── module-level helpers (free functions for the context menus) ────────────

def _elide(s: str, max_len: int = 30) -> str:
    """Trim a long string for menu-item labels."""
    return s if len(s) <= max_len else s[:max_len - 1] + "…"


def _tree_path(item: QtWidgets.QTreeWidgetItem) -> str:
    """Build a slash-separated path from the tree root to `item`."""
    parts: list[str] = []
    cur = item
    while cur is not None:
        parts.append(cur.text(0))
        cur = cur.parent()
    return "/".join(reversed(parts))


def _make_selection(block: QtGui.QTextBlock, col_start: int,
                    col_end: int) -> "QtWidgets.QTextEdit.ExtraSelection":
    """Build one QTextEdit.ExtraSelection spanning [col_start, col_end) of `block`.

    Mutates the selection's existing `.format` instead of replacing it
    — some PySide6 builds drop a freshly assigned `sel.format = fmt`
    object after the slot returns, leaving the selection invisible.
    """
    cur = QtGui.QTextCursor(block)
    cur.setPosition(block.position() + col_start)
    cur.setPosition(block.position() + col_end, QtGui.QTextCursor.KeepAnchor)
    sel = QtWidgets.QTextEdit.ExtraSelection()
    sel.cursor = cur
    sel.format.setBackground(_HIGHLIGHT_BG)
    sel.format.setForeground(_HIGHLIGHT_FG)
    return sel


# ── entry point ─────────────────────────────────────────────────────────────

def run() -> int:
    # High-DPI: with the default (rounded) policy Qt snaps fractional
    # Windows display scales (e.g. 125%/150%) to an integer factor, which
    # leaves text blurry / poorly anti-aliased. PassThrough keeps the real
    # fractional factor so glyphs stay sharp. Must be set before the
    # QApplication is constructed.
    if QtWidgets.QApplication.instance() is None:
        QtWidgets.QApplication.setHighDpiScaleFactorRoundingPolicy(
            QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QtWidgets.QApplication.instance() or QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(run())
