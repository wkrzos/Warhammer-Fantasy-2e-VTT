import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QListWidget, QListWidgetItem)
from PySide6.QtCore import Qt
from backend.mechanic.actions.actionsImplementation import SelfAction, ActionOnAnother, SpecialAction
from frontend.widgets.mapview import MapView
from frontend.widgets.toolbar import Toolbar

class ActionPanel(QWidget):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Actions")
        layout.addWidget(self.label)

        self.action_list = QListWidget()
        layout.addWidget(self.action_list)

        self.execute_button = QPushButton("Execute Action")
        self.execute_button.clicked.connect(self.execute_action)
        layout.addWidget(self.execute_button)

        self.setLayout(layout)

    def update_actions(self, tokens):
        self.action_list.clear()

        if len(tokens) == 1:
            token = tokens[0]
            self.add_action("Parry", lambda: SelfAction.parry(token))
            self.add_action("Aiming", lambda: SelfAction.aiming(token))
            self.add_action("Wake Up", lambda: SelfAction.wakeUp(token))
            self.add_action("Defense Stand", lambda: SelfAction.defenseStand(token))
            self.add_action("Use Talent", lambda: SelfAction.useTalent(token))

        if len(tokens) == 2:
            player, other = tokens
            self.add_action("Simple Attack", lambda: ActionOnAnother.simpleAtack(player, other))
            self.add_action("Multiple Attack", lambda: ActionOnAnother.multipleAtack(player, other))
            self.add_action("Furious Attack", lambda: ActionOnAnother.furiousAtack(player, other))
            self.add_action("Careful Attack", lambda: ActionOnAnother.carefullAtack(player, other))
            self.add_action("Push", lambda: ActionOnAnother.push(player, other))
            self.add_action("Feint", lambda: ActionOnAnother.feint(player, other))

        # Add more conditions and actions as needed

    def add_action(self, name, func):
        item = QListWidgetItem(name)
        item.setData(Qt.UserRole, func)
        self.action_list.addItem(item)

    def execute_action(self):
        selected_items = self.action_list.selectedItems()
        if selected_items:
            action_func = selected_items[0].data(Qt.UserRole)
            action_func()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    action_panel = ActionPanel(main_window)
    main_window.setCentralWidget(action_panel)
    main_window.show()
    sys.exit(app.exec())
