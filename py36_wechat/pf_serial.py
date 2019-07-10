import serial
import time
from serialui import Ui_Form
from PyQt5 import QtWidgets

serial_in=''

def main():
    baud_rate = 9600  # whatever baudrate you are listening to
    com_port1 = 'COM1'  # replace with your first com port path


    ComRead_timeout = 0.01 # Read timeout to avoid waiting while there is no data on the buffer
    ComWr_timeout = 0.005     # Write timeout to avoid waiting in case of write error on the serial port

    #log = open('log.txt', 'a+')     # Open our log file, to put read data

    listener = serial.Serial(com_port1, baud_rate, timeout=ComRead_timeout,
                         write_timeout=ComWr_timeout)

    while 1:
        while (listener.inWaiting()):
            serial_out = listener.readline()
            print(serial_out)
            readflag=b'\x1aV'
            if serial_out == readflag:
                print('start check')
                # time.sleep(0.05)
                serial_in='WELLCOM_JZT-998AFC-V50_V1.0.0.0_A_C_For_ZJNX[20170208]'
                print(serial_in)
                for char in serial_in:
                    #print(char.encode('utf-8'))
                    listener.write(char.encode('utf-8'))
                # listener.close()
                # listener.open()
            else:
                print('check finger')
                # serial_in='0090000003727028831:00;401401<082:19<0070<;<29401>07:562<00209:261<01012;8:180141?9?;2000007<9<9401250<8>2801614=112411=0:2232010608>599<1131008:1410?0:=?;2011:0819;:810;0:=0=:011;061:028208079;12820603>022<21=0404;182120<0;?10211091<5943030670;2831;0700;943160=0?11040>0<1>3:44090801:2;9<0113>'
                # serial_in='008;0000016432:8811:007>02<00<0<6=2100120>5?7:00150684::80090?=9<:80110661028117058942<1040<0:8:01060987<:01040:7811020:08071:42060==629421=086952820?0?7;::82051161:9<21;0:>0>2021008690103120>0019030517704:830<0;8069030514827:03000?609:43160:=:<2431205711:840;066542<40>0;=>6904130:<6'
                #胡旭江
                #serial_in='00540000036752:8830>004<02801008:219400850>3<:400912=2<:000<19><0:010;13843201052:046101043?8>6202000<=;;1421808>>3:830:0;6;42431006867203030866;:831509><;904090:01;4210009?5'
                #王迪
                #serial_in='00680000016032>88013009401400=0==:52001=0<6;7240170<7?;2000>0=711:8111098=6:01000>669:<1170986:241080?=>?201180=7409420<06694982180>><5242080<7489020>0<>192<21006>7?:<20=07740:8310087;4:83070>>:;2030=0574<2830?0725'
                #徐华栋
                #serial_in='00810000036<36488417003?02400:28;?51<00509415:000;1;;3<2<0150540>9001307;;3:01160;5<41<10<134>4:410?08098201093<<389<119070?<1<10724984:42030?54=282160567?:<20>0<=759<30?0;5;5:831506=782<31209=0;143150;10=:83010<8?0:0400047412<40;0<=:1205120:5?1:05190901;:21<1097?'
                #江森辉
                #serial_in='004:0000015?1>88860=007802800;086>42800<08>551801308895:40020<038:80000;69<2<012087;0:420106>5;:820<05717:430<0570:203000901?203000:7712840209>37244080<21'
                # 陈巧娜
                #serial_in='00;7000003723>:88121000:0240130<234:<01511=>5200050;=982<00816:99:801819330:<10>2?5511<10;22531:01090<4<2:410=21;43181150><359411709;56:01000;<3914106265199810;09<=<2010754:2?1410415<2?281120:<=0:02190<<93942160>9849420210=?62<20<0==>6:420:0?6989820;1762<2020;107<390305125<6:0318078371030109=::243110:=6<903190=69?1830;0767:2440=0=66;9<4180876=20401080252?1000=<6<9810607'
                for char in serial_in:
                    listener.write(char.encode("utf-8"))
                print (time.asctime(time.localtime(time.time()) )  + '\tcheck finish')
                listener.close()
                listener.open()

def BrushPhoto(text):
    if text == "0":
        serial_in = '004:0000015?1>88860=007802800;086>42800<08>551801308895:40020<038:80000;69<2<012087;0:420106>5;:820<05717:430<0570:203000901?203000:7712840209>37244080<21'
    elif text == "1":
        serial_in='00;7000003723>:88121000:0240130<234:<01511=>5200050;=982<00816:99:801819330:<10>2?5511<10;22531:01090<4<2:410=21;43181150><359411709;56:01000;<3914106265199810;09<=<2010754:2?1410415<2?281120:<=0:02190<<93942160>9849420210=?62<20<0==>6:420:0?6989820;1762<2020;107<390305125<6:0318078371030109=::243110:=6<903190=69?1830;0767:2440=0=66;9<4180876=20401080252?1000=<6<9810607'

class mywindow(QtWidgets.QWidget):
    def __init__(self):
        super(mywindow, self).__init__()
        self.new = Ui_Form()
        self.new.setupUi(self)
        self.comboBox.activated[str].connect(BrushPhoto)
        self.new.pushButton.clicked.connect(main())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


