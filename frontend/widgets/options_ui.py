from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton
from frontend.util.font import DEFAULT_FONT

class OptionsViewUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        label = QLabel(self.tr("Options"))
        label.setFont(DEFAULT_FONT)
        layout.addWidget(label)

        self.option_list = QListWidget()
        self.option_list.setFont(DEFAULT_FONT)
        layout.addWidget(self.option_list)

        self.exit_button = QPushButton(self.tr("Exit"))
        self.exit_button.setFont(DEFAULT_FONT)
        layout.addWidget(self.exit_button)

        self.setLayout(layout)

    def update_option_list(self, options):
        self.option_list.clear()
        for key, value in options.items():
            item = QListWidgetItem(self.tr(f"{key}: {value}"))
            item.setFont(DEFAULT_FONT)
            self.option_list.addItem(item)
