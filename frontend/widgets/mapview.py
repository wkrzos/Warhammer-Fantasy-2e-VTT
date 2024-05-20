from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class MapView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Map View"))
        self.setLayout(layout)
