import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QComboBox, QLabel, QGridLayout, QGroupBox, QHBoxLayout, QPushButton, QFileDialog)
from PySide6.QtGui import QFont, QIcon, QPixmap
from PySide6.QtCore import Qt, QSize

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
        character_layout = QHBoxLayout()

        form_layout = QFormLayout()
        form_layout.addRow('Name:', QLineEdit())
        race_combo = QComboBox()
        race_combo.addItems(['Human', 'Elf', 'Dwarf', 'Halfling'])
        form_layout.addRow('Race:', race_combo)
        form_layout.addRow('Current Career:', QLineEdit())
        form_layout.addRow('Previous Careers:', QLineEdit())

        character_layout.addLayout(form_layout)

        # Character icon button
        self.character_icon_button = QPushButton()
        self.character_icon_button.setIcon(QIcon("frontend/resources/icons/default_user.png"))
        self.character_icon_button.setIconSize(QSize(100, 100))
        self.character_icon_button.setFixedSize(120, 120)
        self.character_icon_button.clicked.connect(self.choose_image)

        character_layout.addWidget(self.character_icon_button)
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

        # Character Profile Main Section
        profile_group = QGroupBox("Character Profile Main")
        profile_layout = QGridLayout()
        stats = ['WS', 'BS', 'S', 'T', 'Ag', 'Int', 'WP', 'Fel']
        for i, stat in enumerate(stats):
            profile_layout.addWidget(QLabel(stat), 0, i + 1)
        for i in range(3):  # 3 rows for Starting, Advance, Current
            for j in range(8):  # 8 stats columns
                profile_layout.addWidget(QLineEdit(), i + 1, j + 1)
        profile_group.setLayout(profile_layout)
        layout.addWidget(profile_group)
        
        # Character Profile Secondary Section
        profile_group_secondary = QGroupBox("Character Profile Secondary")
        profile_layout_secondary = QGridLayout()
        stats_secondary = ['A', 'W', 'SB', 'TB', 'M', 'Mag', 'IP', 'FP']
        for i, stat in enumerate(stats_secondary):
            profile_layout_secondary.addWidget(QLabel(stat), 0, i + 1)
        for i in range(3):  # 3 rows for Starting, Advance, Current
            for j in range(8):  # 8 stats columns
                profile_layout_secondary.addWidget(QLineEdit(), i + 1, j + 1)
        profile_group_secondary.setLayout(profile_layout_secondary)
        layout.addWidget(profile_group_secondary)
        
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

        # Armour, Experience Points and Combat Movement Sections Side by Side
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
        exp_layout.addRow('Current:', QLineEdit())
        exp_layout.addRow('Total:', QLineEdit())
        exp_group.setLayout(exp_layout)
        armour_exp_layout.addWidget(exp_group)

        layout.addLayout(armour_exp_layout)

        # Combat Movement Section
        combat_group = QGroupBox("Combat Movement")
        combat_layout = QFormLayout()
        combat_layout.addRow('Move/Disengage:', QLineEdit())
        combat_layout.addRow('Charge Attack:', QLineEdit())
        combat_layout.addRow('Run:', QLineEdit())
        combat_group.setLayout(combat_layout)
        armour_exp_layout.addWidget(combat_group)

        """
        # Action Summary Section, optional in the future
        action_group = QGroupBox("Action Summary")
        action_layout = QVBoxLayout()
        action_summary = QLabel("Basic Action | Type | Advanced Action | Type")
        action_summary.setAlignment(Qt.AlignCenter)
        action_layout.addWidget(action_summary)
        action_group.setLayout(action_layout)
        layout.addWidget(action_group)
        """

        widget.setLayout(layout)
        self.show()

    def choose_image(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Choose Character Image", "", "Image Files (*.png *.jpg *.bmp)")
        if file_path:
            self.character_icon_button.setIcon(QIcon(file_path))
            self.character_icon_button.setIconSize(QSize(100, 100))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CharacterSheet()
    sys.exit(app.exec())
