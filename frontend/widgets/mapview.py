from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import QPainter, QPen, QColor, QMouseEvent
from PySide6.QtCore import Qt, QPoint

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

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        self.draw_grid(painter)
        self.draw_characters(painter)

    def draw_grid(self, painter):
        pen = QPen(QColor(200, 200, 200), 1)
        painter.setPen(pen)

        start_x = self.offset.x() % self.grid_size
        start_y = self.offset.y() % self.grid_size

        for x in range(start_x, self.width(), self.grid_size):
            painter.drawLine(x, 0, x, self.height())
        
        for y in range(start_y, self.height(), self.grid_size):
            painter.drawLine(0, y, self.width(), y)

    def draw_characters(self, painter):
        for character in self.characters:
            x, y = character.get_position()
            screen_x = x * self.grid_size + self.offset.x()
            screen_y = y * self.grid_size + self.offset.y()
            painter.setBrush(QColor(255, 0, 0))
            painter.drawEllipse(screen_x, screen_y, self.grid_size, self.grid_size)
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
            screen_x = x * self.grid_size + self.offset.x()
            screen_y = y * self.grid_size + self.offset.y()
            rect = QRect(screen_x, screen_y, self.grid_size, self.grid_size)
            if rect.contains(position.toPoint()):
                self.selected_character = character
                break

    def move_character(self, delta):
        if self.selected_character:
            dx = delta.x() // self.grid_size
            dy = delta.y() // self.grid_size
            self.selected_character.move(dx, dy)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MapView()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())
