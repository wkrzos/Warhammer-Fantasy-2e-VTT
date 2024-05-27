import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
from PySide6.QtCore import QTranslator

from backend.musicManager.musicManager import MusicEventTypes
from frontend.main_window_ui import MainWindowUI

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = MainWindowUI(self)
        self.ui.setup_ui()

        self.ui.music_player_view = self.ui.create_music_player_view()

    def closeEvent(self, event):
        self.ui.music_player_view.music_manager.command = MusicEventTypes.CLOSE
        self.ui.music_player_view.music_thread.join()
        event.accept()

    def update_action_panel(self):
        self.ui.action_panel.update_actions(self.ui.map_view.selected_tokens)

def main():
    app = QApplication(sys.argv)

    stylesheet_path = os.path.join(os.path.dirname(__file__), 'frontend/resources/styles.qss')
    try:
        with open(stylesheet_path, "r") as file:
            app.setStyleSheet(file.read())
    except FileNotFoundError:
        print(f"Stylesheet not found at {stylesheet_path}")

    translator = QTranslator()
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
