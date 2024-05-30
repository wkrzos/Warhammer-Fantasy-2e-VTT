import os
import time

from backend.musicManager.music_manager import MusicManager, MusicEventTypes
from threading import Thread

from backend.paterns.observer.observer import Observer


class MusicPlayerModel():
    def __init__(self, music_folder_path):
        self.music_manager = MusicManager(music_folder_path)
        self.music_thread = Thread(target=self.music_manager.run, daemon=True)
        self.music_thread.start()
        self.is_playing = False
        self.current_index = 0

    def load_playlist(self):
        return [os.path.basename(song) for song in self.music_manager.playlist]

    def play_music(self):
        with self.music_manager.lock:
            self.music_manager.command = MusicEventTypes.UNPAUSE
        self.is_playing = True

    def stop_music(self):
        with self.music_manager.lock:
            self.music_manager.command = MusicEventTypes.PAUSE
        self.is_playing = False

    def pause_music(self):
        with self.music_manager.lock:
            self.music_manager.command = MusicEventTypes.REWIND
        time.sleep(0.03)
        with self.music_manager.lock:
            self.music_manager.command = MusicEventTypes.PAUSE
        self.is_playing = False

    def next_music(self):
        with self.music_manager.lock:
            self.music_manager.command = MusicEventTypes.NEXT

    def prev_music(self):
        with self.music_manager.lock:
            self.music_manager.command = MusicEventTypes.PREVIOUS


    def select_song_on_list(self, item):
        with self.music_manager.lock:
            self.music_manager.currentIndex = item
            self.music_manager.command = MusicEventTypes.PAUSE
        time.sleep(0.03)
        with self.music_manager.lock:
            self.music_manager.command = MusicEventTypes.PLAY