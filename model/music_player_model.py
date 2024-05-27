import os
from backend.musicManager.music_manager import MusicManager, MusicEventTypes
from threading import Thread

class MusicPlayerModel:
    def __init__(self, music_folder_path):
        self.music_manager = MusicManager(music_folder_path)
        self.music_thread = Thread(target=self.music_manager.run)
        self.music_thread.start()
        self.is_playing = False
        self.current_index = 0

    def load_playlist(self):
        return [os.path.basename(song) for song in self.music_manager.playlist]

    def play_music(self):
        self.music_manager.command = MusicEventTypes.PLAY
        self.is_playing = True

    def stop_music(self):
        self.music_manager.command = MusicEventTypes.STOP
        self.is_playing = False

    def pause_music(self):
        self.music_manager.command = MusicEventTypes.PAUSE
        self.is_playing = False

    def next_music(self):
        self.music_manager.command = MusicEventTypes.NEXT

    def prev_music(self):
        self.music_manager.command = MusicEventTypes.PREVIOUS

    def select_song(self, index):
        self.music_manager.currentIndex = index
        self.music_manager.command = MusicEventTypes.PLAY
