class ChatController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.connect_signals()

    def connect_signals(self):
        self.view.send_button.clicked.connect(self.handle_send_message)

    def handle_send_message(self):
        nickname = self.view.nickname_input.text().strip()
        if not nickname:
            self.view.nickname_input.setFocus()
            return
        message = self.view.input_field.text().strip()
        if message:
            self.add_message(nickname, message)
            self.view.input_field.clear()

    def add_message(self, nickname, message):
        self.model.add_message(nickname, message)
        self.view.update_chat(self.model.get_messages())
