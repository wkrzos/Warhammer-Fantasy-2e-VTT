import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QComboBox, QLabel, QGridLayout, QGroupBox, QHBoxLayout, QPushButton, QFileDialog)
from PySide6.QtGui import QFont, QIcon, QPixmap
from PySide6.QtCore import Qt, QSize, QTranslator, QLocale

from backend.character_sheets.sheets import Character, Statistics, Development, Attributes, Equipment, Races, CharacterDescription
from frontend.util.font import HEADING_FONT, SUBHEADING_FONT, DEFAULT_FONT

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

        self.form_layout = QFormLayout()
        self.name_input = QLineEdit()
        self.form_layout.addRow(self.tr('Name:'), self.name_input)
        self.race_combo = QComboBox()
        self.race_combo.setFont(DEFAULT_FONT)
        self.race_combo.addItems([self.tr('Human'), self.tr('Elf'), self.tr('Dwarf'), self.tr('Halfling')])
        self.form_layout.addRow(self.tr('Race:'), self.race_combo)
        self.current_career_input = QLineEdit()
        self.form_layout.addRow(self.tr('Current Career:'), self.current_career_input)
        self.previous_careers_input = QLineEdit()
        self.form_layout.addRow(self.tr('Previous Careers:'), self.previous_careers_input)

        character_layout.addLayout(self.form_layout)

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
        self.personal_layout = QFormLayout()
        self.age_input = QLineEdit()
        self.personal_layout.addRow(self.tr('Age:'), self.age_input)
        self.gender_input = QLineEdit()
        self.personal_layout.addRow(self.tr('Gender:'), self.gender_input)
        self.height_input = QLineEdit()
        self.personal_layout.addRow(self.tr('Height:'), self.height_input)
        self.weight_input = QLineEdit()
        self.personal_layout.addRow(self.tr('Weight:'), self.weight_input)
        self.eyes_color_input = QLineEdit()
        self.personal_layout.addRow(self.tr('Eyes Color:'), self.eyes_color_input)
        self.hair_color_input = QLineEdit()
        self.personal_layout.addRow(self.tr('Hair Color:'), self.hair_color_input)
        self.star_sign_input = QLineEdit()
        self.personal_layout.addRow(self.tr('Star Sign:'), self.star_sign_input)
        self.siblings_input = QLineEdit()
        self.personal_layout.addRow(self.tr('Number of Siblings:'), self.siblings_input)
        self.birthplace_input = QLineEdit()
        self.personal_layout.addRow(self.tr('Birthplace:'), self.birthplace_input)
        self.distinguishing_marks_input = QLineEdit()
        self.personal_layout.addRow(self.tr('Distinguishing Marks:'), self.distinguishing_marks_input)
        personal_group.setLayout(self.personal_layout)
        layout.addWidget(personal_group)

        # Character Profile Main Section
        profile_group = QGroupBox(self.tr("Character Profile Main"))
        profile_group.setFont(HEADING_FONT)
        self.profile_layout = QGridLayout()
        stats = ['WS', 'BS', 'S', 'T', 'Ag', 'Int', 'WP', 'Fel']
        self.main_stats_inputs = {}
        for i, stat in enumerate(stats):
            label = QLabel(self.tr(stat))
            label.setFont(SUBHEADING_FONT)
            self.profile_layout.addWidget(label, 0, i + 1)
            self.main_stats_inputs[stat] = []
            for j in range(3):  # 3 rows for Starting, Advance, Current
                line_edit = QLineEdit()
                line_edit.setFont(DEFAULT_FONT)
                self.profile_layout.addWidget(line_edit, j + 1, i + 1)
                self.main_stats_inputs[stat].append(line_edit)
        profile_group.setLayout(self.profile_layout)
        layout.addWidget(profile_group)
        
        # Character Profile Secondary Section
        profile_group_secondary = QGroupBox(self.tr("Character Profile Secondary"))
        profile_group_secondary.setFont(HEADING_FONT)
        self.profile_layout_secondary = QGridLayout()
        stats_secondary = ['A', 'W', 'SB', 'TB', 'M', 'Mag', 'IP', 'FP']
        self.secondary_stats_inputs = {}
        for i, stat in enumerate(stats_secondary):
            label = QLabel(self.tr(stat))
            label.setFont(SUBHEADING_FONT)
            self.profile_layout_secondary.addWidget(label, 0, i + 1)
            self.secondary_stats_inputs[stat] = []
            for j in range(3):  # 3 rows for Starting, Advance, Current
                line_edit = QLineEdit()
                line_edit.setFont(DEFAULT_FONT)
                self.profile_layout_secondary.addWidget(line_edit, j + 1, i + 1)
                self.secondary_stats_inputs[stat].append(line_edit)
        profile_group_secondary.setLayout(self.profile_layout_secondary)
        layout.addWidget(profile_group_secondary)
        
        # Weapons Section
        weapons_group = QGroupBox(self.tr("Weapons"))
        weapons_group.setFont(HEADING_FONT)
        self.weapons_layout = QGridLayout()
        weapons_headers = ['Name', 'Enc', 'Group', 'Damage', 'Range', 'Reload', 'Qualities']
        self.weapon_inputs = []
        for i, header in enumerate(weapons_headers):
            label = QLabel(self.tr(header))
            label.setFont(SUBHEADING_FONT)
            self.weapons_layout.addWidget(label, 0, i)
        for i in range(5):  # 5 rows for weapon entries
            row_inputs = []
            for j in range(len(weapons_headers)):
                line_edit = QLineEdit()
                line_edit.setFont(DEFAULT_FONT)
                self.weapons_layout.addWidget(line_edit, i + 1, j)
                row_inputs.append(line_edit)
            self.weapon_inputs.append(row_inputs)
        weapons_group.setLayout(self.weapons_layout)
        layout.addWidget(weapons_group)

        # Armour, Experience Points and Combat Movement Sections Side by Side
        armour_exp_layout = QHBoxLayout()

        # Armour Section
        armour_group = QGroupBox(self.tr("Armour"))
        armour_group.setFont(HEADING_FONT)
        self.armour_layout = QFormLayout()
        self.basic_armour_input = QLineEdit()
        self.armour_layout.addRow(self.tr('Basic Armour:'), self.basic_armour_input)
        self.advanced_armour_input = QLineEdit()
        self.armour_layout.addRow(self.tr('Advanced Armour:'), self.advanced_armour_input)
        armour_group.setLayout(self.armour_layout)
        armour_exp_layout.addWidget(armour_group)

        # Experience Points Section
        exp_group = QGroupBox(self.tr("Experience Points"))
        exp_group.setFont(HEADING_FONT)
        self.exp_layout = QFormLayout()
        self.current_exp_input = QLineEdit()
        self.exp_layout.addRow(self.tr('Current:'), self.current_exp_input)
        self.total_exp_input = QLineEdit()
        self.exp_layout.addRow(self.tr('Total:'), self.total_exp_input)
        exp_group.setLayout(self.exp_layout)
        armour_exp_layout.addWidget(exp_group)

        layout.addLayout(armour_exp_layout)

        # Combat Movement Section
        combat_group = QGroupBox(self.tr("Combat Movement"))
        combat_group.setFont(HEADING_FONT)
        self.combat_layout = QFormLayout()
        self.move_input = QLineEdit()
        self.combat_layout.addRow(self.tr('Move/Disengage:'), self.move_input)
        self.charge_attack_input = QLineEdit()
        self.combat_layout.addRow(self.tr('Charge Attack:'), self.charge_attack_input)
        self.run_input = QLineEdit()
        self.combat_layout.addRow(self.tr('Run:'), self.run_input)
        combat_group.setLayout(self.combat_layout)
        armour_exp_layout.addWidget(combat_group)

        # Save Button
        self.save_button = QPushButton(self.tr("Save Character"))
        self.save_button.setFont(DEFAULT_FONT)
        self.save_button.clicked.connect(self.save_character)
        layout.addWidget(self.save_button)

        widget.setLayout(layout)
        self.show()

    def choose_image(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, self.tr("Choose Character Image"), "", self.tr("Image Files (*.png *.jpg *.bmp)"))
        if file_path:
            self.character_icon_button.setIcon(QIcon(file_path))
            self.character_icon_button.setIconSize(QSize(100, 100))
            self.character_image_path = file_path

    def save_character(self):
        name = self.name_input.text()
        race = Races(self.race_combo.currentIndex())
        current_career = self.current_career_input.text()
        previous_careers = self.previous_careers_input.text()

        age = int(self.age_input.text())
        gender = self.gender_input.text()
        height = int(self.height_input.text())
        weight = int(self.weight_input.text())
        eyes_color = self.eyes_color_input.text()
        hair_color = self.hair_color_input.text()
        star_sign = self.star_sign_input.text()
        siblings = int(self.siblings_input.text())
        birthplace = self.birthplace_input.text()
        distinguishing_marks = self.distinguishing_marks_input.text()

        character_description = CharacterDescription(
            colorOfEyes=eyes_color,
            colorOfHairs=hair_color,
            weight=weight,
            height=height,
            sex=gender,
            age=age,
            starSign=star_sign,
            birthplace=birthplace,
            distenguishingMarks=distinguishing_marks,
            previousProfession=previous_careers,
            currentProfession=current_career
        )

        statistics = Statistics(
            weaponSkill=int(self.main_stats_inputs['WS'][0].text()),
            ballisticSkill=int(self.main_stats_inputs['BS'][0].text()),
            strength=int(self.main_stats_inputs['S'][0].text()),
            toughness=int(self.main_stats_inputs['T'][0].text()),
            agility=int(self.main_stats_inputs['Ag'][0].text()),
            intelligence=int(self.main_stats_inputs['Int'][0].text()),
            willPower=int(self.main_stats_inputs['WP'][0].text()),
            fellowship=int(self.main_stats_inputs['Fel'][0].text()),
            wounds=int(self.secondary_stats_inputs['W'][0].text()),
            strengthBonus=int(self.secondary_stats_inputs['SB'][0].text()),
            toughnessBonus=int(self.secondary_stats_inputs['TB'][0].text()),
            movement=int(self.secondary_stats_inputs['M'][0].text()),
            magic=int(self.secondary_stats_inputs['Mag'][0].text()),
            insanityPoints=int(self.secondary_stats_inputs['IP'][0].text()),
            fatePoints=int(self.secondary_stats_inputs['FP'][0].text()),
            attacks=int(self.secondary_stats_inputs['A'][0].text())
        )

        character = Character(
            name=name,
            race=race,
            statistics=statistics,
            description=character_description,
        )

        print(character.__dict__())

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
