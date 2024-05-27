import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QComboBox, QLabel, QGridLayout, QGroupBox, QHBoxLayout, QPushButton, QFileDialog)
from PySide6.QtGui import QFont, QIcon, QPixmap
from PySide6.QtCore import Qt, QSize, QTranslator, QLocale
from frontend.util.font import DEFAULT_FONT, HEADING_FONT, SUBHEADING_FONT

class CharacterSheet(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 1000)
        self.setWindowTitle(self.tr('Warhammer Fantasy Roleplay Character Sheet'))

        widget = QWidget()
        self.setCentralWidget(widget)

        layout = QVBoxLayout()

        # Character Section
        character_group = QGroupBox(self.tr("Character"))
        character_group.setFont(HEADING_FONT)
        character_layout = QHBoxLayout()

        form_layout = QFormLayout()
        form_layout.addRow(self.tr('Name:'), QLineEdit())
        race_combo = QComboBox()
        race_combo.setFont(DEFAULT_FONT)
        race_combo.addItems([self.tr('Human'), self.tr('Elf'), self.tr('Dwarf'), self.tr('Halfling')])
        form_layout.addRow(self.tr('Race:'), race_combo)
        form_layout.addRow(self.tr('Current Career:'), QLineEdit())
        form_layout.addRow(self.tr('Previous Careers:'), QLineEdit())

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
        personal_group = QGroupBox(self.tr("Personal Details"))
        personal_group.setFont(HEADING_FONT)
        personal_layout = QFormLayout()
        personal_layout.addRow(self.tr('Age:'), QLineEdit())
        personal_layout.addRow(self.tr('Gender:'), QLineEdit())
        personal_layout.addRow(self.tr('Height:'), QLineEdit())
        personal_layout.addRow(self.tr('Weight:'), QLineEdit())
        personal_layout.addRow(self.tr('Eyes Color:'), QLineEdit())
        personal_layout.addRow(self.tr('Hair Color:'), QLineEdit())
        personal_layout.addRow(self.tr('Star Sign:'), QLineEdit())
        personal_layout.addRow(self.tr('Number of Siblings:'), QLineEdit())
        personal_layout.addRow(self.tr('Birthplace:'), QLineEdit())
        personal_layout.addRow(self.tr('Distinguishing Marks:'), QLineEdit())
        personal_group.setLayout(personal_layout)
        layout.addWidget(personal_group)

        # Character Profile Main Section
        profile_group = QGroupBox(self.tr("Character Profile Main"))
        profile_group.setFont(HEADING_FONT)
        profile_layout = QGridLayout()
        stats = ['WS', 'BS', 'S', 'T', 'Ag', 'Int', 'WP', 'Fel']
        for i, stat in enumerate(stats):
            label = QLabel(self.tr(stat))
            label.setFont(SUBHEADING_FONT)
            profile_layout.addWidget(label, 0, i + 1)
        for i in range(3):  # 3 rows for Starting, Advance, Current
            for j in range(8):  # 8 stats columns
                line_edit = QLineEdit()
                line_edit.setFont(DEFAULT_FONT)
                profile_layout.addWidget(line_edit, i + 1, j + 1)
        profile_group.setLayout(profile_layout)
        layout.addWidget(profile_group)
        
        # Character Profile Secondary Section
        profile_group_secondary = QGroupBox(self.tr("Character Profile Secondary"))
        profile_group_secondary.setFont(HEADING_FONT)
        profile_layout_secondary = QGridLayout()
        stats_secondary = ['A', 'W', 'SB', 'TB', 'M', 'Mag', 'IP', 'FP']
        for i, stat in enumerate(stats_secondary):
            label = QLabel(self.tr(stat))
            label.setFont(SUBHEADING_FONT)
            profile_layout_secondary.addWidget(label, 0, i + 1)
        for i in range(3):  # 3 rows for Starting, Advance, Current
            for j in range(8):  # 8 stats columns
                line_edit = QLineEdit()
                line_edit.setFont(DEFAULT_FONT)
                profile_layout_secondary.addWidget(line_edit, i + 1, j + 1)
        profile_group_secondary.setLayout(profile_layout_secondary)
        layout.addWidget(profile_group_secondary)
        
        # Weapons Section
        weapons_group = QGroupBox(self.tr("Weapons"))
        weapons_group.setFont(HEADING_FONT)
        weapons_layout = QGridLayout()
        weapons_headers = ['Name', 'Enc', 'Group', 'Damage', 'Range', 'Reload', 'Qualities']
        for i, header in enumerate(weapons_headers):
            label = QLabel(self.tr(header))
            label.setFont(SUBHEADING_FONT)
            weapons_layout.addWidget(label, 0, i)
        for i in range(5):  # 5 rows for weapon entries
            for j in range(len(weapons_headers)):
                line_edit = QLineEdit()
                line_edit.setFont(DEFAULT_FONT)
                weapons_layout.addWidget(line_edit, i + 1, j)
        weapons_group.setLayout(weapons_layout)
        layout.addWidget(weapons_group)

        # Armour, Experience Points and Combat Movement Sections Side by Side
        armour_exp_layout = QHBoxLayout()

        # Armour Section
        armour_group = QGroupBox(self.tr("Armour"))
        armour_group.setFont(HEADING_FONT)
        armour_layout = QFormLayout()
        armour_layout.addRow(self.tr('Basic Armour:'), QLineEdit())
        armour_layout.addRow(self.tr('Advanced Armour:'), QLineEdit())
        armour_group.setLayout(armour_layout)
        armour_exp_layout.addWidget(armour_group)

        # Experience Points Section
        exp_group = QGroupBox(self.tr("Experience Points"))
        exp_group.setFont(HEADING_FONT)
        exp_layout = QFormLayout()
        exp_layout.addRow(self.tr('Current:'), QLineEdit())
        exp_layout.addRow(self.tr('Total:'), QLineEdit())
        exp_group.setLayout(exp_layout)
        armour_exp_layout.addWidget(exp_group)

        layout.addLayout(armour_exp_layout)

        # Combat Movement Section
        combat_group = QGroupBox(self.tr("Combat Movement"))
        combat_group.setFont(HEADING_FONT)
        combat_layout = QFormLayout()
        combat_layout.addRow(self.tr('Move/Disengage:'), QLineEdit())
        combat_layout.addRow(self.tr('Charge Attack:'), QLineEdit())
        combat_layout.addRow(self.tr('Run:'), QLineEdit())
        combat_group.setLayout(combat_layout)
        armour_exp_layout.addWidget(combat_group)

        widget.setLayout(layout)
        self.show()

    def choose_image(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, self.tr("Choose Character Image"), "", self.tr("Image Files (*.png *.jpg *.bmp)"))
        if file_path:
            self.character_icon_button.setIcon(QIcon(file_path))
            self.character_icon_button.setIconSize(QSize(100, 100))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Load translations
    translator = QTranslator()
    locale = QLocale.system().name()
    translation_file = f"translations_{locale}.qm"
    if translator.load(translation_file):
        app.installTranslator(translator)

    ex = CharacterSheet()
    sys.exit(app.exec())
