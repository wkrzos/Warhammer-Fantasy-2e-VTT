class OptionsModel:
    def __init__(self):
        self.options = {}

    def set_option(self, key, value):
        self.options[key] = value

    def get_option(self, key):
        return self.options.get(key)

    def get_all_options(self):
        return self.options
