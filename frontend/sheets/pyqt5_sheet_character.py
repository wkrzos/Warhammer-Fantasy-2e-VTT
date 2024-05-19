import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QComboBox, QLabel, QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class CharacterSheet(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 1000)
        self.setWindowTitle('Warhammer Fantasy Roleplay Character Sheet')

        widget = QWidget()
        self.setCentralWidget(widget)

        layout = QVBoxLayout()

        # Character Section
        character_layout = QFormLayout()
        character_layout.addRow('Name:', QLineEdit())
        race_combo = QComboBox()
        race_combo.addItems(['Human', 'Elf', 'Dwarf', 'Halfling'])
        character_layout.addRow('Race:', race_combo)
        character_layout.addRow('Current Career:', QLineEdit())
        character_layout.addRow('Previous Careers:', QLineEdit())

        layout.addLayout(character_layout)
        layout.addWidget(QLabel(""))

        # Personal Details Section
        personal_details_layout = QFormLayout()
        personal_details_layout.addRow('Age:', QLineEdit())
        personal_details_layout.addRow('Gender:', QLineEdit())
        personal_details_layout.addRow('Height:', QLineEdit())
        personal_details_layout.addRow('Weight:', QLineEdit())
        personal_details_layout.addRow('Eyes Color:', QLineEdit())
        personal_details_layout.addRow('Hair Color:', QLineEdit())
        personal_details_layout.addRow('Star Sign:', QLineEdit())
        personal_details_layout.addRow('Number of Siblings:', QLineEdit())
        personal_details_layout.addRow('Birthplace:', QLineEdit())
        personal_details_layout.addRow('Distinguishing Marks:', QLineEdit())

        layout.addLayout(personal_details_layout)
        layout.addWidget(QLabel(""))

        # Character Profile Section
        profile_layout = QGridLayout()
        profile_layout.addWidget(QLabel("Character Profile"), 0, 0, 1, 8)

        stats = ['WS', 'BS', 'S', 'T', 'Ag', 'Int', 'WP', 'Fel']
        profile_layout.addWidget(QLabel("Main"), 1, 0)
        for i, stat in enumerate(stats):
            profile_layout.addWidget(QLabel(stat), 1, i+1)

        for i in range(3):  # Assuming 3 rows for Starting, Advance, Current
            for j in range(8):  # 8 stats columns
                profile_layout.addWidget(QLineEdit(), i+2, j+1)

        layout.addLayout(profile_layout)

        widget.setLayout(layout)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CharacterSheet()
    sys.exit(app.exec_())
