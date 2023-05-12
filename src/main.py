from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 1500, 1000)
    win.setWindowTitle("Applize - Application Insides")

    win.show()
    sys.exit(app.exec_())

window()