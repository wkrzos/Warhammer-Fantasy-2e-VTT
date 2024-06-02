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

class MainWindowView:
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

        right_tab_widget = QTabWidget()
        right_tab_widget.setFixedWidth(300)
        
        right_tab_widget.addTab(self.chat_view_ui, self.main_window.tr("Chat"))
        right_tab_widget.addTab(self.characters_view_ui, self.main_window.tr("Characters"))
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

    def retranslateUi(self):
        self.main_window.setWindowTitle(self.main_window.tr("BFVTT Application"))
        # Update tab titles
        right_tab_widget = self.main_window.centralWidget().findChild(QTabWidget)
        if right_tab_widget:
            right_tab_widget.setTabText(0, self.main_window.tr("Chat"))
            right_tab_widget.setTabText(1, self.main_window.tr("Characters"))
            right_tab_widget.setTabText(2, self.main_window.tr("Creatures"))
            right_tab_widget.setTabText(3, self.main_window.tr("Items"))
            right_tab_widget.setTabText(4, self.main_window.tr("Music Player"))
            right_tab_widget.setTabText(5, self.main_window.tr("Options"))
        # Add similar calls for other UI elements here

