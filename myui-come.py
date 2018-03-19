# import tkinter
# top = tkinter.Tk()
# # 进入消息循环
# top.mainloop()

# from tkinter import *           # 导入 tkinter 库
# root = Tk()                     # 创建窗口对象的背景色
#                                 # 创建两个列表
# li     = ['C','python','php','html','SQL','java']
# movie  = ['CSS','jQuery','Bootstrap']
# listb  = Listbox(root)          #  创建两个列表组件
# listb2 = Listbox(root)
# button = Button(root,width = 10)
# for item in li:                 # 第一个小部件插入数据
#     listb.insert(0,item)
#
# for item in movie:              # 第二个小部件插入数据
#     listb2.insert(0,item)
#
# listb.pack()                    # 将小部件放置到主窗口中
# listb2.pack()
# button.pack()
# root.mainloop()                 # 进入消息循环
'''
生成一个有close按钮功能的窗口
'''
# import sys
# from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
# from PyQt5.QtCore import QCoreApplication
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#     def initUI(self):
#         qbtn = QPushButton('Quit', self)
#         qbtn.clicked.connect(QCoreApplication.instance().quit)
#         qbtn.resize(qbtn.sizeHint())
#         qbtn.move(50, 50)
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('Quit button')
#         self.show()
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())
'''
继承用pyuic生成的myui.py代码文件，从而来生成窗口
实现代码与界面的分离
小提示：
槽其实就个函数（方法），Qt5中的槽函数不在限定必须是slot，可以是普通的函数、类的普通成员函数、lambda函数等。
编译期间就会检查信号与槽是否存在！信号的connect连接最好放在__init__析构函数里面，这样只会声明一次连接，
如果在类方法（函数中）使用的话，要记得disconnect，否则connect会连接多次，导致程序异常。信号槽函数不用加 ()，
否则可能会导致连接异常
'''
from PyQt5 import QtWidgets
from myui import Ui_Form

class mywindow(QtWidgets.QWidget):
    def __init__(self):
        super(mywindow, self).__init__()
        self.new = Ui_Form()
        self.new.setupUi(self)
        self.new.pushButton.clicked.connect(self.new.textEdit.close) #连接按钮功能

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
