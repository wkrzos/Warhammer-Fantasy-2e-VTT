import sys
from PySide6.QtWidgets import QApplication
from frontend.widgets.sheet_character_ui import CharacterSheet
from model.characters_model import CharactersModel
from frontend.widgets.characters_ui import CharactersViewUI
from backend.mechanics.token import Token
from model.map_model import MapViewModel
from frontend.widgets.map_ui import MapViewUI

class CharactersController:
    def __init__(self, model, view, map_model):
        self.model = model
        self.view = view
        self.map_model = map_model
        self.map_view = MapViewUI()
        self.connect_signals()
        self.view.update_creature_list(self.model.get_characters())

    def connect_signals(self):
        self.view.add_button.clicked.connect(self.add_character)
        self.view.creature_list.itemDoubleClicked.connect(self.open_character_sheet)
        self.view.creature_list.itemClicked.connect(self.select_character)
        self.view.add_token_button.clicked.connect(self.add_character_token)

    def add_character(self):
        # Open character sheet
        self.character_sheet = CharacterSheet()
        self.character_sheet.load_character()
        self.character_sheet.show()
        self.character_sheet.save_button.clicked.connect(self.save_character)

    def open_character_sheet(self, item):
        creature_name = item.text()
        creature = self.model.get_character_by_name(creature_name)
        if creature:
            self.character_sheet = CharacterSheet()
            ###
            print(creature)
            print(creature.__dict__())
            ###
            self.character_sheet.load_character(creature)
            self.character_sheet.show()

    def save_character(self):
        # Logic to save the character from the character sheet
        character_data = self.character_sheet.save_character()
        self.model.add_character(character_data)
        self.view.update_creature_list(self.model.get_characters())

    def select_character(self, item):
        self.selected_character_name = item.text()

    def add_character_token(self):
        character_name = self.selected_character_name
        character = self.model.get_character_by_name(character_name).playerCharacter
        print(character.__dict__())
        if character:
            token = Token(creature=character)
            
            # Calculate the center position
            map_width = self.map_view.width()
            map_height = self.map_view.height()
            center_x = (map_width / 2 - self.map_model.get_offset()[0]) / (self.map_model.grid_size * self.map_model.get_zoom_level())
            center_y = (map_height / 2 - self.map_model.get_offset()[1]) / (self.map_model.grid_size * self.map_model.get_zoom_level())
            token.set_position(center_x, center_y)
            
            self.map_model.tokens.append(token)  # Add token to the map model
            self.view.update_creature_list(self.model.get_characters())
            self.map_model.set_selected_tokens([token])
            self.view.update()  # Update the map view to display the new token

if __name__ == '__main__':
    app = QApplication(sys.argv)

    model = CharactersModel()
    view = CharactersViewUI()
    map_model = MapViewModel()  # Assuming map_model is available
    controller = CharactersController(model, view, map_model)

    view.show()
    sys.exit(app.exec())
