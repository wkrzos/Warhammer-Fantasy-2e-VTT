class CreaturesController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.connect_signals()

    def connect_signals(self):
        self.view.add_button.clicked.connect(self.add_creature)

    def add_creature(self):
        # Logic to add a creature
        creature_name = "New Creature"
        self.model.add_creature(creature_name)
        self.view.update_creature_list(self.model.get_creatures())
