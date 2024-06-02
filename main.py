import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTranslator, QTimer
from model.main_window_model import MainWindowModel
from frontend.main_window_ui import MainWindowView
from controller.main_window_controller import MainWindowController
from frontend.widgets.welcome_screen_ui import SplashScreen

def load_translations(app, language="en"):
    translator = QTranslator()
    translation_file = os.path.normpath(f"translations/{language}.qm")
    if translator.load(translation_file):
        app.installTranslator(translator)
        print(f"Loaded translation file: {translation_file}")
    else:
        print(f"Translation file not found: {translation_file}")
    return translator

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Load translations (default to English)
    translator = load_translations(app, "pl")

    splash = SplashScreen()
    splash.show()

    def start_main_window():
        splash.fade_out()

        main_window = QMainWindow()
        main_window_model = MainWindowModel()
        main_window_view = MainWindowView(main_window)
        main_window_controller = MainWindowController(main_window_model, main_window_view)
        main_window.show()

    QTimer.singleShot(3500, start_main_window)  # Display the splash screen for 3.5 seconds

    sys.exit(app.exec())
