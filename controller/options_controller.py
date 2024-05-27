class OptionsController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.connect_signals()

    def connect_signals(self):
        self.view.exit_button.clicked.connect(self.exit_application)

    def set_option(self, key, value):
        self.model.set_option(key, value)
        self.view.update_option_list(self.model.get_all_options())

    def exit_application(self):
        # Logic to exit the application
        import sys
        sys.exit()
