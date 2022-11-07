import time, sys
from PyQt5 import QtWidgets, QtGui, QtCore, QtMultimediaWidgets
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtMultimedia import (QCameraInfo, QCamera, QCameraImageCapture, QImageEncoderSettings, QMultimedia, QCameraViewfinderSettings, QVideoFrame, QSound)
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
import cv2
from cv2 import VideoCapture
from UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow_controller, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.show_viedo)
        self.ui.pushButton.clicked.connect(self.videoButton)
        #self.ui.photo_Button.clicked.connect(self.photoButton)
        self.cap_video=0
        self.flag = 0
        self.img = []

        

        # self.camera = None  # QCamera对象
        # cameras = QCameraInfo.availableCameras()
        # if len(cameras) > 0:
        #     self.__iniCamera()  # 初始化鏡頭
        #     self.__iniImageCapture()  # 初始化靜態畫圖
        #     self.camera.start()

    def videoButton(self):
        if (self.flag == 0):
            self.cap_video = cv2.VideoCapture('http://192.168.158.244:4747/mjpegfeed')
            self.timer.start(5);
            self.flag+=1
            self.ui.pushButton.setText("Close")
        else:
            self.timer.stop()
            self.cap_video.release()
            self.ui.image.clear()
            self.ui.pushButton.setText("Continue")
            self.flag=0
    def show_viedo(self):
        ret, self.img = self.cap_video.read()
        if ret:
            self.show_cv_img(self.img)
    def show_cv_img(self, img):
        shrink = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #將BGR格式轉為RGB格式
        QtImg = QtGui.QImage(shrink.data,
                              shrink.shape[1],
                              shrink.shape[0],
                              shrink.shape[1] * 3,
                             QtGui.QImage.Format_RGB888) #The image is stored using a 24-bit RGB format (8-8-8).
        jpg_out = QtGui.QPixmap(QtImg).scaled(
             self.ui.image.width(), self.ui.image.height())
        self.ui.image.setPixmap(jpg_out)