from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton

class CreaturesViewUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel(self.tr("Creatures")))

        self.creature_list = QListWidget()
        layout.addWidget(self.creature_list)

        self.add_button = QPushButton(self.tr("Add Creature"))
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def update_creature_list(self, creatures):
        self.creature_list.clear()
        for creature in creatures:
            self.creature_list.addItem(self.tr(creature))
