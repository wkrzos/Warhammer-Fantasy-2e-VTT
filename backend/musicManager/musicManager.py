import enum
import os
import threading
import time
from enum import Enum
from pygame import mixer

class MusicManager:
    def __init__(self, musicFolderPath):
        self.musicFolderPath = musicFolderPath
        self.currentIndex = 0
        self.playlist = []
        self.loadPlaylist()
        self.command = MusicEventTypes.WAIT
        self.lock = threading.Lock()


    def loadPlaylist(self) -> None:
        for root, dirs, files in os.walk(self.musicFolderPath):
            for file in files:
                if file.endswith(('.mp3', '.wav', '.ogg', '.flac')):
                    self.playlist.append(os.path.join(root, file))

    def run(self) -> int:
        mixer.init()
        self.play()
        while True:
            time.sleep(0.025)
            with self.lock:
                if self.command == MusicEventTypes.UNPAUSE:
                    self.unpause()
                    self.command = MusicEventTypes.WAIT
                elif self.command == MusicEventTypes.PAUSE:
                    self.pause()
                    self.command = MusicEventTypes.WAIT
                elif self.command == MusicEventTypes.NEXT:
                    self.next()
                    self.command = MusicEventTypes.WAIT
                elif self.command == MusicEventTypes.PREVIOUS:
                    self.previous()
                    self.command = MusicEventTypes.WAIT
                elif self.command == MusicEventTypes.REWIND:
                    self.rewind()
                    self.command = MusicEventTypes.WAIT
                elif self.command == MusicEventTypes.PLAY:
                    if not mixer.music.get_busy():
                        self.play()
                    self.command = MusicEventTypes.WAIT
                elif self.command == MusicEventTypes.CLOSE:
                    return 0
    def play(self) -> None:
        mixer.music.load(self.playlist[self.currentIndex])
        mixer.music.play()

    def pause(self) -> None:
        mixer.music.pause()

    def unpause(self) -> None:
        mixer.music.unpause()

    def next(self) -> None:
        self.currentIndex = (self.currentIndex + 1) % len(self.playlist)
        self.play()

    def previous(self) -> None:
        self.currentIndex = (self.currentIndex - 1) % len(self.playlist)
        self.play()

    def rewind(self) -> None:
        mixer.music.rewind()

    def setVolume(self, volume: int) -> None:
        if volume < 0:
            mixer.music.set_volume(0)
        elif volume > 1:
            mixer.music.set_volume(1)
        else:
            mixer.music.set_volume(volume)

class MusicEventTypes(Enum):
    CLOSE = -2,
    WAIT = -1
    PLAY = 0
    PAUSE = 1
    NEXT = 2
    PREVIOUS = 3
    REWIND = 4
    UNPAUSE = 5
