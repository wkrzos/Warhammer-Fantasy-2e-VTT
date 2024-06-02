import os
from PySide6.QtCore import QTranslator

class GuiTranslator:
    
    @staticmethod
    def load_translations(app, language="en"):
        translator = QTranslator()
        translation_file = os.path.normpath(f"translations/{language}.qm")
        if translator.load(translation_file):
            app.installTranslator(translator)
            print(f"Loaded translation file: {translation_file}")
        else:
            print(f"Translation file not found: {translation_file}")
        return translator