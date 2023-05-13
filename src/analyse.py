# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analyse.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import numpy as np


class AnalyseTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout(self)

        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.setGeometry(QtCore.QRect(70, 140, 73, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        _translate = QtCore.QCoreApplication.translate
        self.comboBox.setItemText(0, _translate("analyse", "erste"))
        self.comboBox.setItemText(1, _translate("analyse", "zweite"))
        self.comboBox.setItemText(2, _translate("analyse", "dritte"))

        layout.addWidget(self.comboBox)
        self.comboBox.currentTextChanged.connect(self.combo_changed)

        self.label = QtWidgets.QLabel()
        self.label.setGeometry(QtCore.QRect(370, 50, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setGeometry(QtCore.QRect(360, 310, 411, 20))
        self.label_2.setObjectName("label_2")
        self.label.setText(_translate("analyse", "analyse setion"))
        self.label_2.setText(_translate("analyse", "Hier kommt hin was man auswählt"))

        layout.addWidget(self.label)
        layout.addWidget(self.label_2)

    def combo_changed(self):
        self.label_2.setText(self.comboBox.currentText())