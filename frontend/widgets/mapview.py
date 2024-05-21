import sys
from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout
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

class MapView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.grid_size = 50  # Size of each grid cell
        self.offset = QPoint(0, 0)  # Offset for panning
        self.dragging = False
        self.last_mouse_pos = QPoint(0, 0)
        self.characters = [Character("Hero", (5, 5))]
        self.selected_character = None
        self.zoom_level = 1.0  # Initial zoom level

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        self.draw_grid(painter)
        self.draw_characters(painter)
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

    def draw_characters(self, painter):
        for character in self.characters:
            x, y = character.get_position()
            scaled_grid_size = self.grid_size * self.zoom_level
            screen_x = x * scaled_grid_size + self.offset.x()
            screen_y = y * scaled_grid_size + self.offset.y()
            painter.setBrush(QColor(255, 0, 0))
            painter.drawEllipse(screen_x, screen_y, scaled_grid_size, scaled_grid_size)
            painter.drawText(screen_x + 10, screen_y + 30, character.name)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.last_mouse_pos = event.position()
            self.select_character(event.position())

    def mouseMoveEvent(self, event):
        if self.dragging:
            delta = event.position() - self.last_mouse_pos
            if self.selected_character:
                self.move_character(delta)
            else:
                self.offset += delta.toPoint()
            self.last_mouse_pos = event.position()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False
            self.selected_character = None

    def select_character(self, position):
        for character in self.characters:
            x, y = character.get_position()
            scaled_grid_size = self.grid_size * self.zoom_level
            screen_x = x * scaled_grid_size + self.offset.x()
            screen_y = y * scaled_grid_size + self.offset.y()
            rect = QRect(screen_x, screen_y, scaled_grid_size, scaled_grid_size)
            if rect.contains(position.toPoint()):
                self.selected_character = character
                break

    def move_character(self, delta):
        if self.selected_character:
            dx = delta.x() / self.grid_size
            dy = delta.y() / self.grid_size
            self.selected_character.move(dx, dy)
            
    def zoom_in(self):
        self.zoom_level = min(self.zoom_level + 0.1, 2.0)
        self.update()

    def zoom_out(self):
        self.zoom_level = max(self.zoom_level - 0.1, 0.1)
        self.update()

    def wheelEvent(self, event):
        # Zoom in and out with the mouse wheel
        if event.angleDelta().y() > 0:
            self.zoom_in()
        else:
            self.zoom_out()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MapView()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())
