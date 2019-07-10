# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serial.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 30, 71, 21))
        self.label.setStyleSheet("font: 12pt \"Adobe Arabic\";\n"
"border-color: rgb(0, 0, 255);")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(140, 20, 81, 31))
        self.comboBox.setStyleSheet("font: 12pt \"Adobe Arabic\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(294, 20, 81, 31))
        self.pushButton.setStyleSheet("font: 12pt \"Adobe Arabic\";")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "请选择："))
        self.comboBox.setItemText(0, _translate("Form", "江森辉"))
        self.comboBox.setItemText(1, _translate("Form", "陈巧娜"))
        self.pushButton.setText(_translate("Form", "点我开始"))



