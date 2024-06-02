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
