# splash_screen.py

from PySide6.QtCore import Qt, QPropertyAnimation, QRect
from PySide6.QtGui import QPainter, QBrush, QColor, QLinearGradient, QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout

class SplashScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        
        # Horizontal layout for logo and text
        logo_and_text_layout = QHBoxLayout()
        
        # Logo
        logo = QLabel()
        logo_pixmap = QPixmap("frontend/resources/logo/bfvtt_icon_no_bg.png")  # Ensure the path is correct
        scaled_logo_pixmap = logo_pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)  # Scale logo
        logo.setPixmap(scaled_logo_pixmap)
        logo.setAlignment(Qt.AlignCenter)

        # Text layout
        text_layout = QVBoxLayout()

        title = QLabel("BFVTT Application")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 36px; color: white;")

        version = QLabel("Version 0.1")
        version.setAlignment(Qt.AlignCenter)
        version.setStyleSheet("font-size: 18px; color: white;")

        authors = QLabel("By Filip Puszko and Wojciech Krzos")
        authors.setAlignment(Qt.AlignCenter)
        authors.setStyleSheet("font-size: 18px; color: white;")

        text_layout.addWidget(title)
        text_layout.addWidget(version)
        text_layout.addWidget(authors)
        
        logo_and_text_layout.addWidget(logo)
        logo_and_text_layout.addLayout(text_layout)
        
        main_layout.addLayout(logo_and_text_layout)
        self.setLayout(main_layout)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rect = self.rect()

        # Create gradient for feathered edges
        gradient = QLinearGradient(rect.topLeft(), rect.bottomRight())
        gradient.setColorAt(0, QColor(0, 0, 0, 250))  # 40% translucent black
        gradient.setColorAt(1, QColor(0, 0, 0, 100))  # Fully transparent

        painter.setBrush(QBrush(gradient))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(rect, 30, 30)  # Adjust corner radius as needed

    def fade_out(self):
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(1000)
        self.animation.setStartValue(self.geometry())
        self.animation.setEndValue(QRect(self.x(), self.y() - 100, self.width(), self.height()))
        self.animation.finished.connect(self.close)
        self.animation.start()
