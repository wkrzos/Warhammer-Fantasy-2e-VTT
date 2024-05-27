import os
import sys

from PySide6.QtWidgets import QApplication
try:
    from controlers.musicController import MusicPlayerController
except ImportError as e:
    print(e)
from frontend.main_window import MainWindow


class MainController:
    def __init__(self):
        self.mainWindow = MainWindow()
        self.musicController = MusicPlayerController(self.mainWindow.music_player_view)




def main():
    app = QApplication(sys.argv)

    # Load stylesheet
    stylesheet_path = os.path.join(os.path.dirname(__file__), 'frontend/resources/styles.qss')
    try:
        with open(stylesheet_path, "r") as file:
            app.setStyleSheet(file.read())
    except FileNotFoundError:
        print(f"Stylesheet not found at {stylesheet_path}")


    mainController = MainController()
    mainController.mainWindow.show()


    sys.exit(app.exec())

if __name__ == '__main__':
    main()
