from PySide6.QtWidgets import QVBoxLayout, QPushButton, QWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

class Toolbar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # List of tool icons
        tools = ["select", "pan", "measure", "other"]

        for tool in tools:
            button = QPushButton()
            button.setIcon(QIcon(f"frontend/resources/icons/{tool}.png"))
            button.setIconSize(QSize(40, 40))  # Use QSize instead of Qt.Size
            button.setFixedSize(50, 50)
            layout.addWidget(button)

        layout.addStretch()
        self.setLayout(layout)
