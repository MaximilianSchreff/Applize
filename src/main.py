import sys

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi

from main_windows_ui import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


applications = []
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("QtCurve")
    win = Window()
    win.show()
    sys.exit(app.exec())