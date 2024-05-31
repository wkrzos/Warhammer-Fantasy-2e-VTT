from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt

class WelcomeScreen(QWidget):
    def __init__(self, main_window_callback):
        super().__init__()
        self.main_window_callback = main_window_callback
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title = QLabel("BFVTT Application")
        title.setAlignment(Qt.AlignCenter)
        version = QLabel("Version: 0.1")
        version.setAlignment(Qt.AlignCenter)
        authors = QLabel("Authors: Wojciech Krzos, Filip Puszko")
        authors.setAlignment(Qt.AlignCenter)

        start_button = QPushButton("Start")
        start_button.clicked.connect(self.start_main_window)

        layout.addWidget(title)
        layout.addWidget(version)
        layout.addWidget(authors)
        layout.addWidget(start_button)

        self.setFixedSize(300, 200)

        self.setLayout(layout)

    def start_main_window(self):
        self.main_window_callback()
        self.close()
