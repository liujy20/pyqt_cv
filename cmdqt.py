from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit,QMessageBox,QFileDialog
import os
import threading
import _thread
from multiprocessing import Process
import pyWinhook


class Detect:

    mp4Path = ""
    jpgPath = ""
    weightPath = ""


    def __init__(self):
        # 从文件中加载UI定义
        self.ui = uic.loadUi("cmdqt.ui")

        self.ui.getMp4Path.clicked.connect(self.clk)
        self.ui.getJpgPath.clicked.connect(self.clk2)
        self.ui.detect.clicked.connect(self.clk3)

    def clk(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self.ui,  # 父窗口对象
            "选择视频路径",  # 标题
            r"C:/Users/LIUJY/Desktop/yolo/yolov5-5.0/acv",  # 起始目录
            "图片类型 (*.png *.jpg *.mp4)"  # 选择类型过滤项，过滤内容在括号中
        )
        self.mp4Path = filePath
        self.ui.lineEdit.setText(self.mp4Path)

    def clk2(self):
        filePath = QFileDialog.getExistingDirectory(self.ui, "选择图片保存路径")
        self.jpgPath = filePath
        self.ui.lineEdit_2.setText(self.jpgPath)
        # QMessageBox.about(self.ui,'统计结果',self.filepath)

    def clk3(self):
        # _thread.start_new_thread(self.task(),())
        p = Process(target=self.task(),args=())
        p.start()

    def task(self):
        os.system("start /B python C:/Users/LIUJY/Desktop/yolo/yolov5-5.0/acv/cv.py  "
                  "--file_name " + self.mp4Path +
                  " --save_file " + self.jpgPath)



if __name__ == "__main__":
    app = QApplication([])
    detect = Detect()
    detect.ui.show()



    app.exec_()

