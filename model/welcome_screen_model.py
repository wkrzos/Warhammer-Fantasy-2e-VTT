class WelcomeScreenModel:
    def __init__(self):
        self.language = "en"  # Default language

    def set_language(self, language_code):
        self.language = language_code

    def get_language(self):
        return self.language
