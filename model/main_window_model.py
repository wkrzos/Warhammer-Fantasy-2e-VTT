import os

from model.action_panel_model import ActionPanelModel
from model.chat_model import ChatModel
from model.creatures_model import CreaturesModel
from model.items_model import ItemsModel
from model.map_model import MapViewModel
from model.music_player_model import MusicPlayerModel
from model.options_model import OptionsModel
from model.toolbar_model import ToolbarModel


class MainWindowModel:
    def __init__(self):
        self.title = "BFVTT Application"
        self.geometry = (100, 100, 1200, 800)
        self.icon_path = 'frontend/resources/logo/bfvtt_icon_no_bg.png'
        self.toolbar_model = ToolbarModel()
        self.map_view_model = MapViewModel()
        self.chat_model = ChatModel()
        self.items_model = ItemsModel()
        self.creatures_model = CreaturesModel()
        self.options_model = OptionsModel()
        self.music_player_model = MusicPlayerModel((os.path.join(os.path.dirname(__file__), '../music')))
        self.action_panel_model = ActionPanelModel()
