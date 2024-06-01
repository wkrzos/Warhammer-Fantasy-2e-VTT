from PySide6.QtCore import QObject, QPoint, Qt, QRect
from frontend.widgets.map_ui import MapViewUI
from model.map_model import MapViewModel

class MapViewController:
    def __init__(self, model: MapViewModel, view: MapViewUI, main_window_model):
        super().__init__()
        self.model = model
        self.view = view
        self.view.model = model
        self.main_window_model = main_window_model

        self.selected_tool = None
        self.view.setMouseTracking(True)
        self.connect_signals()

    def connect_signals(self):
        self.view.mousePressEvent = self.mousePressEvent
        self.view.mouseMoveEvent = self.mouseMoveEvent
        self.view.mouseReleaseEvent = self.mouseReleaseEvent
        self.view.wheelEvent = self.wheelEvent

    def set_selected_tool(self, tool):
        self.selected_tool = tool

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.last_mouse_pos = event.position()
            if self.selected_tool == "select":
                token = self.get_token_at_position(event.position())
                if token:
                    if token in self.model.get_selected_tokens():
                        self.model.dragging = True
                    else:
                        self.model.set_selected_tokens([token])
                        self.model.dragging = True
                else:
                    self.model.set_selected_tokens([])
                    self.model.set_selection(event.position(), event.position())
                    self.model.selecting = True
            elif self.selected_tool == "pan":
                self.model.dragging = True
            elif self.selected_tool == "measure":
                self.model.set_measurement(event.position(), event.position())
                self.model.measuring = True
            self.main_window_model.update_action_panel()

    def mouseMoveEvent(self, event):
        if self.model.dragging:
            delta = event.position() - self.last_mouse_pos
            if self.selected_tool == "select" and self.model.get_selected_tokens():
                self.move_tokens(delta, event.modifiers() & Qt.ShiftModifier)
            elif self.selected_tool == "pan":
                offset = self.model.get_offset()
                self.model.set_offset((offset[0] + delta.x(), offset[1] + delta.y()))
            self.last_mouse_pos = event.position()
            self.view.update()
        elif self.model.measuring:
            self.model.set_measurement(self.model.measure_start, event.position())
            self.view.update()
        elif self.model.selecting:
            self.model.set_selection(self.model.selection_start, event.position())
            self.update_selection()
            self.view.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.model.dragging = False
            if self.selected_tool == "select" and self.model.selecting:
                self.model.selecting = False
                self.update_selection()  # DEBUG flag
                self.model.set_selection(None, None)
            elif self.model.get_selected_tokens() and not (event.modifiers() & Qt.ShiftModifier):
                self.snap_to_grid_multiple(self.model.get_selected_tokens())
            self.model.measuring = False
            self.main_window_model.update_action_panel()

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.zoom_in()
        else:
            self.zoom_out()

    def update_selection(self):
        selected_tokens = []
        selection_start, selection_end = self.model.get_selection()
        if selection_start and selection_end:
            rect = QRect(QPoint(selection_start.toPoint()), QPoint(selection_end.toPoint())).normalized()
            for token in self.model.get_tokens():
                x, y = token.get_position()
                scaled_grid_size = self.model.grid_size * self.model.get_zoom_level()
                screen_x = x * scaled_grid_size + self.model.get_offset()[0]
                screen_y = y * scaled_grid_size + self.model.get_offset()[1]
                token_rect = QRect(screen_x, screen_y, scaled_grid_size, scaled_grid_size)
                if rect.intersects(token_rect):
                    selected_tokens.append(token)
        self.model.set_selected_tokens(selected_tokens)
        self.view.update()

    def move_tokens(self, delta, shift_pressed):
        selected_tokens = self.model.get_selected_tokens()
        if selected_tokens:
            dx = delta.x() / (self.model.grid_size * self.model.get_zoom_level())
            dy = delta.y() / (self.model.grid_size * self.model.get_zoom_level())
            for token in selected_tokens:
                if shift_pressed:
                    new_x = token.get_position()[0] + dx
                    new_y = token.get_position()[1] + dy
                else:
                    new_x = round(token.get_position()[0] + dx)
                    new_y = round(token.get_position()[1] + dy)
                token.set_position(new_x, new_y)
            self.view.update()

    def snap_to_grid_multiple(self, tokens):
        for token in tokens:
            x, y = token.get_position()
            token.set_position(round(x), round(y))
        self.view.update()

    def zoom_in(self):
        self.model.set_zoom_level(min(self.model.get_zoom_level() + 0.1, 2.0))
        self.view.update()

    def zoom_out(self):
        self.model.set_zoom_level(max(self.model.get_zoom_level() - 0.1, 0.1))
        self.view.update()

    def get_token_at_position(self, position):
        for token in self.model.get_tokens():
            x, y = token.get_position()
            scaled_grid_size = self.model.grid_size * self.model.get_zoom_level()
            screen_x = x * scaled_grid_size + self.model.get_offset()[0]
            screen_y = y * scaled_grid_size + self.model.get_offset()[1]
            token_rect = QRect(screen_x, screen_y, scaled_grid_size, scaled_grid_size)
            if token_rect.contains(position.toPoint()):
                return token
        return None

