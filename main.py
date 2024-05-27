import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from model.main_window_model import MainWindowModel
from frontend.main_window_ui import MainWindowView
from controller.main_window_controller import MainWindowController

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window_model = MainWindowModel()
    main_window_view = MainWindowView(main_window)
    main_window_controller = MainWindowController(main_window_model, main_window_view)
    main_window.show()
    sys.exit(app.exec())
