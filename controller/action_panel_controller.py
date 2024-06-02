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
                (self.tr("Parry"), lambda: SelfAction.parry(token)),
                (self.tr("Aiming"), lambda: SelfAction.aiming(token)),
                (self.tr("Wake Up"), lambda: SelfAction.wakeUp(token)),
                (self.tr("Defense Stand"), lambda: SelfAction.defenseStand(token)),
                (self.tr("Use Talent"), lambda: SelfAction.useTalent(token))
            ])

        if len(tokens) == 2:
            player, other = tokens
            actions.extend([
                (self.tr("Simple Attack"), lambda: ActionOnAnother.simpleAtack(player, other)),
                (self.tr("Multiple Attack"), lambda: ActionOnAnother.multipleAtack(player, other)),
                (self.tr("Furious Attack"), lambda: ActionOnAnother.furiousAtack(player, other)),
                (self.tr("Careful Attack"), lambda: ActionOnAnother.carefullAtack(player, other)),
                (self.tr("Push"), lambda: ActionOnAnother.push(player, other)),
                (self.tr("Feint"), lambda: ActionOnAnother.feint(player, other))
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
