from PySide6.QtCore import QCoreApplication, QTranslator

class OptionsController:
    def __init__(self, model, view, main_controller):
        self.model = model
        self.view = view
        self.main_controller = main_controller
        self.translator = QTranslator()
        self.connect_signals()
        self.update_language(self.model.get_language())  # Load the initial language

    def connect_signals(self):
        self.view.exit_button.clicked.connect(self.exit_application)
        self.view.languageChanged.connect(self.change_language)

    def set_option(self, key, value):
        self.model.set_option(key, value)
        self.view.update_option_list(self.model.get_all_options())

    def change_language(self, language):
        self.model.set_language(language)
        self.main_controller.load_backend_localisation()
        self.update_language(language)

    def update_language(self, language):
        ts_file = f"translations/{language}.qm"
        if self.translator.load(ts_file):
            QCoreApplication.instance().installTranslator(self.translator)
            self.view.initUI()  # Update UI with new language
        else:
            print(f"Failed to load language file: {ts_file}")

    def exit_application(self):
        # Logic to exit the application
        import sys
        sys.exit()
