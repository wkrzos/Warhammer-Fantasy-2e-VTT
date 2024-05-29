from PySide6.QtCore import QObject




class ToolbarController(QObject):
    def __init__(self, model, view, main_window_controller):
        super().__init__()
        self.model = model
        self.view = view
        self.connect_signals()
        self.main_window_controller = main_window_controller

    def connect_signals(self):
        for tool, button in self.view.buttons.items():
            button.clicked.connect(self.create_button_handler(tool))

    def create_button_handler(self, tool):
        def handler():
            self.model.set_selected_tool(tool)
            self.main_window_controller.map_view_controller.set_selected_tool(tool)
            self.view.highlight_button(tool)
        return handler
