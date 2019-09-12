# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'postinfo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import pandas as pd
from Post import Post


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
        # self.pushButton.clicked.connect(self.textEdit.clear)
        self.pushButton.clicked.connect(self.postinfo)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def showDialog(self):
        #fname = QFileDialog.getOpenFileName(None, "选取文件", '/', "All Files (*);;Excel 文件(*.xls;*.xlsx)")
        fileName_choose, filetype = QFileDialog.getOpenFileName(
            None, "选取文件", '/', "Excel 文件(*.xls;*.xlsx)")

        if fileName_choose == "":
            print("\n取消选择")
            return
        # print("\n你选择的文件为:")
        # print(fileName_choose)
        # print("文件筛选器类型: ", filetype)
        if fileName_choose != "":
            return fileName_choose  # 返回选择文件路径

# 第一个参数必须是self，用于检查电话号码
    def check(self, s):
        if len(str(s)) != 11:
            return False
        elif len(str(s)) == 11 and str(s).strip().startswith('11') is True:
            return False
        elif len(str(s)) == 11 and str(s).strip().startswith('12') is True:
            return False
        elif len(str(s)) == 11 and str(s).strip().startswith('14') is True:
            return False
        elif len(str(s)) == 11 and str(s).strip().startswith('16') is True:
            return False
        elif len(str(s)) == 11 and str(s).strip().startswith('19') is True:
            return False
        else:
            return True

    def read_excel(self):
        excel = self.showDialog()
        # 必须判断返回的值，不能界面会奔溃
        if excel is None:
            return
        if excel is not None:
            phone = []
            info = []
            result = []
            ls = pd.DataFrame(pd.read_excel(excel, header=None))
            #根据电话号码去掉重复行，保留重复行第一行的数据
            lsls=ls.drop_duplicates([0])
            #比较去重前后的行数，如果相等表示没有重复
            number=ls.shape[0]-lsls.shape[0]
            if number>0:
                reply=QMessageBox.warning(
                    None, "警告框", "有%d行电话号码重复！yes：去重发送；no：重新选择" % number, QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Ok:
                    '''ls.shape[0]:取行数；ls[0][i]：第一列的数据'''
                    for i in range(0, ls.shape[0]):
                        print(ls[0][i])
                        if self.check(ls[0][i]) is True:
                            phone.append(str(ls[0][i]))  # 需转化为字符串
                            info.append(ls[1][i])  # 第二列的数据
                        else:
                            QMessageBox.warning(
                                None, "处理结果", "第%d行电话号码错误！" %
                                              (i + 1), )
                            return None
                    result.append(phone)
                    result.append(info[0])
                    return result  # 返回结果列表
                else: return None
            #######################################################################
            if number==0:
                reply=QMessageBox.information(
                    None, "消息框", "总共有%d行信息！请点击yes发送" % ls.shape[0], QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Ok:
                    '''ls.shape[0]:取行数；ls[0][i]：第一列的数据'''
                    for i in range(0, ls.shape[0]):
                        print(ls[0][i])
                        if self.check(ls[0][i]) is True:
                            phone.append(str(ls[0][i]))  # 需转化为字符串
                            info.append(ls[1][i])  # 第二列的数据
                        else:
                            QMessageBox.warning(
                                None, "处理结果", "第%d行电话号码错误！" %
                                              (i + 1), )
                            return None
                    result.append(phone)
                    result.append(info[0])
                    return result  # 返回结果列表
                else: return None

    def postinfo(self):
        listinfo = self.read_excel()
        if listinfo is None:
            return
        if listinfo is not None:
            # print(listinfo)
            response = Post(listinfo)
            # print(response)
            ss = response.split(',')
            s = '\"' + "rspcod" + "\":" + "\"" + "success" + "\""
            if ss[1] == s:
                print("发送成功")
                QMessageBox.information(None,
                                        "处理结果",
                                        "发送完毕，发送成功", )
            else:
                print("发送失败")
                QMessageBox.warning(None,
                                    "处理结果",
                                    "发送完毕，发送失败",)

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
