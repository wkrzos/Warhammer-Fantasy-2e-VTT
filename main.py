import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from model.main_window_model import MainWindowModel
from frontend.main_window_ui import MainWindowView
from controller.main_window_controller import MainWindowController
from frontend.widgets.welcome_screen_ui import SplashScreen
from model.welcome_screen_model import WelcomeScreenModel
from controller.welcome_screen_controller import WelcomeScreenController
from translations.gui_translator import GuiTranslator



if __name__ == '__main__':
    app = QApplication(sys.argv)

    welcome_model = WelcomeScreenModel()
    splash = SplashScreen()
    welcome_controller = WelcomeScreenController(welcome_model, splash)
    splash.show()

    def start_main_window():
        splash.fade_out()

        selected_language = welcome_model.get_language()
        translator = GuiTranslator.load_translations(app, selected_language)

        main_window = QMainWindow()
        main_window_model = MainWindowModel()
        main_window_view = MainWindowView(main_window)  
        main_window_controller = MainWindowController(main_window_model, main_window_view)
        main_window.show()

    splash.language_selected.connect(start_main_window)

    sys.exit(app.exec())
