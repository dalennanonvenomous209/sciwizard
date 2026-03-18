"""Apply the SciWizard dark theme to a QApplication."""

from __future__ import annotations

from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication

from sciwizard.config import DARK_PALETTE

_QSS = """
/* ================================================================
   SciWizard Dark Theme — Catppuccin-inspired
================================================================ */

QWidget {
    background-color: #1e1e2e;
    color: #cdd6f4;
    font-family: "Segoe UI", "Inter", "SF Pro Display", sans-serif;
    font-size: 13px;
}

QMainWindow {
    background-color: #1e1e2e;
}

/* Sidebar */
QFrame#sidebar {
    background-color: #181825;
    border-right: 1px solid #313244;
}

QPushButton#sidebar_btn {
    background-color: transparent;
    color: #a6adc8;
    border: none;
    padding: 10px 18px;
    text-align: left;
    border-radius: 6px;
    font-size: 13px;
}

QPushButton#sidebar_btn:hover {
    background-color: #313244;
    color: #cdd6f4;
}

QPushButton#sidebar_btn:checked {
    background-color: #7c6af7;
    color: #ffffff;
    font-weight: 600;
}

/* Generic buttons */
QPushButton {
    background-color: #313244;
    color: #cdd6f4;
    border: 1px solid #45475a;
    border-radius: 6px;
    padding: 6px 14px;
    font-size: 13px;
}

QPushButton:hover {
    background-color: #45475a;
    border-color: #7c6af7;
}

QPushButton:pressed {
    background-color: #7c6af7;
    color: #ffffff;
}

QPushButton:disabled {
    background-color: #27273a;
    color: #585b70;
    border-color: #313244;
}

QPushButton#primary_btn {
    background-color: #7c6af7;
    color: #ffffff;
    border: none;
    font-weight: 600;
}

QPushButton#primary_btn:hover {
    background-color: #9b8df8;
}

QPushButton#primary_btn:pressed {
    background-color: #6c5ce7;
}

/* Inputs */
QLineEdit, QSpinBox, QDoubleSpinBox, QComboBox {
    background-color: #27273a;
    color: #cdd6f4;
    border: 1px solid #45475a;
    border-radius: 5px;
    padding: 5px 8px;
}

QLineEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus, QComboBox:focus {
    border-color: #7c6af7;
}

QComboBox::drop-down {
    border: none;
    padding-right: 8px;
}

QComboBox QAbstractItemView {
    background-color: #27273a;
    border: 1px solid #45475a;
    selection-background-color: #7c6af7;
}

/* Tables */
QTableView {
    background-color: #1e1e2e;
    gridline-color: #313244;
    border: 1px solid #313244;
    border-radius: 6px;
}

QTableView::item {
    padding: 4px 8px;
}

QTableView::item:selected {
    background-color: #7c6af7;
    color: #ffffff;
}

QHeaderView::section {
    background-color: #27273a;
    color: #a6adc8;
    border: none;
    border-right: 1px solid #313244;
    border-bottom: 1px solid #313244;
    padding: 6px 10px;
    font-weight: 600;
    font-size: 12px;
}

/* Tabs */
QTabWidget::pane {
    border: 1px solid #313244;
    border-radius: 6px;
    background-color: #1e1e2e;
}

QTabBar::tab {
    background-color: #27273a;
    color: #a6adc8;
    padding: 8px 20px;
    border: 1px solid #313244;
    border-bottom: none;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
    margin-right: 2px;
}

QTabBar::tab:selected {
    background-color: #1e1e2e;
    color: #cdd6f4;
    border-bottom: 2px solid #7c6af7;
}

QTabBar::tab:hover:!selected {
    background-color: #313244;
}

/* Scrollbars */
QScrollBar:vertical {
    background-color: #1e1e2e;
    width: 10px;
    border-radius: 5px;
}

QScrollBar::handle:vertical {
    background-color: #45475a;
    border-radius: 5px;
    min-height: 20px;
}

QScrollBar::handle:vertical:hover {
    background-color: #7c6af7;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0;
}

QScrollBar:horizontal {
    background-color: #1e1e2e;
    height: 10px;
    border-radius: 5px;
}

QScrollBar::handle:horizontal {
    background-color: #45475a;
    border-radius: 5px;
}

/* Progress bar */
QProgressBar {
    background-color: #27273a;
    border-radius: 4px;
    border: none;
    text-align: center;
    color: #cdd6f4;
    height: 12px;
}

QProgressBar::chunk {
    background-color: #7c6af7;
    border-radius: 4px;
}

/* Splitters */
QSplitter::handle {
    background-color: #313244;
}

/* Labels */
QLabel#section_header {
    font-size: 15px;
    font-weight: 700;
    color: #cdd6f4;
    padding: 6px 0;
}

QLabel#muted {
    color: #6c7086;
    font-size: 12px;
}

/* Status bar */
QStatusBar {
    background-color: #181825;
    color: #a6adc8;
    border-top: 1px solid #313244;
    font-size: 12px;
}

/* Tooltips */
QToolTip {
    background-color: #313244;
    color: #cdd6f4;
    border: 1px solid #7c6af7;
    border-radius: 4px;
    padding: 5px 8px;
    font-size: 12px;
}

/* Group boxes */
QGroupBox {
    border: 1px solid #313244;
    border-radius: 6px;
    margin-top: 14px;
    padding-top: 10px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 0 6px;
    color: #7c6af7;
    font-weight: 600;
}

/* Checkboxes / radio buttons */
QCheckBox, QRadioButton {
    spacing: 6px;
}

QCheckBox::indicator {
    width: 16px;
    height: 16px;
    border-radius: 3px;
    border: 1px solid #45475a;
    background-color: #27273a;
}

QCheckBox::indicator:checked {
    background-color: #7c6af7;
    border-color: #7c6af7;
}

/* Sliders */
QSlider::groove:horizontal {
    background-color: #27273a;
    height: 6px;
    border-radius: 3px;
}

QSlider::handle:horizontal {
    background-color: #7c6af7;
    width: 16px;
    height: 16px;
    border-radius: 8px;
    margin: -5px 0;
}

QSlider::sub-page:horizontal {
    background-color: #7c6af7;
    border-radius: 3px;
}

/* Text edit */
QTextEdit, QPlainTextEdit {
    background-color: #181825;
    border: 1px solid #313244;
    border-radius: 6px;
    padding: 6px;
}
"""


def apply_dark_theme(app: QApplication) -> None:
    """Apply the SciWizard dark stylesheet to the application.

    Args:
        app: The running QApplication instance.
    """
    app.setStyle("Fusion")
    app.setStyleSheet(_QSS)

    palette = QPalette()
    bg = QColor(DARK_PALETTE["background"])
    text = QColor(DARK_PALETTE["text"])
    primary = QColor(DARK_PALETTE["primary"])

    palette.setColor(QPalette.ColorRole.Window, bg)
    palette.setColor(QPalette.ColorRole.WindowText, text)
    palette.setColor(QPalette.ColorRole.Base, QColor("#27273a"))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor("#313244"))
    palette.setColor(QPalette.ColorRole.ToolTipBase, QColor("#313244"))
    palette.setColor(QPalette.ColorRole.ToolTipText, text)
    palette.setColor(QPalette.ColorRole.Text, text)
    palette.setColor(QPalette.ColorRole.Button, QColor("#313244"))
    palette.setColor(QPalette.ColorRole.ButtonText, text)
    palette.setColor(QPalette.ColorRole.Highlight, primary)
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor("#ffffff"))
    palette.setColor(QPalette.ColorRole.Link, primary)

    app.setPalette(palette)
