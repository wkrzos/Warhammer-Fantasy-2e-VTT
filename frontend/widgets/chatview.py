import time

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QHBoxLayout, QFileDialog, \
    QTextEdit, QAbstractItemView
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
import threading
import os
from backend.musicManager.musicManager import *
from backend.paterns.observer.observer import Observer


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

class MusicPlayerView(QWidget, Observer):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        
        # Correct path to the music folder
        music_folder_path = os.path.join(os.path.dirname(__file__), '../../music')
        self.music_manager = MusicManager(music_folder_path)
        MusicManager.attach(self)
        self.music_thread = threading.Thread(target=self.music_manager.run)
        self.music_thread.start()

        self.load_playlist()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Music Player"))
        self.playlist = QListWidget()
        self.playlist.setCurrentRow(0)
        self.playlist.currentRowChanged.connect(self.select_song_on_list)
        self.playlist.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

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
        self.toggle_button.clicked.connect(self.toggle_play_stop)
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
        self.pause_button.clicked.connect(self.pause_music)
        self.next_button.clicked.connect(self.next_music)
        self.prev_button.clicked.connect(self.prev_music)
        
        controls_layout.addWidget(self.prev_button)
        controls_layout.addWidget(self.toggle_button)
        controls_layout.addWidget(self.pause_button)
        controls_layout.addWidget(self.next_button)
        
        layout.addLayout(controls_layout)
        self.setLayout(layout)
        
    def load_playlist(self):
        self.playlist.clear()
        for song in self.music_manager.playlist:
            self.playlist.addItem(os.path.basename(song))
            
    def toggle_play_stop(self):
        if self.is_playing:
            self.stop_music()
        else:
            self.play_music()

    def play_music(self):
        with self.music_manager.lock:
            self.music_manager.command = MusicEventTypes.UNPAUSE
        self.toggle_button.setIcon(self.stop_icon)
        self.is_playing = True
            
    def stop_music(self):
        with self.music_manager.lock:
            self.music_manager.command = MusicEventTypes.PAUSE
        self.toggle_button.setIcon(self.play_icon)
        self.is_playing = False
            
    def pause_music(self):
        with self.music_manager.lock:
            self.music_manager.command = MusicEventTypes.REWIND
        time.sleep(0.03)
        with self.music_manager.lock:
            self.music_manager.command = MusicEventTypes.PAUSE
        self.toggle_button.setIcon(self.play_icon)
        self.is_playing = False
    def next_music(self):
        with self.music_manager.lock:
            self.music_manager.command = MusicEventTypes.NEXT
            
    def prev_music(self):
        with self.music_manager.lock:
            self.music_manager.command = MusicEventTypes.PREVIOUS
    def reactForNotify(self, subject):
        self.playlist.setCurrentRow(subject)

    def select_song_on_list(self, item):
        with self.music_manager.lock:
            self.music_manager.currentIndex = item
            self.music_manager.command = MusicEventTypes.PAUSE
        time.sleep(0.03)
        with self.music_manager.lock:
            self.music_manager.command = MusicEventTypes.PLAY