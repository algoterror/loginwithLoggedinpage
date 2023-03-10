# -*- coding: utf-8 -*-
import sys

import pymongo
from pymongo import MongoClient
from Listfile import CommonList

# print("Welcome to pymongo")
# client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
# print("Connection Successful")
# db = client['ankita']
# collections = db['test']

# dictionary = {'name': 'ankita', 'age': '21', 'company': 'cars24'}
# collections.insert_one(dictionary)

# Form implementation generated from reading ui file 's2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from Listfile import CommonList
from connectionDB import addItem



class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(681, 376)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setSizeIncrement(QtCore.QSize(0, 6))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(4)
        Form.setFont(font)
        icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("img/295128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setToolTipDuration(0)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(221, 245, 255, 255), stop:1 rgba(255, 255, 255, 255));")

        # Frame for signup area
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(230, 20, 411, 231))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # inside the frame
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 411, 33))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(170, 255, 255);\n"
                                   "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(0, 0, 127);")
        self.label_4.setObjectName("label_4")

        # signup button
        self.crtaccnt = QtWidgets.QPushButton(self.frame)
        self.crtaccnt.setGeometry(QtCore.QRect(150, 170, 101, 31))
        self.crtaccnt.setStyleSheet("background-color: rgb(170, 255, 255);\n"
                                    "font: 75 12pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(0, 0, 127);")

        self.crtaccnt.setObjectName("crtaccnt")

        # small window screen
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 40, 411, 111))
        self.layoutWidget.setObjectName("layoutWidget")

        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setBaseSize(QtCore.QSize(65, 1))
        self.label.setStyleSheet("color: rgb(0, 170, 127);\n"
                                 "font: 10pt \"MS Shell Dlg 2\";\n"
                                 "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));\n"
                                 "border-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(71, 1, 137, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)

        # placeholder username
        self.name = QtWidgets.QLineEdit(self.layoutWidget)
        self.name.setMinimumSize(QtCore.QSize(0, 0))
        self.name.setText("")
        self.name.setObjectName("name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name)

        # Login to your account
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("color: rgb(0, 170, 127);\n"
                                   "font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)

        # password placeholder
        self.passcode = QtWidgets.QLineEdit(self.layoutWidget)
        self.passcode.setMinimumSize(QtCore.QSize(4, 0))
        self.passcode.setMaximumSize(QtCore.QSize(16777214, 16777215))
        self.passcode.setBaseSize(QtCore.QSize(0, 15))
        self.passcode.setText("")
        self.passcode.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.passcode.setProperty("QLineEdit", "")
        self.passcode.setObjectName("passcode")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passcode)

        # password label name
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("color: rgb(0, 170, 127);\n"
                                   "font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.cnfrmpassco = QtWidgets.QLineEdit(self.layoutWidget)
        self.cnfrmpassco.setObjectName("cnfrmpassco")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cnfrmpassco)

        # white message box
        self.Message = QtWidgets.QTextBrowser(Form)
        self.Message.setGeometry(QtCore.QRect(40, 260, 481, 91))
        self.Message.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "font: 75 10pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(0, 85, 0);")
        self.Message.setObjectName("Message")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 60, 141, 131))
        self.label_5.setText("")
        self.label_5.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_5.setPixmap(QtGui.QPixmap("i2.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.crtaccnt.clicked.connect(lambda: self.addData(Form))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sign Up Page"))
        self.label_4.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" vertical-align:super;\">Enter Your Details Here</span></p></body></html>"))
        self.crtaccnt.setText(_translate("Form", "Enter"))
        self.label.setText(_translate("Form", "USERNAME"))
        self.name.setPlaceholderText(_translate("Form", "Enter your full name"))
        self.label_3.setText(_translate("Form", "PASSWORD"))
        self.passcode.setPlaceholderText(_translate("Form", "Enter your new password"))
        self.label_2.setText(_translate("Form", "CONFIRM PASSWORD"))
        self.cnfrmpassco.setPlaceholderText(_translate("Form", "Enter your confirm password"))

    def addData(self, Form):
        # print(self.name.text(),self.code.text(),self.cnfrmcode.text())

        if (self.passcode.text() != self.cnfrmpassco.text()):
            self.Message.setText("PASSWORDS DONT MATCH")
        elif (len(self.name.text()) < 3):
            self.Message.setText("name too short")
        elif (len(self.passcode.text()) < 6):
            self.Message.setText("PassWord should have 6 didigts")
        else:
            self.Message.setText("SUCCESS")
            # self.Listfile.get_list()
            # self.Listfile.add_to_list({'name':self.name.text(),'code':self.code.text()})

            # data to be taken is self.name.text()   self.code.text()

            CommonList.reqData.append({'name': self.name.text(), 'code': self.passcode.text()})
            # insertThese = [
            #     {'name': self.name.text(), 'code': self.passcode.text()}]
            # collections.insert_many({'name': self.name.text(), 'code': self.passcode.text()})

            # collections.insert_one({'name': self.name.text(), 'code': self.passcode.text()})
            # print(self.Listfile.reqData)
            # self.ui.lst=self.Listfile.reqData
            addItem()
            Form.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
