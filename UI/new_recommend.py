# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_Recommend.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(602, 450)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 565, 587))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)
        self.textEdit_4 = QtWidgets.QTextEdit(self.frame_5)
        self.textEdit_4.setObjectName("textEdit_4")
        self.gridLayout_3.addWidget(self.textEdit_4, 1, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 7, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 7, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 2)
        self.verticalLayout_4.addWidget(self.widget)
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Fit Analysis - Computing Similiarity of new job postings to resumes / past postings"))
        self.label_7.setText(_translate("Form", "Job Posting"))
        self.label_2.setText(_translate("Form", "Current Resume"))
        self.pushButton.setText(_translate("Form", "Compute Similiarity"))
        self.lineEdit.setText(_translate("Form", "<Match-Score>"))
        self.label_6.setText(_translate("Form", "Paste the resume, you want to use, to see whether it is a fit for the posting!"))
        self.label.setText(_translate("Form", "We use past job postings of successful applications (positive weight) and declined ones (negative weight)"))
        self.label_3.setText(_translate("Form", "See the Match-Score compared to your past successfull / declined Applications!"))
        self.lineEdit_2.setText(_translate("Form", "<Match-Score>"))
