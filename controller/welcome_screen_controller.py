from localisation.actionsText import ActionsTextAggregator
from localisation.characteristics import CharacterTextAggregator
from localisation.descriptions import RollDescriptionAggregator
from localisation.itemsText import ItemsTextAggregator


class WelcomeScreenController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.connect_signals()


    def connect_signals(self):
        self.view.language_combo.currentTextChanged.connect(self.update_language)

    def update_language(self, language):
        language_code = "en"
        if language == "English":
            language_code = "en"
        elif language == "Polish":
            language_code = "pl"
        elif language == "German":
            language_code = "de"
        self.model.set_language(language_code)
        self.load_backend_localisation()

    def load_backend_localisation(self):
        RollDescriptionAggregator.loadtestDescriptions(self.model.get_language())
        RollDescriptionAggregator.loadFigthDescriptions(self.model.get_language())
        CharacterTextAggregator.load_races_names(self.model.get_language())
        CharacterTextAggregator.load_stats_names(self.model.get_language())
        CharacterTextAggregator.load_skills_names(self.model.get_language())
        CharacterTextAggregator.load_attributes_names(self.model.get_language())
        ItemsTextAggregator.load_weapon_types_names(self.model.get_language())
        ItemsTextAggregator.load_armor_types_names(self.model.get_language())
        ItemsTextAggregator.load_weapon_trait_names(self.model.get_language())
        ItemsTextAggregator.load_hit_localisation_names(self.model.get_language())
        ActionsTextAggregator.load_double_actions(self.model.get_language())
        ActionsTextAggregator.load_basic_actions(self.model.get_language())
