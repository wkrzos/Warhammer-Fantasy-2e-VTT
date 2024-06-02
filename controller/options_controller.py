from PySide6.QtCore import QCoreApplication, QTranslator

class OptionsController:
    def __init__(self, model, view, main_controller):
        self.model = model
        self.view = view
        self.main_controller = main_controller
        self.translator = QTranslator()
        self.connect_signals()

    def connect_signals(self):
        self.view.exit_button.clicked.connect(self.exit_application)

    def set_option(self, key, value):
        self.model.set_option(key, value)
        self.view.update_option_list(self.model.get_all_options())

    def change_language(self, language):
        self.main_controller.load_backend_localisation()

    def exit_application(self):
        # Logic to exit the application
        import sys
        sys.exit()
