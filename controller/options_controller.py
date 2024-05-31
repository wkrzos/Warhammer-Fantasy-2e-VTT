from PySide6.QtCore import QCoreApplication

class OptionsController:
    def __init__(self, model, view, main_controller):
        self.model = model
        self.view = view
        self.connect_signals()
        self.main_controller = main_controller

    def connect_signals(self):
        self.view.exit_button.clicked.connect(self.exit_application)
        self.view.language_selector.currentTextChanged.connect(self.change_language)

    def set_option(self, key, value):
        self.model.set_option(key, value)
        self.view.update_option_list(self.model.get_all_options())

    def change_language(self, language):
        self.model.set_language(language)
        self.main_controller.load_backend_localisation()
        self.update_language()

    def update_language(self):
        language = self.model.get_language()
        translator = QCoreApplication.instance().translator()
        if translator:
            QCoreApplication.instance().removeTranslator(translator)

        translator = QTranslator()
        ts_file = f"translations/{language}.qm"
        if translator.load(ts_file):
            QCoreApplication.instance().installTranslator(translator)
        else:
            print(f"Failed to load language file: {ts_file}")

        # Update UI with new language
        self.view.initUI()

    def exit_application(self):
        # Logic to exit the application
        import sys
        sys.exit()
