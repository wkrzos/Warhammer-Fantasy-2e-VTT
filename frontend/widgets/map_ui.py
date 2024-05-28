from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPen, QColor, QFont, QBrush
from PySide6.QtCore import Qt, QPoint, QRect
from frontend.util.font import DEFAULT_FONT, HEADING_FONT

class MapViewUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.model = None

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

        grid_size = self.model.grid_size
        zoom_level = self.model.get_zoom_level()
        offset = self.model.get_offset()

        scaled_grid_size = int(grid_size * zoom_level)
        start_x = offset[0] % scaled_grid_size
        start_y = offset[1] % scaled_grid_size

        for x in range(start_x, self.width(), scaled_grid_size):
            painter.drawLine(x, 0, x, self.height())

        for y in range(start_y, self.height(), scaled_grid_size):
            painter.drawLine(0, y, self.width(), y)

    def draw_tokens(self, painter):
        zoom_level = self.model.get_zoom_level()
        offset = self.model.get_offset()
        tokens = self.model.get_tokens()
        selected_tokens = self.model.get_selected_tokens()

        for token in tokens:
            x, y = token.get_position()
            scaled_grid_size = self.model.grid_size * zoom_level
            screen_x = x * scaled_grid_size + offset[0]
            screen_y = y * scaled_grid_size + offset[1]
            painter.setBrush(QColor(255, 0, 0) if token not in selected_tokens else QColor(0, 255, 0))
            painter.drawEllipse(screen_x, screen_y, scaled_grid_size, scaled_grid_size)
            painter.setFont(DEFAULT_FONT)
            painter.drawText(screen_x + 10, screen_y + 30, token.creature.name)

    def draw_measurement(self, painter):
        measure_start, measure_end = self.model.get_measurement()
        if measure_start and measure_end:
            pen = QPen(QColor(0, 0, 255), 2)
            painter.setPen(pen)
            painter.drawLine(measure_start, measure_end)

            dx = abs(measure_end.x() - measure_start.x())
            dy = abs(measure_end.y() - measure_start.y())
            distance = max(dx, dy) // (self.model.grid_size * self.model.get_zoom_level())

            mid_point = (measure_start + measure_end) / 2
            painter.setFont(QFont('Arial', 14))
            painter.setPen(QColor(0, 0, 0))
            painter.drawText(mid_point, self.tr(f"{distance:.0f} squares"))

    def draw_selection(self, painter):
        selection_start, selection_end = self.model.get_selection()
        if selection_start and selection_end:
            rect = QRect(QPoint(selection_start.toPoint()), QPoint(selection_end.toPoint()))
            painter.setPen(QPen(QColor(0, 0, 255), 1, Qt.DashLine))
            painter.setBrush(QBrush(QColor(0, 0, 255, 50)))
            painter.drawRect(rect)
