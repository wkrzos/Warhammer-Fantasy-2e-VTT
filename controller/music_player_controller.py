from backend.paterns.observer.observer import Observer
from frontend.widgets.music_player_ui import MusicPlayerViewUI
from model.music_player_model import MusicPlayerModel


class MusicPlayerController(Observer):
    def __init__(self, model:MusicPlayerModel, view:MusicPlayerViewUI):
        self.model = model
        self.view = view
        self.load_playlist()
        self.view.playlist.setCurrentRow(0)
        self.connect_signals()
        self.model.music_manager.attach(self)


    def connect_signals(self):
        self.view.play_button.clicked.connect(self.play_music)
        self.view.stop_button.clicked.connect(self.stop_music)
        self.view.pause_button.clicked.connect(self.pause_music)
        self.view.next_button.clicked.connect(self.next_music)
        self.view.prev_button.clicked.connect(self.prev_music)
        self.view.playlist.currentRowChanged.connect(self.select_song)

    def load_playlist(self):
        songs = self.model.load_playlist()
        self.view.update_playlist(songs)

    def play_music(self):
        self.model.play_music()
        self.view.toggle_button.setIcon(self.view.stop_icon)

    def stop_music(self):
        self.model.stop_music()
        self.view.toggle_button.setIcon(self.view.play_icon)

    def pause_music(self):
        self.model.pause_music()
        self.view.toggle_button.setIcon(self.view.play_icon)


    def next_music(self):
        self.model.next_music()

    def prev_music(self):
        self.model.prev_music()

    def select_song(self, index):
        self.model.select_song_on_list(index)

    def reactForNotify(self, subject):
        self.view.playlist.setCurrentRow(subject)
