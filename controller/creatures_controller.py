import sys
from PySide6.QtWidgets import QApplication
from frontend.widgets.sheet_character_ui import CharacterSheet
from model.creatures_model import CreaturesModel
from frontend.widgets.creatures_ui import CreaturesViewUI

class CreaturesController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.connect_signals()
        self.view.update_creature_list(self.model.get_creatures())

    def connect_signals(self):
        self.view.add_button.clicked.connect(self.add_creature)
        self.view.creature_list.itemDoubleClicked.connect(self.open_character_sheet)

    def add_creature(self):
        # Open character sheet
        self.character_sheet = CharacterSheet()
        self.character_sheet.show()
        self.character_sheet.save_button.clicked.connect(self.save_character)

    def open_character_sheet(self, item):
        creature_name = item.text()
        creature = self.model.get_creature_by_name(creature_name)
        if creature:
            self.character_sheet = CharacterSheet()
            self.character_sheet.load_character(creature)
            self.character_sheet.show()

    def save_character(self):
        # Logic to save the character from the character sheet
        character_data = self.character_sheet.save_character()
        self.model.add_creature(character_data)
        self.view.update_creature_list(self.model.get_creatures())

if __name__ == '__main__':
    app = QApplication(sys.argv)

    model = CreaturesModel()
    view = CreaturesViewUI()
    controller = CreaturesController(model, view)

    view.show()
    sys.exit(app.exec())
