from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton
from frontend.util.font import DEFAULT_FONT

class CreaturesViewUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        label = QLabel(self.tr("Creatures"))
        label.setFont(DEFAULT_FONT)
        layout.addWidget(label)

        self.creature_list = QListWidget()
        self.creature_list.setFont(DEFAULT_FONT)
        layout.addWidget(self.creature_list)

        self.add_button = QPushButton(self.tr("Add Creature"))
        self.add_button.setFont(DEFAULT_FONT)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def update_creature_list(self, creatures):
        self.creature_list.clear()
        for creature in creatures:
            self.creature_list.addItem(self.tr(creature.name))
