import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QSplitter
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

from frontend.widgets.toolbar import Toolbar
from frontend.widgets.mapview import MapView
from frontend.widgets.chatview import ChatView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BFVTT")
        self.setGeometry(100, 100, 1200, 800)

        self.setWindowIcon(QIcon("frontend/resources/logo/bfvtt_icon_no_bg.png"))

        self.initUI()

    def initUI(self):
        main_layout = QHBoxLayout()

        # Create the toolbar
        toolbar = Toolbar(self)
        toolbar.setFixedWidth(60)

        # Create the map view
        map_view = MapView()

        # Create the chat view
        chat_view = ChatView()
        chat_view.setFixedWidth(300)

        # Splitter to allow resizing
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(map_view)
        splitter.addWidget(chat_view)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 0)

        # Add components to the main layout
        main_layout.addWidget(toolbar)
        main_layout.addWidget(splitter)

        # Set the central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

def main():
    app = QApplication(sys.argv)

    # Load stylesheet
    stylesheet_path = os.path.join(os.path.dirname(__file__), 'frontend/resources/styles.qss')
    try:
        with open(stylesheet_path, "r") as file:
            app.setStyleSheet(file.read())
    except FileNotFoundError:
        print(f"Stylesheet not found at {stylesheet_path}")

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
