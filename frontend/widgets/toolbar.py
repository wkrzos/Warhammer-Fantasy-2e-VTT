from PySide6.QtWidgets import QVBoxLayout, QPushButton, QWidget
from PySide6.QtGui import QIcon, QPalette, QColor
from PySide6.QtCore import QSize

class Toolbar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        self.selected_button = None

    def initUI(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # List of tool icons
        tools = ["select", "pan", "measure", "other"]

        self.buttons = []

        for tool in tools:
            button = QPushButton()
            button.setIcon(QIcon(f"frontend/resources/icons/{tool}.png"))
            button.setIconSize(QSize(40, 40))  # Use QSize instead of Qt.Size
            button.setFixedSize(50, 50)
            button.clicked.connect(self.button_clicked)
            layout.addWidget(button)
            self.buttons.append(button)

        layout.addStretch()
        self.setLayout(layout)

    def button_clicked(self):
        sender = self.sender()

        # Unhighlight the previously selected button
        if self.selected_button:
            self.selected_button.setStyleSheet("")

        # Highlight the selected button
        sender.setStyleSheet("background-color: lightblue;")
        self.selected_button = sender
