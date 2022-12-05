import time, sys
import os
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QImage, QPixmap, QFont
from PyQt5.QtWidgets import QFileDialog, QToolTip, QColorDialog
import cv2
from cv2 import VideoCapture
from UI import Ui_MainWindow
from cgitb import reset #合
import numpy as np #合
import matplotlib.pyplot as plt #合
from PyQt5.QtWebEngineWidgets import *
#import qdarkstyle

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow_controller, self).__init__()
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        uic.loadUi('CameraWin.ui', self)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.show_viedo)
        self.bStart.clicked.connect(self.showVideo) #鏡頭
        self.bGrayHair.clicked.connect(self.grayHairAna) #白髮分析
        self.bPhoto.clicked.connect(self.takePhoto) #拍照
        self.comboBox.addItems(["長髮整理", "中長髮整理", "短髮整理", "男生髮型整理", "其他"])
        self.bColor.clicked.connect(self.chooseColor) #調整髮色、唇色
        # self.ui.comboBox.setCurrentIndex.connect(self.selectionchange)
        self.image.setToolTip('手機鏡頭畫面')
        self.photo.setToolTip('照片顯示於此')
        self.bPhoto.setToolTip('拍照並儲存照片')
        self.bGrayHair.setToolTip('分析白頭髮區域')
        self.bColor.setToolTip('使用調色盤選擇髮色及唇色')
        self.cap_video=0
        self.flag = 0
        self.img = []
        QToolTip.setFont(QFont('SansSerif', 10))
        #setup style sheet
        #self.ui.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5()) #介面改為黑色

    #連接手機相機
    def showVideo(self):
        if (self.flag == 0):
            # self.ui.bStart.setToolTip('關閉相機')
            self.cap_video = cv2.VideoCapture('http://192.168.252.2:4747/mjpegfeed')
            self.timer.start(5);
            self.flag+=1
            self.bStart.setText("Close")
        # elif (self.flag == 1):
        #     ret, frame = self.cap_video.read()
        #     cv2.imwrite('photo.jpg',frame)
        #     #cv2.imshow('photo.jpg', frame)
        #     self.ui.bStart.setText("Close")
        #     self.flag+=1
        else:
            self.timer.stop()
            self.cap_video.release()
            self.image.clear()
            self.bStart.setText("Continue")
            self.flag=0

    #拍照
    def takePhoto(self):
        thresh= 120
        maxval= 255
        #def window (name):
            #cv2.namedWindow(name,cv2.WINDOW_NORMAL)
        if (self.flag == 1):
            ret, frame = self.cap_video.read()
            cv2.imwrite('photo.jpg',frame)
            img = cv2.imread("photo.jpg")
            thresh= 120
            maxval=255
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # 改為 RGB
            height, width, channel = frame.shape
            bytesPerline = channel * width
            img = QImage(frame, width, height, bytesPerline, QImage.Format_RGB888)
            self.photo.setPixmap(QPixmap.fromImage(img))   # 顯示圖片
            #window("photo")
            #cv2.imshow("photo",frame)
            #self.ui.image.setPixmap(QPixmap.fromImage(img))
        # else:
        #     self.ui.bPhoto.setToolTip('拍照')
    
    #白頭髮 #合
    def grayHairAna(self):
        thresh= 120
        maxval= 255
        if (self.flag == 1):
            #ret, frame = self.cap_video.read()
            #cv2.imshow('output',frame)
            #cv2.imwrite('photo.jpg')
            #cv2.destroyWindow('output')
            sc = self.selectedColor
            os.system(f'python makeup.py -i photo.jpg --color {sc[2]},{sc[1]},{sc[0]}')
            # img = cv2.imread("photo.jpg")
            # thresh= 120
            # maxval=255
            # cv2.namedWindow("gray_hair", cv2.WINDOW_NORMAL)
            # cv2.namedWindow("gray_hair_region", cv2.WINDOW_NORMAL)
            # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # ret,dst=cv2.threshold(img_gray,thresh,maxval,cv2.THRESH_BINARY)
            # contours,hierarchy=cv2.findContours(dst,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
            # image_copy = img.copy()
            # cv2.drawContours(image_copy, contours, -1, (0, 255, 0),2, cv2.LINE_AA)
            # cv2.imshow("gray_hair",dst)
            # cv2.imshow("gray_hair_region",image_copy)

    #整理方法建議
    @pyqtSlot()
    def selectionchange(self):
        Form = QtWidgets.QWidget()
        Form.setWindowTitle('整理方法建議')
        self.browser = QWebEngineView()
        # self.ui.comboBox.
        self.browser.load(QtCore.QUrl('https://www.youtube.com/results?search_query=%E9%95%B7%E9%AB%AE%E6%95%B4%E7%90%86'))
        self.browser.show()

    def chooseColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            print(color.name())
            print(color.red(), color.green(), color.blue())
            r, g, b = color.red(), color.green(), color.blue()
            self.selectedColor = [r, g, b]
        # strRGB = ('{:^3d}, {:^3d}, {:^3d}'.format(r, g, b))

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
             self.image.width(), self.image.height())
        self.image.setPixmap(jpg_out)