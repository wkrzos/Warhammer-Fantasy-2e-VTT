from controller.action_panel_controller import ActionPanelController
from controller.chat_controller import ChatController
from controller.creatures_controller import CreaturesController
from controller.items_controller import ItemsController
from controller.map_controller import MapViewController
from controller.music_player_controller import MusicPlayerController
from controller.options_controller import OptionsController
from controller.toolbar_controller import ToolbarController
from frontend.main_window_ui import MainWindowView
from frontend.widgets.map_ui import MapViewUI
from model.main_window_model import MainWindowModel


class MainWindowController:
    def __init__(self, model:MainWindowModel, view: MainWindowView):
        self.model = model
        self.view = view
        self.view.setup_ui(self.model)
        self.map_view_controller = MapViewController(self.model.map_view_model, self.view.map_view_ui, self)
        self.chat_controller = ChatController(self.model.chat_model, self.view.chat_view_ui)
        self.creatures_controller = CreaturesController(self.model.creatures_model, self.view.creatures_view_ui)
        self.items_controller = ItemsController(self.model.items_model, self.view.items_view_ui)
        self.options_controller = OptionsController(self.model.options_model, self.view.options_view_ui)
        self.music_player_controller = MusicPlayerController(self.model.music_player_model, self.view.music_player_view_ui)
        self.action_panel_controller = ActionPanelController(self.model.action_panel_model, self.view.action_panel_ui)
        self.toolbar_controller = ToolbarController(self.model.toolbar_model, self.view.toolbar_view, self)
        self.music_controller = MusicPlayerController(self.model.music_player_model, self.view.music_player_view_ui)
        # Connect the toolbar selection signal to the map view controller
        self.toolbar_controller.view.tool_selected = self.tool_selected

    def tool_selected(self, tool):
        # Propagate the selected tool to the map view controller
        self.map_view_controller.set_selected_tool(tool)

    def update_action_panel(self):
        self.action_panel_controller.update_actions(self.map_view_controller.model.selected_tokens)