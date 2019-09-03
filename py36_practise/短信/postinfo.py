# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'postinfo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import pandas as pd
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(150, 130, 104, 71))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        #self.pushButton.clicked.connect(self.textEdit.clear)
        self.pushButton.clicked.connect(self.read_excel)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def showDialog(self):
        #fname = QFileDialog.getOpenFileName(None, "选取文件", '/', "All Files (*);;Excel 文件(*.xls;*.xlsx)")
        fileName_choose, filetype = QFileDialog.getOpenFileName(None, "选取文件", '/', "All Files (*);;Excel 文件(*.xls;*.xlsx)")

        # if fileName_choose == "":
        #     print("\n取消选择")
        #     return
        # print("\n你选择的文件为:")
        # print(fileName_choose)
        # print("文件筛选器类型: ", filetype)
        return fileName_choose  #返回选择文件路径
    def read_excel(self):
        excel=self.showDialog()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

