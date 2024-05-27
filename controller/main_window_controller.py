class MainWindowController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.setup_ui(self.model)

        # Connect the toolbar selection signal to the map view controller
        self.view.toolbar_controller.view.tool_selected = self.tool_selected

    def tool_selected(self, tool):
        # Propagate the selected tool to the map view controller
        self.view.map_view_controller.set_selected_tool(tool)
