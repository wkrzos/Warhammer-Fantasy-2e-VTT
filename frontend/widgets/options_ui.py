from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton

class OptionsViewUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel(self.tr("Options")))

        self.option_list = QListWidget()
        layout.addWidget(self.option_list)

        self.exit_button = QPushButton(self.tr("Exit"))
        layout.addWidget(self.exit_button)

        self.setLayout(layout)

    def update_option_list(self, options):
        self.option_list.clear()
        for key, value in options.items():
            self.option_list.addItem(self.tr(f"{key}: {value}"))
