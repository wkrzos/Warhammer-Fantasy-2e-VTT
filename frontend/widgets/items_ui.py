from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton
from frontend.util.font import DEFAULT_FONT

class ItemsViewUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        label = QLabel(self.tr("Items"))
        label.setFont(DEFAULT_FONT)
        layout.addWidget(label)

        self.item_list = QListWidget()
        self.item_list.setFont(DEFAULT_FONT)
        layout.addWidget(self.item_list)

        self.add_button = QPushButton(self.tr("Add Item"))
        self.add_button.setFont(DEFAULT_FONT)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def update_item_list(self, items):
        self.item_list.clear()
        for item in items:
            self.item_list.addItem(self.tr(item))
