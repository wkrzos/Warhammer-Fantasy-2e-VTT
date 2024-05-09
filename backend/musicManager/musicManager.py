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
        self.command = MusicEventTypes.PLAY
        self.lock = threading.Lock()


    def loadPlaylist(self) -> list[str]:
        for root, dirs, files in os.walk(self.musicFolderPath):
            for file in files:
                if file.endswith(('.mp3', '.wav', '.ogg', '.flac')):
                    self.playlist.append(os.path.join(root, file))

    def checkExternalEvents(self): #Temp test function
        while True:
            user_input = input("Wpisz 'stop', aby zatrzymać odtwarzanie lub 'next', aby przejść do następnego utworu: ")
            if user_input.lower() == "stop":
                with self.lock:

                    self.command = MusicEventTypes.PAUSE
            elif user_input.lower() == "play":
                with self.lock:

                    self.command = MusicEventTypes.PLAY
    def run(self):
        mixer.init()
        while True:
            time.sleep(0.1)
            match self.command:
                case MusicEventTypes.PLAY:
                    with self.lock:
                        self.command = MusicEventTypes.WAIT
                    self.play()



    def play(self):
        while self.currentIndex < len(self.playlist):
            mixer.music.load(self.playlist[self.currentIndex])
            mixer.music.play()
            while mixer.music.get_busy():
                time.sleep(0.1)
                with self.lock:
                    match self.command:
                        case MusicEventTypes.PAUSE:
                            self.pause()
                            break
                        case MusicEventTypes.NEXT:
                            self.next()
                            self.command = MusicEventTypes.WAIT
                        case MusicEventTypes.PREVIOUS:
                            self.previous()
                            self.command = MusicEventTypes.WAIT
                        case MusicEventTypes.REWIND:
                            self.rewind()
                            self.command = MusicEventTypes.WAIT
            self.currentIndex = (self.currentIndex + 1) % len(self.playlist)
            if self.command == MusicEventTypes.PAUSE:
                self.command = MusicEventTypes.WAIT
                break

    def pause(self):
        mixer.music.pause()
    def next(self):
        mixer.music.stop()
        self.currentIndex = (self.currentIndex - 1) % len(self.playlist) if self.currentIndex > 0 else len(
            self.playlist) - 1
        mixer.music.load(self.playlist[self.currentIndex])
        mixer.music.play()
    def previous(self):
        mixer.music.stop()
        self.currentIndex = (self.currentIndex + 1) % len(self.playlist)
        mixer.music.load(self.playlist[self.currentIndex])
        mixer.music.play()
    def rewind(self):
        mixer.music.rewind()


class MusicEventTypes(Enum):
    WAIT = -1
    PLAY = 0
    PAUSE = 1
    NEXT = 2
    PREVIOUS = 3
    REWIND = 4


if __name__ == "__main__":
    test = MusicManager(r"C:\Users\FilipPuszko(272731)\PycharmProjects\bardzofajenvtt\music")
    music_thread = threading.Thread(target=test.run)
    music_thread.start()
    test.checkExternalEvents()
    time.sleep(10)
