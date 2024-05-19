import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QComboBox, QLabel, QGridLayout, QGroupBox, QHBoxLayout)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

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
        character_group = QGroupBox("Character")
        character_layout = QFormLayout()
        character_layout.addRow('Name:', QLineEdit())
        race_combo = QComboBox()
        race_combo.addItems(['Human', 'Elf', 'Dwarf', 'Halfling'])
        character_layout.addRow('Race:', race_combo)
        character_layout.addRow('Current Career:', QLineEdit())
        character_layout.addRow('Previous Careers:', QLineEdit())
        character_group.setLayout(character_layout)
        layout.addWidget(character_group)

        # Personal Details Section
        personal_group = QGroupBox("Personal Details")
        personal_layout = QFormLayout()
        personal_layout.addRow('Age:', QLineEdit())
        personal_layout.addRow('Gender:', QLineEdit())
        personal_layout.addRow('Height:', QLineEdit())
        personal_layout.addRow('Weight:', QLineEdit())
        personal_layout.addRow('Eyes Color:', QLineEdit())
        personal_layout.addRow('Hair Color:', QLineEdit())
        personal_layout.addRow('Star Sign:', QLineEdit())
        personal_layout.addRow('Number of Siblings:', QLineEdit())
        personal_layout.addRow('Birthplace:', QLineEdit())
        personal_layout.addRow('Distinguishing Marks:', QLineEdit())
        personal_group.setLayout(personal_layout)
        layout.addWidget(personal_group)

        # Character Profile Section
        profile_group = QGroupBox("Character Profile")
        profile_layout = QGridLayout()
        stats = ['WS', 'BS', 'S', 'T', 'Ag', 'Int', 'WP', 'Fel']
        profile_layout.addWidget(QLabel("Main"), 0, 0)
        for i, stat in enumerate(stats):
            profile_layout.addWidget(QLabel(stat), 0, i + 1)
        for i in range(3):  # 3 rows for Starting, Advance, Current
            for j in range(8):  # 8 stats columns
                profile_layout.addWidget(QLineEdit(), i + 1, j + 1)
        profile_group.setLayout(profile_layout)
        layout.addWidget(profile_group)

        # Weapons Section
        weapons_group = QGroupBox("Weapons")
        weapons_layout = QGridLayout()
        weapons_headers = ['Name', 'Enc', 'Group', 'Damage', 'Range', 'Reload', 'Qualities']
        for i, header in enumerate(weapons_headers):
            weapons_layout.addWidget(QLabel(header), 0, i)
        for i in range(5):  # 5 rows for weapon entries
            for j in range(len(weapons_headers)):
                weapons_layout.addWidget(QLineEdit(), i + 1, j)
        weapons_group.setLayout(weapons_layout)
        layout.addWidget(weapons_group)

        # Armour and Experience Points Sections Side by Side
        armour_exp_layout = QHBoxLayout()

        # Armour Section
        armour_group = QGroupBox("Armour")
        armour_layout = QFormLayout()
        armour_layout.addRow('Basic Armour:', QLineEdit())
        armour_layout.addRow('Advanced Armour:', QLineEdit())
        armour_group.setLayout(armour_layout)
        armour_exp_layout.addWidget(armour_group)

        # Experience Points Section
        exp_group = QGroupBox("Experience Points")
        exp_layout = QFormLayout()
        exp_layout.addRow('Total:', QLineEdit())
        exp_group.setLayout(exp_layout)
        armour_exp_layout.addWidget(exp_group)
        
        # Combat Movement Section
        combat_group = QGroupBox("Combat Movement")
        combat_layout = QFormLayout()
        combat_layout.addRow('Move/Disengage:', QLineEdit())
        combat_layout.addRow('Charge Attack:', QLineEdit())
        combat_layout.addRow('Run:', QLineEdit())
        combat_group.setLayout(combat_layout)
        armour_exp_layout.addWidget(combat_group)

        layout.addLayout(armour_exp_layout)

        # Action Summary Section
        action_group = QGroupBox("Action Summary")
        action_layout = QVBoxLayout()
        action_summary = QLabel("Basic Action | Type | Advanced Action | Type")
        action_summary.setAlignment(Qt.AlignCenter)
        action_layout.addWidget(action_summary)
        action_group.setLayout(action_layout)
        layout.addWidget(action_group)

        widget.setLayout(layout)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CharacterSheet()
    sys.exit(app.exec())
