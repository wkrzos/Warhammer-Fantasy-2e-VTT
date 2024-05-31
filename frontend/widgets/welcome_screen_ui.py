# welcome_screen.py

from PySide6.QtCore import Qt, QTimer, QPropertyAnimation, QRect
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class SplashScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title = QLabel("BFVTT Application")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 36px; color: white;")

        version = QLabel("Version 1.0")
        version.setAlignment(Qt.AlignCenter)
        version.setStyleSheet("font-size: 18px; color: white;")

        authors = QLabel("By Author1 and Author2")
        authors.setAlignment(Qt.AlignCenter)
        authors.setStyleSheet("font-size: 18px; color: white;")

        layout.addWidget(title)
        layout.addWidget(version)
        layout.addWidget(authors)
        self.setLayout(layout)

    def fade_out(self):
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(1000)
        self.animation.setStartValue(self.geometry())
        self.animation.setEndValue(QRect(self.x(), self.y() - 100, self.width(), self.height()))
        self.animation.finished.connect(self.close)
        self.animation.start()
