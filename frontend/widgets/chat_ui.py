from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QLineEdit, QPushButton, QHBoxLayout
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

        self.nickname_layout = QHBoxLayout()
        self.nickname_input = QLineEdit()
        self.nickname_input.setFont(DEFAULT_FONT)
        self.nickname_input.setPlaceholderText("Enter your nickname")
        self.nickname_layout.addWidget(self.nickname_input)

        self.input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setFont(DEFAULT_FONT)
        self.input_layout.addWidget(self.input_field)

        self.send_button = QPushButton(self.tr("Send"))
        self.send_button.setFont(DEFAULT_FONT)
        self.input_layout.addWidget(self.send_button)

        layout.addLayout(self.nickname_layout)
        layout.addLayout(self.input_layout)

        self.setLayout(layout)

    def update_chat(self, messages):
        self.chat_area.clear()
        for message in messages:
            self.chat_area.append(message)
