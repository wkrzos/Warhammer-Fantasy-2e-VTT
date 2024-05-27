import os

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QHBoxLayout, QFileDialog, \
    QTextEdit, QAbstractItemView
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon

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

class CharactersView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Characters"))
        self.character_list = QListWidget()
        layout.addWidget(self.character_list)
        add_button = QPushButton("Add Character")
        layout.addWidget(add_button)
        self.setLayout(layout)
        
class CreaturesView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Creatures"))
        self.character_list = QListWidget()
        layout.addWidget(self.character_list)
        add_button = QPushButton("Add Creature")
        layout.addWidget(add_button)
        self.setLayout(layout)
        
class ItemsView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Items"))
        self.character_list = QListWidget()
        layout.addWidget(self.character_list)
        add_button = QPushButton("Add Item")
        layout.addWidget(add_button)
        self.setLayout(layout)

class MusicPlayerView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        
        # Correct path to the music folder


    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Music Player"))
        self.playlist = QListWidget()


        layout.addWidget(self.playlist)
        
        controls_layout = QHBoxLayout()

        # Load icons from the resources directory
        icon_path = os.path.join(os.path.dirname(__file__), '../../frontend/resources/icons')
        play_icon = QIcon(os.path.join(icon_path, 'play.png'))
        stop_icon = QIcon(os.path.join(icon_path, 'stop.png'))
        pause_icon = QIcon(os.path.join(icon_path, 'pause.png'))
        next_icon = QIcon(os.path.join(icon_path, 'next.png'))
        prev_icon = QIcon(os.path.join(icon_path, 'prev.png'))

        # Create a toggle button for play/stop
        self.toggle_button = QPushButton()
        self.toggle_button.setIcon(pause_icon)
        self.toggle_button.setIconSize(QSize(32, 32))
        self.is_playing = True
        self.play_icon = play_icon
        self.stop_icon = pause_icon

        self.pause_button = QPushButton()
        self.pause_button.setIcon(stop_icon)
        self.pause_button.setIconSize(QSize(32, 32))

        self.next_button = QPushButton()
        self.next_button.setIcon(next_icon)
        self.next_button.setIconSize(QSize(32, 32))

        self.prev_button = QPushButton()
        self.prev_button.setIcon(prev_icon)
        self.prev_button.setIconSize(QSize(32, 32))

        # Connect buttons to functions

        
        layout.addLayout(controls_layout)
        self.setLayout(layout)