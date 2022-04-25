#coding:UTF-8
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,QPlainTextEdit,QMessageBox,QWidget
import os
from multiprocessing import Process

class Stats:

    def __init__(self):
        # 从文件中加载UI定义
        self.ui = uic.loadUi("test.ui")

        self.ui.pushButton.clicked.connect(self.task)  # handleCalc)
        self.ui.pushButton_2.clicked.connect(slot_btn_function_1)



    def task(self):
        a = "python arg1.py"
        result = os.popen(a)
        # print(result.read(),type(result))
        res = result.read()
        print(type(res))
        print(len(res))
        # for line in res.splitlines():
        #     self.textBrowser.append(line)
        #     print(line)
        self.ui.textBrowser.append(res)
        self.ui.textBrowser.ensureCursorVisible()


    def handleCalc(self):
        # _thread.start_new_thread(self.task(),())
        p = Process(target=self.task(),args=())
        p.start()





class Second(QWidget):
    def __init__(self):
        super(Second, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(500, 350)  # 设置第二个窗口代码
        self.setWindowTitle('Second Ui')  # 设置第二个窗口标题
        self.btn = QPushButton('jump', self)  # 设置按钮和按钮名称
        self.btn.setGeometry(150, 150, 100, 50)  # 前面是按钮左上角坐标，后面是按钮大小
        self.btn.clicked.connect(slot_btn_function_2)  # 将信号连接到槽

def slot_btn_function_1():
    stats.ui.hide()  # 隐藏此窗口
    second.show()  # 将第2个窗口显示出来

def slot_btn_function_2():
    second.hide()  # 隐藏此窗口
    stats.ui.show()  # 经第1个窗口显示出来


app = QApplication([])
stats = Stats()
second = Second()
stats.ui.show()

app.exec_()
