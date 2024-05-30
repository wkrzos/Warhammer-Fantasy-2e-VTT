class ChatModel:
    def __init__(self):
        self.messages = []

    def add_message(self, nickname, message):
        self.messages.append(f"{nickname}: {message}")

    def get_messages(self):
        return self.messages
