import sys
from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtCore import Qt, QPoint, QRect

class Character:
    def __init__(self, name, position=(0, 0)):
        self.name = name
        self.position = position

    def set_position(self, x, y):
        self.position = (x, y)

    def get_position(self):
        return self.position

    def move(self, dx, dy):
        self.position = (self.position[0] + dx, self.position[1] + dy)

class Token:
    def __init__(self, character):
        self.character = character
        self.position = character.get_position()

    def set_position(self, x, y):
        self.position = (x, y)
        self.character.set_position(x, y)

    def get_position(self):
        return self.position

class MapView(QWidget):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.grid_size = 50  # Size of each grid cell
        self.offset = QPoint(0, 0)  # Offset for panning
        self.dragging = False
        self.last_mouse_pos = QPoint(0, 0)
        self.characters = [
            Character("Hero", (5, 5)),
            Character("Enemy", (10, 10))
        ]
        self.tokens = [Token(character) for character in self.characters]
        self.selected_token = None
        self.zoom_level = 1.0  # Initial zoom level
        self.measuring = False
        self.measure_start = None
        self.measure_end = None

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        self.draw_grid(painter)
        self.draw_tokens(painter)
        self.draw_measurement(painter)
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
            painter.setBrush(QColor(255, 0, 0))
            painter.drawEllipse(screen_x, screen_y, scaled_grid_size, scaled_grid_size)
            painter.drawText(screen_x + 10, screen_y + 30, token.character.name)

    def draw_measurement(self, painter):
        if self.measure_start and self.measure_end:
            pen = QPen(QColor(0, 0, 255), 2)
            painter.setPen(pen)
            painter.drawLine(self.measure_start, self.measure_end)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.last_mouse_pos = event.position()
            if self.main_window.toolbar.selected_tool == "select":
                self.dragging = True
                self.select_token(event.position())
            elif self.main_window.toolbar.selected_tool == "pan":
                self.dragging = True
            elif self.main_window.toolbar.selected_tool == "measure":
                self.measuring = True
                self.measure_start = event.position()
                self.measure_end = event.position()

    def mouseMoveEvent(self, event):
        if self.dragging:
            delta = event.position() - self.last_mouse_pos
            if self.main_window.toolbar.selected_tool == "select" and self.selected_token:
                self.move_token(delta, event.modifiers() & Qt.ShiftModifier)
            elif self.main_window.toolbar.selected_tool == "pan":
                self.offset += delta.toPoint()
            self.last_mouse_pos = event.position()
            self.update()
        elif self.measuring:
            self.measure_end = event.position()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False
            if self.selected_token and not (event.modifiers() & Qt.ShiftModifier):
                self.snap_to_grid(self.selected_token)
            self.selected_token = None
            self.measuring = False

    def wheelEvent(self, event):
        # Zoom in and out with the mouse wheel
        if event.angleDelta().y() > 0:
            self.zoom_in()
        else:
            self.zoom_out()

    def select_token(self, position):
        for token in self.tokens:
            x, y = token.get_position()
            scaled_grid_size = self.grid_size * self.zoom_level
            screen_x = x * scaled_grid_size + self.offset.x()
            screen_y = y * scaled_grid_size + self.offset.y()
            rect = QRect(screen_x, screen_y, scaled_grid_size, scaled_grid_size)
            if rect.contains(position.toPoint()):
                self.selected_token = token
                break

    def move_token(self, delta, shift_pressed):
        if self.selected_token:
            if shift_pressed:
                # Free movement
                dx = delta.x() / (self.grid_size * self.zoom_level)
                dy = delta.y() / (self.grid_size * self.zoom_level)
                new_x = self.selected_token.get_position()[0] + dx
                new_y = self.selected_token.get_position()[1] + dy
            else:
                # Snap to grid
                dx = delta.x() / (self.grid_size * self.zoom_level)
                dy = delta.y() / (self.grid_size * self.zoom_level)
                new_x = round(self.selected_token.get_position()[0] + dx)
                new_y = round(self.selected_token.get_position()[1] + dy)
            
            self.selected_token.set_position(new_x, new_y)

    def snap_to_grid(self, token):
        x, y = token.get_position()
        token.set_position(round(x), round(y))
        self.update()

    def zoom_in(self):
        self.zoom_level = min(self.zoom_level + 0.1, 2.0)
        self.update()

    def zoom_out(self):
        self.zoom_level = max(self.zoom_level - 0.1, 0.1)
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MapView(None)  # For standalone testing
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())
