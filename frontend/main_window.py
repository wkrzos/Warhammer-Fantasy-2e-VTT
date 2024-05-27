import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QSplitter, QTabWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QTranslator, QLocale

from backend.musicManager.musicManager import MusicEventTypes
from frontend.widgets.toolbar import Toolbar
from frontend.widgets.mapview import MapView
from frontend.widgets.chatview import ChatView, CharactersView, ItemsView, CreaturesView, MusicPlayerView, OptionsView
from frontend.widgets.actionpanel import ActionPanel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(self.tr("BFVTT Application"))
        self.setGeometry(100, 100, 1200, 800)

        # Set the application icon
        icon_path = os.path.join(os.path.dirname(__file__), 'frontend/resources/logo/bfvtt_icon_no_bg.png')
        self.setWindowIcon(QIcon(icon_path))

        self.music_player_view = MusicPlayerView()
        self.initUI()

    def initUI(self):
        main_layout = QHBoxLayout()

        # Create the toolbar
        self.toolbar = Toolbar(self)
        self.toolbar.setFixedWidth(60)

        # Create the map view and pass a reference to the main window
        self.map_view = MapView(self)

        # Create the tab widget for the right panel
        right_tab_widget = QTabWidget()
        right_tab_widget.setFixedWidth(300)

        # Add tabs
        chat_view = ChatView()
        characters_view = CharactersView()
        creatures_view = CreaturesView()
        items_view = ItemsView()
        options_view = OptionsView()
        
        right_tab_widget.addTab(chat_view, self.tr("Chat"))
        right_tab_widget.addTab(characters_view, self.tr("Characters"))
        right_tab_widget.addTab(creatures_view, self.tr("Creatures"))
        right_tab_widget.addTab(items_view, self.tr("Items"))
        right_tab_widget.addTab(self.music_player_view, self.tr("Music Player"))
        right_tab_widget.addTab(options_view, self.tr("Options"))

        # Splitter to allow resizing
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.map_view)
        splitter.addWidget(right_tab_widget)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 0)

        # Create the action panel
        self.action_panel = ActionPanel(self)
        self.action_panel.setFixedWidth(200)

        # Add components to the main layout
        main_layout.addWidget(self.toolbar)
        main_layout.addWidget(splitter)
        main_layout.addWidget(self.action_panel)

        # Set the central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def closeEvent(self, event):
        # self.music_player_view.music_manager.command = MusicEventTypes.CLOSE
        # self.music_player_view.music_thread.join()
        event.accept()

    def update_action_panel(self):
        self.action_panel.update_actions(self.map_view.selected_tokens)

def main():
    app = QApplication(sys.argv)

    # Load stylesheet
    stylesheet_path = os.path.join(os.path.dirname(__file__), 'frontend/resources/styles.qss')
    try:
        with open(stylesheet_path, "r") as file:
            app.setStyleSheet(file.read())
    except FileNotFoundError:
        print(f"Stylesheet not found at {stylesheet_path}")

    # Load translations
    translator = QTranslator()
    # Set the language you want to load, e.g., "pl" for Polish
    language = "pl"
    translation_file = f"translations/{language}.qm"
    if translator.load(translation_file):
        app.installTranslator(translator)
    else:
        print(f"Translation file not found: {translation_file}")

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
