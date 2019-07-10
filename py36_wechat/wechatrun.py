#coding=utf8
import itchat
import time
from wechat import Ui_Form
from PyQt5 import QtWidgets

# 自动回复
# 封装好的装饰器，当接收到的消息是Text，即文字消息
@itchat.msg_register('Text')
def text_reply(msg):
    #当消息不是由自己发出的时候
    if not msg['FromUserName'] == itchat.get_friends(update=True)[0]["UserName"]:
        # 发送一条提示给文件助手
        itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %
                        (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
                         msg['User']['NickName'],
                         msg['Text']), 'filehelper')

        #回复给好友
        return u'[自动回复]您好，我现在有事不在，一会再和您联系。\n已经收到您的的信息：%s\n' % (msg['Text'])
def wechat(self):
    itchat.auto_login()
    # 获取自己的UserName
    #myUserName = itchat.get_friends(update=True)[0]["UserName"]
    itchat.run()

class mywindow(QtWidgets.QWidget):
    def __init__(self):
        super(mywindow, self).__init__()
        self.new = Ui_Form()
        self.new.setupUi(self)
        self.new.pushButton.clicked.connect(wechat)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())