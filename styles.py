# Stylesheet moderno para a aplicação
# Dark Theme com cores azuis/roxas (2024/2025 design trends)

DARK_STYLESHEET = """
QMainWindow {
    background-color: #0f172a;
    color: #e2e8f0;
}

QWidget {
    background-color: #0f172a;
    color: #e2e8f0;
}

QLineEdit {
    background-color: #1e293b;
    border: 2px solid #334155;
    border-radius: 8px;
    padding: 10px;
    color: #e2e8f0;
    font-size: 13px;
    font-family: 'Segoe UI', Arial;
    selection-background-color: #3b82f6;
}

QLineEdit:focus {
    border: 2px solid #3b82f6;
    background-color: #1e293b;
}

QLineEdit::placeholder {
    color: #64748b;
}

QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #3b82f6, stop:1 #1e40af);
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 600;
    font-family: 'Segoe UI', Arial;
    box-shadow: 0px 4px 15px rgba(59, 130, 246, 0.4);
}

QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #60a5fa, stop:1 #3b82f6);
    box-shadow: 0px 6px 20px rgba(59, 130, 246, 0.6);
}

QPushButton:pressed {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #1e40af, stop:1 #1e3a8a);
    padding: 14px 24px 10px 24px;
    box-shadow: 0px 2px 8px rgba(59, 130, 246, 0.3);
}

QPushButton:flat {
    background-color: transparent;
    box-shadow: none;
}

QLabel {
    color: #e2e8f0;
    font-family: 'Segoe UI', Arial;
}

QLabel#title {
    font-size: 28px;
    font-weight: 700;
    color: #f1f5f9;
}

QLabel#subtitle {
    font-size: 14px;
    color: #94a3b8;
}

QGroupBox {
    border: 2px solid #334155;
    border-radius: 10px;
    margin-top: 10px;
    padding-top: 10px;
    color: #e2e8f0;
    font-weight: 600;
    font-family: 'Segoe UI', Arial;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 15px;
    padding: 0 5px 0 5px;
}

QTextEdit {
    background-color: #1e293b;
    border: 2px solid #334155;
    border-radius: 8px;
    padding: 10px;
    color: #e2e8f0;
    font-size: 13px;
    font-family: 'Consolas', 'Monaco', monospace;
    selection-background-color: #3b82f6;
}

QTextEdit:focus {
    border: 2px solid #3b82f6;
}

QTableWidget {
    background-color: #1e293b;
    gridline-color: #334155;
    border: 1px solid #334155;
    border-radius: 8px;
}

QTableWidget::item {
    padding: 8px;
    color: #e2e8f0;
}

QTableWidget::item:selected {
    background-color: #3b82f6;
    color: white;
}

QHeaderView::section {
    background-color: #0f172a;
    color: #e2e8f0;
    padding: 8px;
    border: none;
    border-bottom: 2px solid #334155;
    font-weight: 600;
    font-family: 'Segoe UI', Arial;
}

QMenuBar {
    background-color: #0f172a;
    color: #e2e8f0;
    border-bottom: 1px solid #334155;
}

QMenuBar::item:selected {
    background-color: #1e293b;
}

QMenu {
    background-color: #1e293b;
    color: #e2e8f0;
    border: 1px solid #334155;
}

QMenu::item:selected {
    background-color: #3b82f6;
}

QStatusBar {
    background-color: #0f172a;
    color: #94a3b8;
    border-top: 1px solid #334155;
}

QMessageBox {
    background-color: #0f172a;
}

QMessageBox QLabel {
    color: #e2e8f0;
}

QMessageBox QPushButton {
    min-width: 60px;
    min-height: 30px;
}

/* Scrollbars */
QScrollBar:vertical {
    background-color: #0f172a;
    width: 12px;
    border: none;
}

QScrollBar::handle:vertical {
    background-color: #334155;
    border-radius: 6px;
    min-height: 20px;
}

QScrollBar::handle:vertical:hover {
    background-color: #475569;
}

QScrollBar:horizontal {
    background-color: #0f172a;
    height: 12px;
    border: none;
}

QScrollBar::handle:horizontal {
    background-color: #334155;
    border-radius: 6px;
    min-width: 20px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #475569;
}

QScrollBar::up-arrow, QScrollBar::down-arrow, 
QScrollBar::left-arrow, QScrollBar::right-arrow {
    background: none;
}

QScrollBar::add-page, QScrollBar::sub-page {
    background: none;
}
"""
