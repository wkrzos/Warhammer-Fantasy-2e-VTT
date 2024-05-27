from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QHBoxLayout, QPushButton, QAbstractItemView
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
import os

class MusicPlayerViewUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel(self.tr("Music Player")))

        self.playlist = QListWidget()
        self.playlist.setCurrentRow(0)
        self.playlist.setSelectionMode(QAbstractItemView.SingleSelection)
        layout.addWidget(self.playlist)

        controls_layout = QHBoxLayout()

        icon_path = os.path.join(os.path.dirname(__file__), '../../frontend/resources/icons')
        self.play_button = QPushButton()
        self.play_button.setIcon(QIcon(os.path.join(icon_path, 'play.png')))
        self.play_button.setIconSize(QSize(32, 32))

        self.stop_button = QPushButton()
        self.stop_button.setIcon(QIcon(os.path.join(icon_path, 'stop.png')))
        self.stop_button.setIconSize(QSize(32, 32))

        self.pause_button = QPushButton()
        self.pause_button.setIcon(QIcon(os.path.join(icon_path, 'pause.png')))
        self.pause_button.setIconSize(QSize(32, 32))

        self.next_button = QPushButton()
        self.next_button.setIcon(QIcon(os.path.join(icon_path, 'next.png')))
        self.next_button.setIconSize(QSize(32, 32))

        self.prev_button = QPushButton()
        self.prev_button.setIcon(QIcon(os.path.join(icon_path, 'prev.png')))
        self.prev_button.setIconSize(QSize(32, 32))

        controls_layout.addWidget(self.prev_button)
        controls_layout.addWidget(self.play_button)
        controls_layout.addWidget(self.pause_button)
        controls_layout.addWidget(self.stop_button)
        controls_layout.addWidget(self.next_button)

        layout.addLayout(controls_layout)
        self.setLayout(layout)

    def update_playlist(self, songs):
        self.playlist.clear()
        for song in songs:
            self.playlist.addItem(self.tr(song))
