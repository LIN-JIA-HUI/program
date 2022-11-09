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
from cgitb import reset #合
import numpy as np #合
import matplotlib.pyplot as plt #合

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow_controller, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.show_viedo)
        self.ui.pushButton.clicked.connect(self.videoButton)
        self.ui.pushButton_2.clicked.connect(self.grayhairButton)
        # self.ui.pushButton_3.clicked.connect(self.photoButton)
        self.cap_video=0
        self.flag = 0
        self.img = []
    
    def videoButton(self):
        if (self.flag == 0):
            self.cap_video = cv2.VideoCapture('http://192.168.38.74:4747/mjpegfeed')
            self.timer.start(5);
            self.flag+=1
            self.ui.pushButton.setText("Close")
        else:
            self.timer.stop()
            self.cap_video.release()
            self.ui.image.clear()
            self.ui.pushButton.setText("Continue")
            self.flag=0
    
    #拍照
    # def photoButton(self):
    #     thresh= 120
    #     maxval= 255
    #     def window (name):
    #         cv2.namedWindow(name,cv2.WINDOW_NORMAL)
    #     if (self.flag == 1):
    #         ret, frame = self.cap_video.read()
    #         cv2.imwrite('photo.jpg',frame)
    #         img = cv2.imread("mypict.jpg")
    #         thresh= 120
    #         maxval=255
    #         window("photo")
    #         cv2.imshow("photo",frame)
    
    #白頭髮 #合
    def grayhairButton(self):
        thresh= 120
        maxval= 255
        def window (name):
            cv2.namedWindow(name,cv2.WINDOW_NORMAL)
        if (self.flag == 1):
            ret, frame = self.cap_video.read()
            #cv2.imshow('output',frame)
            cv2.imwrite('mypict.jpg',frame)
            #cv2.destroyWindow('output')
            img = cv2.imread("mypict.jpg")
            thresh= 120
            maxval=255
            window("gray_hair")
            window("gray_hair_region")
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret,dst=cv2.threshold(img_gray,thresh,maxval,cv2.THRESH_BINARY)
            contours,hierarchy=cv2.findContours(dst,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
            image_copy = img.copy()
            cv2.drawContours(image_copy, contours, -1, (0, 255, 0),2, cv2.LINE_AA)
            cv2.imshow("gray_hair",dst)
            cv2.imshow("gray_hair_region",image_copy)

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