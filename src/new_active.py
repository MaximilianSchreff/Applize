# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_Active.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Application import Application


class ActiveTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkFrame = QtWidgets.QFrame(self)
        self.checkFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.checkFrame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.checkFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.checkFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.checkFrame.setObjectName("checkFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.checkFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.aktivBox = QtWidgets.QCheckBox(self.checkFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.aktivBox.setFont(font)
        self.aktivBox.setChecked(True)
        self.aktivBox.setTristate(False)
        self.aktivBox.setObjectName("aktivBox")
        self.verticalLayout_2.addWidget(self.aktivBox, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.checkFrame, 0, QtCore.Qt.AlignTop)
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setObjectName("tableWidget")

        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)

        self.verticalLayout.addWidget(self.tableWidget)
        self.frame_2 = QtWidgets.QFrame(self)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout.addWidget(self.frame_2)

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.aktivBox.setText(_translate("Form", "Aktiv"))