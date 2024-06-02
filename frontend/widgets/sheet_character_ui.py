import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QComboBox, QLabel, QGridLayout, QGroupBox, QHBoxLayout, QPushButton, QFileDialog, QMessageBox)
from PySide6.QtGui import QFont, QIcon, QPixmap
from PySide6.QtCore import Qt, QSize, QTranslator, QLocale

from backend.character_sheets.sheets import Character, Statistics, Development, Attributes, Equipment, Races, CharacterDescription, Card
from frontend.util.font import HEADING_FONT, SUBHEADING_FONT, DEFAULT_FONT
from backend.json_serialisation.save_manager import SaveManager
from translations.gui_translator import GuiTranslator
from backend.character_sheets.characteristics import MainStats, SecondaryStats

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
        self.setup_character_section(layout)
        self.setup_personal_details_section(layout)
        self.setup_character_profile_main(layout)
        self.setup_character_profile_secondary(layout)
        self.setup_weapons_section(layout)
        self.setup_armour_exp_combat(layout)

        self.save_button = QPushButton(self.tr("Save Character"))
        self.save_button.setFont(DEFAULT_FONT)
        self.save_button.clicked.connect(self.save_character)
        layout.addWidget(self.save_button)

        widget.setLayout(layout)
        self.show()

    def setup_character_section(self, layout):
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

        self.character_icon_button = QPushButton()
        self.character_icon_button.setIcon(QIcon("frontend/resources/icons/default_user.png"))
        self.character_icon_button.setIconSize(QSize(100, 100))
        self.character_icon_button.setFixedSize(120, 120)
        self.character_icon_button.clicked.connect(self.choose_image)

        character_layout.addWidget(self.character_icon_button)
        character_group.setLayout(character_layout)
        layout.addWidget(character_group)

    def setup_personal_details_section(self, layout):
        personal_group = QGroupBox(self.tr("Personal Details"))
        personal_group.setFont(HEADING_FONT)
        self.personal_layout = QFormLayout()
        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Required")
        self.personal_layout.addRow(self.tr('Age:'), self.age_input)
        self.gender_input = QLineEdit()
        self.personal_layout.addRow(self.tr('Gender:'), self.gender_input)
        self.height_input = QLineEdit()
        self.height_input.setPlaceholderText("Required")
        self.personal_layout.addRow(self.tr('Height:'), self.height_input)
        self.weight_input = QLineEdit()
        self.weight_input.setPlaceholderText("Required")
        self.personal_layout.addRow(self.tr('Weight:'), self.weight_input)
        self.eyes_color_input = QLineEdit()
        self.personal_layout.addRow(self.tr('Eyes Color:'), self.eyes_color_input)
        self.hair_color_input = QLineEdit()
        self.personal_layout.addRow(self.tr('Hair Color:'), self.hair_color_input)
        self.star_sign_input = QLineEdit()
        self.personal_layout.addRow(self.tr('Star Sign:'), self.star_sign_input)
        self.siblings_input = QLineEdit()
        self.siblings_input.setPlaceholderText("Required")
        self.personal_layout.addRow(self.tr('Number of Siblings:'), self.siblings_input)
        self.birthplace_input = QLineEdit()
        self.personal_layout.addRow(self.tr('Birthplace:'), self.birthplace_input)
        self.distinguishing_marks_input = QLineEdit()
        self.personal_layout.addRow(self.tr('Distinguishing Marks:'), self.distinguishing_marks_input)
        personal_group.setLayout(self.personal_layout)
        layout.addWidget(personal_group)

    def setup_character_profile_main(self, layout):
        profile_group = QGroupBox(self.tr("Character Profile Main"))
        profile_group.setFont(HEADING_FONT)
        self.profile_layout = QGridLayout()
        stats = ['WS', 'BS', 'S', 'T', 'Ag', 'Int', 'WP', 'Fel']
        self.main_stats_inputs = self.setup_stats_inputs(stats, self.profile_layout)
        profile_group.setLayout(self.profile_layout)
        layout.addWidget(profile_group)

    def setup_character_profile_secondary(self, layout):
        profile_group_secondary = QGroupBox(self.tr("Character Profile Secondary"))
        profile_group_secondary.setFont(HEADING_FONT)
        self.profile_layout_secondary = QGridLayout()
        stats_secondary = ['A', 'W', 'SB', 'TB', 'M', 'Mag', 'IP', 'FP']
        self.secondary_stats_inputs = self.setup_secondary_stats_inputs(stats_secondary, self.profile_layout_secondary)
        profile_group_secondary.setLayout(self.profile_layout_secondary)
        layout.addWidget(profile_group_secondary)

    def setup_weapons_section(self, layout):
        weapons_group = QGroupBox(self.tr("Weapons"))
        weapons_group.setFont(HEADING_FONT)
        self.weapons_layout = QGridLayout()
        weapons_headers = ['Name', 'Enc', 'Group', 'Damage', 'Range', 'Reload', 'Qualities']
        self.weapon_inputs = self.setup_grid_inputs(weapons_headers, self.weapons_layout, 5)
        weapons_group.setLayout(self.weapons_layout)
        layout.addWidget(weapons_group)

    def setup_armour_exp_combat(self, layout):
        armour_exp_layout = QHBoxLayout()

        # Armour Section
        armour_group = QGroupBox(self.tr("Armour"))
        armour_group.setFont(HEADING_FONT)
        self.armour_layout = QFormLayout()
        self.basic_armour_input = QLineEdit()
        self.armour_layout.addRow(self.tr('Basic Armour:'), self.basic_armour_input)
        self.advanced_armour_input = QLineEdit()
        self.armour_layout.addRow(self.tr('Advanced Armour:'), self.advanced_armour_input)
        
        # Add maxHP field
        self.max_hp_input = QLineEdit()
        self.max_hp_input.setReadOnly(True)
        self.armour_layout.addRow(self.tr('Max HP:'), self.max_hp_input)
        
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

        # Combat Movement Section
        combat_group = QGroupBox(self.tr("Combat Movement"))
        combat_group.setFont(HEADING_FONT)
        self.combat_layout = QFormLayout()
        
        # Add walk, chargeRange, and runRange
        self.walk_input = QLineEdit()
        self.walk_input.setReadOnly(True)
        self.combat_layout.addRow(self.tr('Walk:'), self.walk_input)
        self.charge_range_input = QLineEdit()
        self.charge_range_input.setReadOnly(True)
        self.combat_layout.addRow(self.tr('Charge Range:'), self.charge_range_input)
        self.run_range_input = QLineEdit()
        self.run_range_input.setReadOnly(True)
        self.combat_layout.addRow(self.tr('Run Range:'), self.run_range_input)
        
        combat_group.setLayout(self.combat_layout)
        armour_exp_layout.addWidget(combat_group)

        layout.addLayout(armour_exp_layout)

    def setup_stats_inputs(self, stats, layout):
        stats_inputs = {}
        for i, stat in enumerate(stats):
            label = QLabel(self.tr(stat))
            label.setFont(SUBHEADING_FONT)
            layout.addWidget(label, 0, i + 1)
            stats_inputs[stat] = []
            for j in range(3):  # 3 rows for Starting, Advance, Current
                line_edit = QLineEdit()
                line_edit.setFont(DEFAULT_FONT)
                if j == 1 or j == 2:  # Make the second and third rows uneditable
                    line_edit.setReadOnly(True)
                layout.addWidget(line_edit, j + 1, i + 1)
                stats_inputs[stat].append(line_edit)
        return stats_inputs

    def setup_secondary_stats_inputs(self, stats, layout):
        stats_inputs = {}
        for i, stat in enumerate(stats):
            label = QLabel(self.tr(stat))
            label.setFont(SUBHEADING_FONT)
            layout.addWidget(label, 0, i + 1)
            stats_inputs[stat] = []
            # Only one row for SB, TB, IP (editable)
            if stat in ['SB', 'TB', 'IP']:
                line_edit = QLineEdit()
                line_edit.setFont(DEFAULT_FONT)
                if stat != 'IP':
                    line_edit.setReadOnly(True)
                layout.addWidget(line_edit, 1, i + 1)
                stats_inputs[stat].append(line_edit)
            else:
                for j in range(3):  # 3 rows for other stats
                    line_edit = QLineEdit()
                    line_edit.setFont(DEFAULT_FONT)
                    if j == 1 or j == 2:  # Make the second and third rows uneditable
                        line_edit.setReadOnly(True)
                    layout.addWidget(line_edit, j + 1, i + 1)
                    stats_inputs[stat].append(line_edit)
        return stats_inputs

    def setup_grid_inputs(self, headers, layout, rows):
        grid_inputs = []
        for i, header in enumerate(headers):
            label = QLabel(self.tr(header))
            label.setFont(SUBHEADING_FONT)
            layout.addWidget(label, 0, i)
        for i in range(rows):  # rows for entries
            row_inputs = []
            for j in range(len(headers)):
                line_edit = QLineEdit()
                line_edit.setFont(DEFAULT_FONT)
                layout.addWidget(line_edit, i + 1, j)
                row_inputs.append(line_edit)
            grid_inputs.append(row_inputs)
        return grid_inputs

    def choose_image(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, self.tr("Choose Character Image"), "", self.tr("Image Files (*.png *.jpg *.bmp)"))
        if file_path:
            self.character_icon_button.setIcon(QIcon(file_path))
            self.character_icon_button.setIconSize(QSize(100, 100))
            self.character_image_path = file_path

    def show_error_message(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.exec()

    def validate_fields(self):
        required_fields = [
            (self.name_input, 'Name'),
            (self.age_input, 'Age'),
            (self.height_input, 'Height'),
            (self.weight_input, 'Weight'),
            (self.siblings_input, 'Number of Siblings'),
        ]
        valid = True
        for field, name in required_fields:
            if not field.text():
                field.setStyleSheet('border: 2px solid red')
                self.show_error_message(f"The field '{name}' is required.")
                valid = False
            else:
                field.setStyleSheet('')
        
        if not hasattr(self, 'character_image_path') or not self.character_image_path:
            self.character_icon_button.setStyleSheet('border: 2px solid red')
            self.show_error_message("The character image is required.")
            valid = False
        else:
            self.character_icon_button.setStyleSheet('')
        
        return valid

    def save_character(self):
        if not self.validate_fields():
            return
        
        name = self.name_input.text()
        race = Races(1)
        current_career = self.current_career_input.text()
        previous_careers = self.previous_careers_input.text()

        try:
            age = int(self.age_input.text())
            height = int(self.height_input.text())
            weight = int(self.weight_input.text())
            siblings = int(self.siblings_input.text())
        except ValueError:
            self.show_error_message("Age, Height, Weight, and Number of Siblings must be integers.")
            return

        gender = self.gender_input.text()
        eyes_color = self.eyes_color_input.text()
        hair_color = self.hair_color_input.text()
        star_sign = self.star_sign_input.text()
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

        try:
            statistics = Statistics(
                ws=int(self.main_stats_inputs['WS'][0].text()),
                bs=int(self.main_stats_inputs['BS'][0].text()),
                s=int(self.main_stats_inputs['S'][0].text()),
                t=int(self.main_stats_inputs['T'][0].text()),
                ag=int(self.main_stats_inputs['Ag'][0].text()),
                int=int(self.main_stats_inputs['Int'][0].text()),
                wp=int(self.main_stats_inputs['WP'][0].text()),
                fel=int(self.main_stats_inputs['Fel'][0].text()),
                w=int(self.secondary_stats_inputs['W'][0].text()),
                m=int(self.secondary_stats_inputs['M'][0].text()),
                magic=int(self.secondary_stats_inputs['Mag'][0].text()),
                ip=int(self.secondary_stats_inputs['IP'][0].text()),  # Modifiable, can't be developed
                fp=int(self.secondary_stats_inputs['FP'][0].text())  # Modifiable, can't be developed
            )
        except ValueError:
            self.show_error_message("Statistics fields must be integers.")
            return

        development = Development()
        try:
            development.exp = int(self.current_exp_input.text())  # Set current experience
        except ValueError:
            self.show_error_message("Current experience must be an integer.")
            return

        character = Character(
            name=name,
            race=race,
            statistics=statistics,
            development=development,
            characterPicture=self.character_image_path
        )

        card = Card(
            playerName=name,
            playerCharacter=character,
            characterDescription=character_description,
            history="History"
        )

        SaveManager.saveCharacterCard(characterCard=card, saveName=name.replace(" ", "_"))
        
        # Update summary statistics
        self.update_summary_statistics(character)
        return card

    def update_summary_statistics(self, character):
        # Main stats summary
        self.main_stats_inputs['WS'][1].setText(str(character.summaryWeaponSkill))
        self.main_stats_inputs['BS'][1].setText(str(character.summaryBalisticSkill))
        self.main_stats_inputs['S'][1].setText(str(character.summaryStrength))
        self.main_stats_inputs['T'][1].setText(str(character.summaryToughness))
        self.main_stats_inputs['Ag'][1].setText(str(character.summaryAgility))
        self.main_stats_inputs['Int'][1].setText(str(character.summaryInteligence))
        self.main_stats_inputs['WP'][1].setText(str(character.summaryWillPower))
        self.main_stats_inputs['Fel'][1].setText(str(character.summaryFellowship))

        # Main stats development
        self.main_stats_inputs['WS'][2].setText(str(character.development.getStatsBonus(MainStats.WEAPON_SKILL)))
        self.main_stats_inputs['BS'][2].setText(str(character.development.getStatsBonus(MainStats.BALLISTIC_SKILL)))
        self.main_stats_inputs['S'][2].setText(str(character.development.getStatsBonus(MainStats.STRENGTH)))
        self.main_stats_inputs['T'][2].setText(str(character.development.getStatsBonus(MainStats.TOUGHNESS)))
        self.main_stats_inputs['Ag'][2].setText(str(character.development.getStatsBonus(MainStats.AGILITY)))
        self.main_stats_inputs['Int'][2].setText(str(character.development.getStatsBonus(MainStats.INTELLIGENCE)))
        self.main_stats_inputs['WP'][2].setText(str(character.development.getStatsBonus(MainStats.WILL_POWER)))
        self.main_stats_inputs['Fel'][2].setText(str(character.development.getStatsBonus(MainStats.FELLOWSHIP)))

        # Secondary stats summary
        self.secondary_stats_inputs['A'][1].setText(str(character.summaryAttacks))
        self.secondary_stats_inputs['W'][1].setText(str(character.summaryHp))
        self.secondary_stats_inputs['SB'][0].setText(str(character.strengthBonus))
        self.secondary_stats_inputs['TB'][0].setText(str(character.toughnessBonus))
        self.secondary_stats_inputs['M'][1].setText(str(character.summaryMovement))
        self.secondary_stats_inputs['Mag'][1].setText(str(character.summaryMagic))
        self.secondary_stats_inputs['IP'][0].setText(str(character.statistics.insanityPoints))
        self.secondary_stats_inputs['FP'][1].setText(str(character.statistics.fatePoint))

        # Secondary stats development
        self.secondary_stats_inputs['A'][2].setText(str(character.development.getStatsBonus(SecondaryStats.ATTACKS)))
        self.secondary_stats_inputs['W'][2].setText(str(character.development.getStatsBonus(SecondaryStats.WOUNDS)))
        self.secondary_stats_inputs['M'][2].setText(str(character.development.getStatsBonus(SecondaryStats.MOVEMENT)))
        self.secondary_stats_inputs['Mag'][2].setText(str(character.development.getStatsBonus(SecondaryStats.MAGIC)))

        # Update combat movement
        self.walk_input.setText(str(character.walk))
        self.charge_range_input.setText(str(character.chargeRange))
        self.run_range_input.setText(str(character.runRange))

        # Update max HP
        self.max_hp_input.setText(str(character.maxHP))

    def load_character(self, character_card: Card = SaveManager.loadCharacterCard("saves/cards/default.json")):
        self.name_input.setText(character_card.playerName)
        self.race_combo.setCurrentIndex(1)
        self.current_career_input.setText(character_card.characterDescription.currentProfession)
        self.previous_careers_input.setText(character_card.characterDescription.previousProfession)
        self.character_icon_button.setIcon(QIcon(character_card.playerCharacter.characterPicture))
        self.character_icon_button.setIconSize(QSize(100, 100))
        ###
        print(character_card.characterDescription.age)
        ###
        self.age_input.setText(str(character_card.characterDescription.age))
        self.gender_input.setText(character_card.characterDescription.sex)
        self.height_input.setText(str(character_card.characterDescription.height))
        self.weight_input.setText(str(character_card.characterDescription.weight))
        self.eyes_color_input.setText(character_card.characterDescription.colorOfEyes)
        self.hair_color_input.setText(character_card.characterDescription.colorOfHairs)
        self.star_sign_input.setText(character_card.characterDescription.starSign)
        self.siblings_input.setText(str(1))
        self.birthplace_input.setText(character_card.characterDescription.birthplace)
        self.distinguishing_marks_input.setText(character_card.characterDescription.distenguishingMarks)

        self.main_stats_inputs['WS'][0].setText(str(character_card.playerCharacter.statistics.weaponSkill))
        self.main_stats_inputs['BS'][0].setText(str(character_card.playerCharacter.statistics.ballisticSkill))
        self.main_stats_inputs['S'][0].setText(str(character_card.playerCharacter.statistics.strength))
        self.main_stats_inputs['T'][0].setText(str(character_card.playerCharacter.statistics.toughness))
        self.main_stats_inputs['Ag'][0].setText(str(character_card.playerCharacter.statistics.agility))
        self.main_stats_inputs['Int'][0].setText(str(character_card.playerCharacter.statistics.intelligence))
        self.main_stats_inputs['WP'][0].setText(str(character_card.playerCharacter.statistics.willPower))
        self.main_stats_inputs['Fel'][0].setText(str(character_card.playerCharacter.statistics.fellowship))
        self.secondary_stats_inputs['W'][0].setText(str(character_card.playerCharacter.statistics.wounds))
        self.secondary_stats_inputs['M'][0].setText(str(character_card.playerCharacter.statistics.movement))
        self.secondary_stats_inputs['Mag'][0].setText(str(character_card.playerCharacter.statistics.magic))
        self.secondary_stats_inputs['IP'][0].setText(str(character_card.playerCharacter.statistics.insanityPoints))
        self.secondary_stats_inputs['FP'][0].setText(str(character_card.playerCharacter.statistics.fatePoint))

        # Update summary statistics
        self.update_summary_statistics(character_card.playerCharacter)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    translator = GuiTranslator.load_translations(app, "pl")
    app.installTranslator(translator)

    ex = CharacterSheet()
    sys.exit(app.exec())
