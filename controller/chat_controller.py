class ChatController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_message(self, message):
        self.model.add_message(message)
        self.view.update_chat(self.model.get_messages())
