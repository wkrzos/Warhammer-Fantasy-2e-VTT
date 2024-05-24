import sys
from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton
from PySide6.QtGui import QPainter, QPen, QColor, QFont, QBrush
from PySide6.QtCore import Qt, QPoint, QRect

from backend.characterCard.cards import Character
from backend.mechanic.token import Token


# class Token:
#     def __init__(self, character):
#         self.character = character
#         self.position = character.get_position()
#
#     def set_position(self, x, y):
#         self.position = (x, y)
#         self.character.set_position(x, y)
#
#     def get_position(self):
#         return self.position

# Update MapView class (previously defined) to include a call to update_action_panel

class MapView(QWidget):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.grid_size = 50  # Size of each grid cell
        self.offset = QPoint(0, 0)  # Offset for panning
        self.dragging = False
        self.last_mouse_pos = QPoint(0, 0)
        self.characters = [
            Character("Hero" ),
            Character("Enemy" )
        ]
        self.tokens = [Token(character) for character in self.characters]
        self.tokens[0].position = (5,5)
        self.tokens[1].position = (10,10)
        self.selected_tokens = []
        self.zoom_level = 1.0  # Initial zoom level
        self.measuring = False
        self.measure_start = None
        self.measure_end = None
        self.selecting = False
        self.selection_start = None
        self.selection_end = None

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        self.draw_grid(painter)
        self.draw_tokens(painter)
        self.draw_measurement(painter)
        self.draw_selection(painter)
        painter.end()

    def draw_grid(self, painter):
        pen = QPen(QColor(200, 200, 200), 1)
        painter.setPen(pen)

        scaled_grid_size = int(self.grid_size * self.zoom_level)
        start_x = self.offset.x() % scaled_grid_size
        start_y = self.offset.y() % scaled_grid_size

        for x in range(start_x, self.width(), scaled_grid_size):
            painter.drawLine(x, 0, x, self.height())
        
        for y in range(start_y, self.height(), scaled_grid_size):
            painter.drawLine(0, y, self.width(), y)

    def draw_tokens(self, painter):
        for token in self.tokens:
            x, y = token.get_position()
            scaled_grid_size = self.grid_size * self.zoom_level
            screen_x = x * scaled_grid_size + self.offset.x()
            screen_y = y * scaled_grid_size + self.offset.y()
            painter.setBrush(QColor(255, 0, 0) if token not in self.selected_tokens else QColor(0, 255, 0))
            painter.drawEllipse(screen_x, screen_y, scaled_grid_size, scaled_grid_size)
            painter.drawText(screen_x + 10, screen_y + 30, token.creature.name)

    def draw_measurement(self, painter):
        if self.measure_start and self.measure_end:
            pen = QPen(QColor(0, 0, 255), 2)
            painter.setPen(pen)
            painter.drawLine(self.measure_start, self.measure_end)

            # Calculate distance in grid squares
            dx = abs(self.measure_end.x() - self.measure_start.x())
            dy = abs(self.measure_end.y() - self.measure_start.y())
            distance = max(dx, dy) // (self.grid_size * self.zoom_level)
            
            # Display the distance
            mid_point = (self.measure_start + self.measure_end) / 2
            painter.setFont(QFont('Arial', 14))
            painter.setPen(QColor(0, 0, 0))
            painter.drawText(mid_point, f"{distance:.0f} squares")

    def draw_selection(self, painter):
        if self.selecting and self.selection_start and self.selection_end:
            rect = QRect(QPoint(self.selection_start.toPoint()), QPoint(self.selection_end.toPoint()))
            painter.setPen(QPen(QColor(0, 0, 255), 1, Qt.DashLine))
            painter.setBrush(QBrush(QColor(0, 0, 255, 50)))
            painter.drawRect(rect)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.last_mouse_pos = event.position()
            if self.main_window.toolbar.selected_tool == "select":
                token = self.get_token_at_position(event.position())
                if token:
                    if token in self.selected_tokens:
                        self.dragging = True
                    else:
                        self.selected_tokens = [token]
                        self.dragging = True
                else:
                    self.selected_tokens = []
                    self.selection_start = event.position()
                    self.selection_end = event.position()
                    self.selecting = True
            elif self.main_window.toolbar.selected_tool == "pan":
                self.dragging = True
            elif self.main_window.toolbar.selected_tool == "measure":
                self.measuring = True
                self.measure_start = event.position()
                self.measure_end = event.position()
            self.main_window.update_action_panel()  # Update action panel on mouse press

    def mouseMoveEvent(self, event):
        if self.dragging:
            delta = event.position() - self.last_mouse_pos
            if self.main_window.toolbar.selected_tool == "select" and self.selected_tokens:
                self.move_tokens(delta, event.modifiers() & Qt.ShiftModifier)
            elif self.main_window.toolbar.selected_tool == "pan":
                self.offset += delta.toPoint()
            self.last_mouse_pos = event.position()
            self.update()
        elif self.measuring:
            self.measure_end = event.position()
            self.update()
        elif self.selecting:
            self.selection_end = event.position()
            self.update_selection()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False
            if self.main_window.toolbar.selected_tool == "select" and self.selecting:
                self.selecting = False
                self.update_selection()
            elif self.selected_tokens and not (event.modifiers() & Qt.ShiftModifier):
                self.snap_to_grid_multiple(self.selected_tokens)
            self.measuring = False
            self.main_window.update_action_panel()  # Update action panel on mouse release

    def wheelEvent(self, event):
        # Zoom in and out with the mouse wheel
        if event.angleDelta().y() > 0:
            self.zoom_in()
        else:
            self.zoom_out()

    def update_selection(self):
        self.selected_tokens = []
        if self.selection_start and self.selection_end:
            rect = QRect(QPoint(self.selection_start.toPoint()), QPoint(self.selection_end.toPoint())).normalized()
            for token in self.tokens:
                x, y = token.get_position()
                scaled_grid_size = self.grid_size * self.zoom_level
                screen_x = x * scaled_grid_size + self.offset.x()
                screen_y = y * scaled_grid_size + self.offset.y()
                token_rect = QRect(screen_x, screen_y, scaled_grid_size, scaled_grid_size)
                if rect.intersects(token_rect):
                    self.selected_tokens.append(token)
        self.update()

    def move_tokens(self, delta, shift_pressed):
        if self.selected_tokens:
            dx = delta.x() / (self.grid_size * self.zoom_level)
            dy = delta.y() / (self.grid_size * self.zoom_level)
            for token in self.selected_tokens:
                if shift_pressed:
                    # Free movement
                    new_x = token.get_position()[0] + dx
                    new_y = token.get_position()[1] + dy
                else:
                    # Snap to grid
                    new_x = round(token.get_position()[0] + dx)
                    new_y = round(token.get_position()[1] + dy)
                token.set_position(new_x, new_y)
            self.update()

    def snap_to_grid_multiple(self, tokens):
        for token in tokens:
            x, y = token.get_position()
            token.set_position(round(x), round(y))
        self.update()

    def zoom_in(self):
        self.zoom_level = min(self.zoom_level + 0.1, 2.0)
        self.update()

    def zoom_out(self):
        self.zoom_level = max(self.zoom_level - 0.1, 0.1)
        self.update()

    def get_token_at_position(self, position):
        for token in self.tokens:
            x, y = token.get_position()
            scaled_grid_size = self.grid_size * self.zoom_level
            screen_x = x * scaled_grid_size + self.offset.x()
            screen_y = y * scaled_grid_size + self.offset.y()
            token_rect = QRect(screen_x, screen_y, scaled_grid_size, scaled_grid_size)
            if token_rect.contains(position.toPoint()):
                return token
        return None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MapView(None)  # For standalone testing
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())
