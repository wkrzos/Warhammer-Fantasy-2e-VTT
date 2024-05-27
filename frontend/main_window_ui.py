import os
from PySide6.QtWidgets import QHBoxLayout, QWidget, QSplitter, QTabWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from model.toolbar_model import ToolbarModel
from frontend.widgets.toolbar_ui import ToolbarUI
from controller.toolbar_controller import ToolbarController
from model.mapview_model import MapViewModel
from frontend.widgets.mapview_ui import MapViewUI
from controller.mapview_controller import MapViewController
from model.chat_model import ChatModel
from frontend.widgets.chat_ui import ChatViewUI
from controller.chat_controller import ChatController
from model.creatures_model import CreaturesModel
from frontend.widgets.creatures_ui import CreaturesViewUI
from controller.creatures_controller import CreaturesController
from model.items_model import ItemsModel
from frontend.widgets.items_ui import ItemsViewUI
from controller.items_controller import ItemsController
from model.options_model import OptionsModel
from frontend.widgets.options_ui import OptionsViewUI
from controller.options_controller import OptionsController
from model.musicplayer_model import MusicPlayerModel
from frontend.widgets.musicplayer_ui import MusicPlayerViewUI
from controller.musicplayer_controller import MusicPlayerController
from model.actionpanel_model import ActionPanelModel
from frontend.widgets.actionpanel_ui import ActionPanelUI
from controller.actionpanel_controller import ActionPanelController

class MainWindowUI:
    def __init__(self, main_window):
        self.main_window = main_window
        self.music_player_model = MusicPlayerModel(os.path.join(os.path.dirname(__file__), '../../music'))
        self.music_player_view_ui = MusicPlayerViewUI(self.main_window)
        self.music_player_controller = MusicPlayerController(self.music_player_model, self.music_player_view_ui)
        self.toolbar_model = ToolbarModel()
        self.toolbar_view = ToolbarUI(self.main_window)
        self.toolbar_controller = ToolbarController(self.toolbar_model, self.toolbar_view)
        self.map_view_model = MapViewModel()
        self.map_view_ui = MapViewUI(self.map_view_model, self.main_window)
        self.map_view_controller = MapViewController(self.map_view_model, self.map_view_ui, self.main_window)
        self.chat_model = ChatModel()
        self.chat_view_ui = ChatViewUI(self.main_window)
        self.chat_controller = ChatController(self.chat_model, self.chat_view_ui)
        self.creatures_model = CreaturesModel()
        self.creatures_view_ui = CreaturesViewUI(self.main_window)
        self.creatures_controller = CreaturesController(self.creatures_model, self.creatures_view_ui)
        self.items_model = ItemsModel()
        self.items_view_ui = ItemsViewUI(self.main_window)
        self.items_controller = ItemsController(self.items_model, self.items_view_ui)
        self.options_model = OptionsModel()
        self.options_view_ui = OptionsViewUI(self.main_window)
        self.options_controller = OptionsController(self.options_model, self.options_view_ui)
        self.action_panel_model = ActionPanelModel()
        self.action_panel_ui = ActionPanelUI(self.main_window)
        self.action_panel_controller = ActionPanelController(self.action_panel_model, self.action_panel_ui)

    def setup_ui(self):
        self.main_window.setWindowTitle(self.main_window.tr("BFVTT Application"))
        self.main_window.setGeometry(100, 100, 1200, 800)

        icon_path = os.path.join(os.path.dirname(__file__), 'frontend/resources/logo/bfvtt_icon_no_bg.png')
        self.main_window.setWindowIcon(QIcon(icon_path))

        self.initUI()

    def initUI(self):
        main_layout = QHBoxLayout()

        self.toolbar_view.setFixedWidth(60)

        right_tab_widget = QTabWidget()
        right_tab_widget.setFixedWidth(300)

        characters_view = CreaturesViewUI(self.main_window)
        
        right_tab_widget.addTab(self.chat_view_ui, self.main_window.tr("Chat"))
        right_tab_widget.addTab(characters_view, self.main_window.tr("Characters"))
        right_tab_widget.addTab(self.creatures_view_ui, self.main_window.tr("Creatures"))
        right_tab_widget.addTab(self.items_view_ui, self.main_window.tr("Items"))
        right_tab_widget.addTab(self.music_player_view_ui, self.main_window.tr("Music Player"))
        right_tab_widget.addTab(self.options_view_ui, self.main_window.tr("Options"))

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.map_view_ui)
        splitter.addWidget(right_tab_widget)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 0)

        self.action_panel_ui.setFixedWidth(200)

        main_layout.addWidget(self.toolbar_view)
        main_layout.addWidget(splitter)
        main_layout.addWidget(self.action_panel_ui)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.main_window.setCentralWidget(central_widget)

