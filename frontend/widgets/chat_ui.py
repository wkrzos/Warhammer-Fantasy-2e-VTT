from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit
from frontend.util.font import DEFAULT_FONT

class ChatViewUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        label = QLabel(self.tr("Chat View"))
        label.setFont(DEFAULT_FONT)
        layout.addWidget(label)

        self.chat_area = QTextEdit()
        self.chat_area.setFont(DEFAULT_FONT)
        self.chat_area.setReadOnly(True)
        layout.addWidget(self.chat_area)

        self.setLayout(layout)

    def update_chat(self, messages):
        self.chat_area.clear()
        for message in messages:
            self.chat_area.append(message)
