from PySide2.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

import src.services.hello as hello_service


class MainFrame(QWidget):
    _message: str = ""

    def __init__(self):
        super().__init__()
        self._get_data()
        self._setup_ui()

    def _get_data(self):
        self._message = hello_service.get_hello_world()

    def _setup_ui(self):
        self.setWindowTitle("Ma thune")
        main_layout: QVBoxLayout = QVBoxLayout(self)
        hello_world_label: QLabel = QLabel(self._message)
        main_layout.addWidget(hello_world_label)


if __name__ == "__main__":
    app = QApplication()
    window = MainFrame()
    window.show()
    app.exec_()
