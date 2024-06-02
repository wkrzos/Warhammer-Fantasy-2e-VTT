# main_window_ui.py

import os
from PySide6.QtWidgets import QHBoxLayout, QWidget, QSplitter, QTabWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from model.toolbar_model import ToolbarModel
from frontend.widgets.toolbar_ui import ToolbarUI
from controller.toolbar_controller import ToolbarController
from model.map_model import MapViewModel
from frontend.widgets.map_ui import MapViewUI
from controller.map_controller import MapViewController
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
from model.music_player_model import MusicPlayerModel
from frontend.widgets.music_player_ui import MusicPlayerViewUI
from controller.music_player_controller import MusicPlayerController
from model.action_panel_model import ActionPanelModel
from frontend.widgets.action_panel_ui import ActionPanelUI
from frontend.widgets.characters_ui import CharactersViewUI
from frontend.widgets.welcome_screen_ui import SplashScreen
from translations.gui_translator import GuiTranslator

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QHBoxLayout, QPushButton, QAbstractItemView, \
    QListWidgetItem
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, QObject
import os
from frontend.util.font import DEFAULT_FONT

class MainWindowView(QWidget):
    def __init__(self, main_window):
        self.main_window = main_window
        self.map_view_ui = MapViewUI(self.main_window)
        self.toolbar_view = ToolbarUI(self.main_window)
        self.chat_view_ui = ChatViewUI(self.main_window)
        self.characters_view_ui = CharactersViewUI(self.main_window)
        self.creatures_view_ui = CreaturesViewUI(self.main_window)
        self.items_view_ui = ItemsViewUI(self.main_window)
        self.options_view_ui = OptionsViewUI(self.main_window)
        self.music_player_view_ui = MusicPlayerViewUI(self.main_window)
        self.action_panel_ui = ActionPanelUI(self.main_window)
        self.welcome_screen_view = SplashScreen()
        
    def setup_ui(self, model):
        self.main_window.setWindowTitle(self.main_window.tr(model.title))
        self.main_window.setGeometry(*model.geometry)

        icon_path = model.icon_path
        if not os.path.exists(icon_path):
            print(f"Icon path does not exist: {icon_path}")
        else:
            print(f"Setting icon from: {icon_path}")
        
        self.main_window.setWindowIcon(QIcon(icon_path))

        self.init_ui()

    def init_ui(self):
        main_layout = QHBoxLayout()

        self.toolbar_view.setFixedWidth(60)

        self.right_tab_widget = QTabWidget()
        self.right_tab_widget.setFixedWidth(300)
        
        self.right_tab_widget.addTab(self.chat_view_ui, self.tr("Chat"))
        self.right_tab_widget.addTab(self.characters_view_ui, self.tr("Characters"))
        self.right_tab_widget.addTab(self.creatures_view_ui, self.tr("Creatures"))
        self.right_tab_widget.addTab(self.items_view_ui, self.tr("Items"))
        self.right_tab_widget.addTab(self.music_player_view_ui, self.tr("Music Player"))
        self.right_tab_widget.addTab(self.options_view_ui, self.tr("Options"))

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.map_view_ui)
        splitter.addWidget(self.right_tab_widget)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 0)

        self.action_panel_ui.setFixedWidth(200)

        main_layout.addWidget(self.toolbar_view)
        main_layout.addWidget(splitter)
        main_layout.addWidget(self.action_panel_ui)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.main_window.setCentralWidget(central_widget)
