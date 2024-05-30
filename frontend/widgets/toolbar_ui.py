from PySide6.QtWidgets import QVBoxLayout, QPushButton, QWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

class ToolbarUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.buttons = {}
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # List of tool icons and corresponding actions
        tools = [("select", self.tr("Select")), ("pan", self.tr("Pan")), ("measure", self.tr("Measure"))]

        for tool, action in tools:
            button = QPushButton()
            button.setIcon(QIcon(f"frontend/resources/icons/{tool}.png"))
            button.setIconSize(QSize(40, 40))
            button.setFixedSize(50, 50)
            button.setObjectName(tool)
            layout.addWidget(button)
            self.buttons[tool] = button

        layout.addStretch()
        self.setLayout(layout)

    def highlight_button(self, tool):
        for btn in self.buttons.values():
            btn.setStyleSheet("")
        if tool in self.buttons:
            self.buttons[tool].setStyleSheet("background-color: lightblue;")
