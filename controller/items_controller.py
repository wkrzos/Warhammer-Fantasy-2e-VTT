class ItemsController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.connect_signals()

    def connect_signals(self):
        self.view.add_button.clicked.connect(self.add_item)

    def add_item(self):
        # Logic to add an item
        item_name = "New Item"
        self.model.add_item(item_name)
        self.view.update_item_list(self.model.get_items())
