from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog
import cv2

from cv2 import VideoCapture

from UI import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow_controller, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.show_viedo)
        self.ui.pushButton.clicked.connect(self.videoButton)
        self.ui.label.setText('image')
        self.ui.pushButton.setText('video')
        self.cap_video=0
        self.flag = 0
        self.img = []

    def videoButton(self):
        if (self.flag == 0):
            self.cap_video = cv2.VideoCapture('http://192.168.221.242:4747/mjpegfeed')
            self.timer.start(5);
            self.flag+=1
            self.ui.pushButton.setText("Close")
        else:
            self.timer.stop()
            self.cap_video.release()
            self.ui.label.clear()
            self.ui.pushButton.setText("Open")
            self.flag=0
    def show_viedo(self):
        ret, self.img = self.cap_video.read()
        if ret:
            self.show_cv_img(self.img)
    def show_cv_img(self, img):
        shrink = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        QtImg = QtGui.QImage(shrink.data,
                             shrink.shape[1],
                             shrink.shape[0],
                             shrink.shape[1] * 3,
                             QtGui.QImage.Format_RGB888)
        jpg_out = QtGui.QPixmap(QtImg).scaled(
            self.ui.label.width(), self.ui.label.height())

        self.ui.label.setPixmap(jpg_out)


    # def setup_control(self):
    #     # TODO
    #     # self.ui.pushButton.setText('Print message!')
    #     # self.clicked_counter = 0
    #     self.ui.button_line.clicked.connect(self.buttonClicked_line)
    #     self.ui.button_text.clicked.connect(self.buttonClicked_text)
    #     self.ui.button_plain.clicked.connect(self.buttonClicked_plain)
    # def buttonClicked_line(self):
    #     msg = self.ui.box_line.text()
    #     self.ui.label_line.setText(msg)
    # def buttonClicked_text(self):
    #     msg = self.ui.box_text.toPlainText()
    #     self.ui.label_text.setText(msg)
    # def buttonClicked_plain(self):
    #     msg = self.ui.box_plain.toPlainText()
    #     self.ui.label_plain.setText(msg)

    # def buttonClicked(self):
    #     msg = self.ui.f2.text()
    #     self.ui.f1.setText(msg)
        # self.clicked_counter += 1
        # print(f"You clicked {self.clicked_counter} times.")