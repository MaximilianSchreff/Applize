# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'active.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Application import Application


# This is a test Widget which can be used for a tab
class ActiveTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout(self)
        
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 751, 461))
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
        
        _translate = QtCore.QCoreApplication.translate
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Company"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Position"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Status"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Date"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Feedback"))
        
        layout.addWidget(self.tableWidget)
        
        self.checkBox = QtWidgets.QCheckBox()
        self.checkBox.setGeometry(QtCore.QRect(20, 20, 91, 20))
        self.checkBox.setObjectName("checkBox")
        
        layout.addWidget(self.checkBox)
        
        self.checkBox.setText(_translate("Form", "Only Active"))
        
        self.checkBox.stateChanged.connect(self.state_changed)

    def state_changed(self):
        if self.checkBox.isChecked():
            numRows = self.tableWidget.rowCount()
            for i in range(numRows):
                item = self.tableWidget.item(i, 2)  # get the status item in this row
                if item.text() != "Application Sent" and item.text() != "Interview Invite":
                    self.tableWidget.setRowHidden(i, True)  # hide the row
        else:
            numRows = self.tableWidget.rowCount()
            for i in range(numRows):
                self.tableWidget.setRowHidden(i, False)  # show all rows
    
    def add_application(self, application: Application):
        # Create a empty row at bottom of table
        numRows = self.tableWidget.rowCount()
        self.tableWidget.insertRow(numRows)     
        # Add text to the row
        self.tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(application.company))
        self.tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(
            application.jobTitle + " - " + application.employmentType))
        self.tableWidget.setItem(numRows, 2, QtWidgets.QTableWidgetItem(application.status))
        self.tableWidget.setItem(numRows, 3, QtWidgets.QTableWidgetItem(application.date))
        self.tableWidget.setItem(numRows, 4, QtWidgets.QTableWidgetItem(application.link))

    def load_app_list(self, applications):
        for application in applications:
            self.add_application(application)
