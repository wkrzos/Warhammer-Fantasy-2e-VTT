from PySide6.QtWidgets import QApplication
from model.creatures_model import CreaturesModel
from controller.creatures_controller import CreaturesController
from frontend.widgets.creatures_ui import CreaturesViewUI
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    model = CreaturesModel()
    view = CreaturesViewUI()
    controller = CreaturesController(model, view)

    view.show()
    sys.exit(app.exec())
