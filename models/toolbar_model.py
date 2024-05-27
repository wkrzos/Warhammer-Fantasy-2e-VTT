class ToolbarModel:
    def __init__(self):
        self.selected_tool = "select"
        
    def set_selected_tool(self, tool):
        self.selected_tool = tool
        
    def get_selected_tool(self):
        return self.selected_tool