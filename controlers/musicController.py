import os
import threading
from datetime import time

from PySide6.QtWidgets import QAbstractItemView

from backend.musicManager.musicManager import MusicManager, MusicEventTypes
from backend.paterns.observer.observer import Observer
from frontend.widgets.chatview import MusicPlayerView


class MusicPlayerController(Observer):

    def __init__(self, view:MusicPlayerView = MusicPlayerView()):
        self.view = view
        music_folder_path = os.path.join(os.path.dirname(__file__), '../../music')
        self.music_manager = MusicManager(music_folder_path)
        MusicManager.attach(self)
        self.music_thread = threading.Thread(target=self.music_manager.run, daemon=True)
        self.music_thread.start()
        self.connect_view()
        self.load_playlist()


    def connect_view(self):


        # Connect playlist to functions
        self.view.playlist.setCurrentRow(0)
        self.view.playlist.currentRowChanged.connect(self.select_song_on_list)
        self.view.playlist.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)



        # Connect buttons to functions
        self.view.toggle_button.clicked.connect(self.toggle_play_stop)
        self.view.pause_button.clicked.connect(self.pause_music)
        self.view.next_button.clicked.connect(self.next_music)
        self.view.prev_button.clicked.connect(self.prev_music)

    def load_playlist(self):
        self.view.playlist.clear()
        for song in self.music_manager.playlist:
            self.view.playlist.addItem(os.path.basename(song))

    def toggle_play_stop(self):
        if self.is_playing:
            self.stop_music()
        else:
            self.play_music()

    def play_music(self):
        with self.music_manager.lock:
            self.music_manager.command = MusicEventTypes.UNPAUSE
        self.view.toggle_button.setIcon(self.stop_icon)
        self.is_playing = True

    def stop_music(self):
        with self.music_manager.lock:
            self.music_manager.command = MusicEventTypes.PAUSE
        self.view.toggle_button.setIcon(self.play_icon)
        self.is_playing = False

    def pause_music(self):
        with self.music_manager.lock:
            self.music_manager.command = MusicEventTypes.REWIND
        time.sleep(0.03)
        with self.music_manager.lock:
            self.music_manager.command = MusicEventTypes.PAUSE
        self.view.toggle_button.setIcon(self.play_icon)
        self.is_playing = False

    def next_music(self):
        with self.music_manager.lock:
            self.music_manager.command = MusicEventTypes.NEXT

    def prev_music(self):
        with self.music_manager.lock:
            self.music_manager.command = MusicEventTypes.PREVIOUS

    def reactForNotify(self, subject):
        self.view.playlist.setCurrentRow(subject)

    def select_song_on_list(self, item):
        with self.music_manager.lock:
            self.music_manager.currentIndex = item
            self.music_manager.command = MusicEventTypes.PAUSE
        time.sleep(0.03)
        with self.music_manager.lock:
            self.music_manager.command = MusicEventTypes.PLAY
