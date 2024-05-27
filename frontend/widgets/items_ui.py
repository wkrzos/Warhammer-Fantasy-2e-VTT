from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton

class ItemsViewUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Items"))

        self.item_list = QListWidget()
        layout.addWidget(self.item_list)

        self.add_button = QPushButton("Add Item")
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def update_item_list(self, items):
        self.item_list.clear()
        for item in items:
            self.item_list.addItem(item)
