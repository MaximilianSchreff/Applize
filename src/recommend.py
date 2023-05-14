# -*- coding: utf-8 -*-
"""
Created on Sat May 13 17:32:20 2023

@author: NamPh
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from sentence_transformers import SentenceTransformer, util
import os
import pandas as pd

# This is a test Widget which can be used for a tab
class RecommendTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.model = SentenceTransformer('all-MiniLM-L6-v2', device="cpu")
        #layout = QtWidgets.QVBoxLayout(self)
        self.resize(1116, 591)
        
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setReadOnly(False)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 540, 411))
        self.textEdit.setObjectName("textBrowser")
        self.textEdit_2 = QtWidgets.QTextEdit(self)
        self.textEdit_2.setReadOnly(False)
        self.textEdit_2.setGeometry(QtCore.QRect(580, 20, 521, 411))
        self.textEdit_2.setObjectName("textBrowser_2")
        
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(510, 450, 93, 28))
        self.pushButton.setObjectName("pushButton")

        
        self.label = QtWidgets.QLabel(self)

        self.label.setGeometry(QtCore.QRect(370, 510, 200, 31))


        self.font = QtGui.QFont()
        self.font.setFamily("Impact")
        self.font.setPointSize(22)
        self.font.setBold(False)
        self.font.setItalic(False)
        self.font.setWeight(50)
        self.label.setFont(self.font)
        self.label.setStyleSheet("font: 22pt \"Impact\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)

        self.label_2.setGeometry(QtCore.QRect(420, 540, 91, 41))

        self.font = QtGui.QFont()
        self.font.setFamily("Impact")
        self.font.setPointSize(20)
        self.label_2.setFont(self.font)

        self.label_2.setObjectName("label_2")
        
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(570, 510, 600, 31))


        self.font = QtGui.QFont()
        self.font.setFamily("Impact")
        self.font.setPointSize(22)
        self.font.setBold(False)
        self.font.setItalic(False)
        self.font.setWeight(50)
        self.label_5.setFont(self.font)
        self.label_5.setStyleSheet("font: 22pt \"Impact\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self)

        self.label_6.setGeometry(QtCore.QRect(620, 540, 600, 41))

        self.font = QtGui.QFont()
        self.font.setFamily("Impact")
        self.font.setPointSize(20)
        self.label_6.setFont(self.font)
        self.label_6.setObjectName("label_6")

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(180, 440, 181, 41))
        self.font = QtGui.QFont()
        self.font.setFamily("Impact")
        self.font.setPointSize(20)
        self.label_3.setFont(self.font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(740, 440, 231, 41))
        self.font = QtGui.QFont()
        self.font.setFamily("Impact")
        self.font.setPointSize(20)
        self.label_4.setFont(self.font)
        self.label_4.setObjectName("label_4")
        
        QtCore.QMetaObject.connectSlotsByName(self)
        self._translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(self._translate("Form", "Start"))
        self.label.setText(self._translate("Form", "Score: 0"))
        self.label_2.setText(self._translate("Form", "MATCH"))
        
        self.label_5.setText(self._translate("Form", "Score: 0"))
        self.label_6.setText(self._translate("Form", "MATCH FOR PAST JOB POSTINGS"))
        
        self.label_3.setText(self._translate("Form", "YOUR CV TEXT"))
        self.label_4.setText(self._translate("Form", "JOB DESCRIPTION"))
        self.label_5.setText(self._translate("Form", "SCORE: 0"))
        self.label_6.setText(self._translate("Form", "MATCHING WITH PAST JOB POSTINGS"))
        
        #Button clicked
        self.pushButton.clicked.connect(self.state_changed)
        
    def state_changed(self):
        cv_text = self.textEdit.toPlainText()
        job_text = self.textEdit_2.toPlainText()
        
        embedding1 = self.model.encode(cv_text, convert_to_tensor=True)
        embedding2 = self.model.encode(job_text, convert_to_tensor=True)
        # compute similarity scores of two embeddings
        cosine_scores = util.pytorch_cos_sim(embedding1, embedding2)
        cosine_scores = cosine_scores.item()*100
        
        if os.path.exists("../data/applications.csv"):
            df = pd.read_csv("../data/applications.csv", sep=";")
            job_postings = list(df["jobPosting"])
            for x in job_postings:
                if len(str(x)) < 1 or not isinstance(x, str):
                    job_postings.remove(x)
            
            if len(job_postings) > 0 :
                average_score = 0
                
                for job_posting in job_postings:
                    embedding3 = self.model.encode(job_posting, convert_to_tensor=True)
                    temp = util.pytorch_cos_sim(embedding1, embedding3)
                    temp = temp.item()*100
                    average_score += temp
                    
                average_score /= len(job_postings)
                self.label_5.setText(self._translate("Form", "Score: "+str(round(average_score,2))))
        
        self.label.setText(self._translate("Form", "Score: "+str(round(cosine_scores,2))))
        self.label.setText(self._translate("Form", "Score: " +str(round(cosine_scores,2))))
