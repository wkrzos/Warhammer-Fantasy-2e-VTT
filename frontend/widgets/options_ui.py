from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QComboBox, QListWidgetItem
from PySide6.QtCore import Signal, QCoreApplication
from frontend.util.font import DEFAULT_FONT

class OptionsViewUI(QWidget):
    languageChanged = Signal(str)

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

        self.language_selector = QComboBox()
        self.language_selector.addItems(["en", "pl", "de"])  # Available languages
        self.language_selector.setFont(DEFAULT_FONT)
        layout.addWidget(self.language_selector)

        apply_button = QPushButton(self.tr("Apply Language"))
        apply_button.setFont(DEFAULT_FONT)
        apply_button.clicked.connect(self.change_language)
        layout.addWidget(apply_button)

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

    def change_language(self):
        selected_language = self.language_selector.currentText()
        if selected_language == "en":
            language_code = "en"
        elif selected_language == "pl":
            language_code = "pl"
        elif selected_language == "de":
            language_code = "de"
        else:
            language_code = "en"  # Default to English if not found

        # Emit signal with the selected language code
        self.languageChanged.emit(language_code)
