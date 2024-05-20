from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit

class ChatView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Chat View"))
        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)
        layout.addWidget(self.chat_area)
        self.setLayout(layout)
