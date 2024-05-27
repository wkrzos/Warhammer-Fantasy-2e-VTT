from PySide6.QtCore import QObject
from backend.mechanics.actions.actions_implementation import SelfAction, ActionOnAnother, SpecialAction

class ActionPanelController(QObject):
    def __init__(self, model, view):
        super().__init__()
        self.model = model
        self.view = view
        self.connect_signals()

    def connect_signals(self):
        self.view.execute_button.clicked.connect(self.execute_action)

    def update_actions(self, tokens):
        self.view.clear_actions()
        actions = []

        if len(tokens) == 1:
            token = tokens[0]
            actions.extend([
                ("Parry", lambda: SelfAction.parry(token)),
                ("Aiming", lambda: SelfAction.aiming(token)),
                ("Wake Up", lambda: SelfAction.wakeUp(token)),
                ("Defense Stand", lambda: SelfAction.defenseStand(token)),
                ("Use Talent", lambda: SelfAction.useTalent(token))
            ])

        if len(tokens) == 2:
            player, other = tokens
            actions.extend([
                ("Simple Attack", lambda: ActionOnAnother.simpleAtack(player, other)),
                ("Multiple Attack", lambda: ActionOnAnother.multipleAtack(player, other)),
                ("Furious Attack", lambda: ActionOnAnother.furiousAtack(player, other)),
                ("Careful Attack", lambda: ActionOnAnother.carefullAtack(player, other)),
                ("Push", lambda: ActionOnAnother.push(player, other)),
                ("Feint", lambda: ActionOnAnother.feint(player, other))
            ])

        # Set actions in the model
        self.model.set_actions(actions)

        # Add actions to the view
        for name, func in actions:
            self.view.add_action(name, func)

    def execute_action(self):
        action_func = self.view.get_selected_action()
        if action_func:
            action_func()
