# main.py

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from model.main_window_model import MainWindowModel
from frontend.main_window_ui import MainWindowView
from controller.main_window_controller import MainWindowController
from frontend.widgets.welcome_screen_ui import SplashScreen
from PySide6.QtCore import QTimer

if __name__ == '__main__':
    app = QApplication(sys.argv)

    splash = SplashScreen()
    splash.show()

    def start_main_window():
        splash.fade_out()

        main_window = QMainWindow()
        main_window_model = MainWindowModel()
        main_window_view = MainWindowView(main_window)
        main_window_controller = MainWindowController(main_window_model, main_window_view)
        main_window.show()

    QTimer.singleShot(4500, start_main_window)  # Display the splash screen for 2 seconds

    sys.exit(app.exec())
