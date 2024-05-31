import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from model.main_window_model import MainWindowModel
from frontend.main_window_ui import MainWindowView
from controller.main_window_controller import MainWindowController
from frontend.widgets.welcome_screen_ui import WelcomeScreen

def show_main_window():
    main_window = QMainWindow()
    main_window_model = MainWindowModel()
    main_window_view = MainWindowView(main_window)
    main_window_controller = MainWindowController(main_window_model, main_window_view)
    main_window.show()

def main():
    app = QApplication(sys.argv)

    welcome_screen = WelcomeScreen(show_main_window)
    welcome_screen.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
