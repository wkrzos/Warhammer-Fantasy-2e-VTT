from backend.mechanics.rolling_machine import RollGod

class ChatController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.connect_signals()
        RollGod.attach(self)

    def connect_signals(self):
        self.view.send_button.clicked.connect(self.handle_send_message)

    def handle_send_message(self):
        nickname = self.view.nickname_input.text().strip()
        if not nickname:
            self.view.nickname_input.setFocus()
            return
        message = self.view.input_field.text().strip()
        if message:
            if message.startswith('/roll'):
                self.handle_roll_command(nickname, message)
            else:
                self.add_message(nickname, message)
            self.view.input_field.clear()

    def handle_roll_command(self, nickname, message):
        parts = message.split()
        if len(parts) == 2:
            try:
                dice_type = parts[1].lower()
                if dice_type == 'd4':
                    result = RollGod.rollD4()
                elif dice_type == 'd6':
                    result = RollGod.rollD6()
                elif dice_type == 'd8':
                    result = RollGod.rollD8()
                elif dice_type == 'd10':
                    result = RollGod.rollD10()
                elif dice_type == 'd12':
                    result = RollGod.rollD12()
                elif dice_type == 'd20':
                    result = RollGod.rollD20()
                elif dice_type == 'd100':
                    result = RollGod.rollD100()
                else:
                    result = ["Invalid dice type."]
                self.add_message(nickname, f"Roll {dice_type}: {result}")
            except ValueError:
                self.add_message(nickname, "Invalid roll command format.")
        else:
            self.add_message(nickname, "Usage: /roll [d4|d6|d8|d10|d12|d20|d100]")

    def add_message(self, nickname, message):
        self.model.add_message(nickname, message)
        self.view.update_chat(self.model.get_messages())

    # Can be used to react to signals from the RollGod || Example: self.reactForNotify(signal). May be removed, causes the additional System[<roll outcome>] message.
    def reactForNotify(self, signal):
        result, description = signal
        self.add_message("System", f"{description}: {result}")
