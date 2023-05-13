import sys

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi
from data import create_file_system, load_applications_from_csv
from main_windows_ui import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    create_file_system()
    load_applications_from_csv()
    app = QApplication(sys.argv)
    app.setStyle("QtCurve")
    win = Window()
    win.show()
    sys.exit(app.exec())