import time, sys
import os
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap, QFont
from PyQt5.QtWidgets import QFileDialog, QToolTip, QColorDialog, QMainWindow, QApplication
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
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.show_viedo)
        self.lImage.setAlignment(Qt.AlignCenter)
        self.lPhoto.setAlignment(Qt.AlignCenter)
        self.bStart.clicked.connect(self.showVideo) #鏡頭
        self.bGrayHair.clicked.connect(self.grayHairAna) #白髮分析
        self.bPhoto.clicked.connect(self.takePhoto) #拍照
        self.comboBox.currentIndexChanged.connect(self.selectChanged)
        # self.menuactionChoose_Hairstyle.triggered.connect(self.menuselectChanged)
        self.bColor.clicked.connect(self.chooseColor) #調整髮色
        self.actionClose.triggered.connect(exit) #關閉程式
        self.actiontoolbarClose.triggered.connect(exit)
        self.actionOpen.triggered.connect(self.fileOpen) #開啟資料夾選擇照片
        self.actiontoolbarOpen.triggered.connect(self.fileOpen)
        self.actionSave.triggered.connect(self.fileSave) #儲存照片至資料夾
        self.actiontoolbarSave.triggered.connect(self.fileSave)
        self.lImage.setToolTip('手機鏡頭畫面')
        self.lPhoto.setToolTip('照片顯示於此')
        self.bPhoto.setToolTip('拍照並儲存照片')
        self.bGrayHair.setToolTip('分析白頭髮區域')
        self.bColor.setToolTip('使用調色盤選擇髮色')
        self.actionOpen.setStatusTip('開啟資料夾選擇圖片')
        self.actionSave.setStatusTip('儲存照片至資料夾')
        self.actionClose.setStatusTip('選取以關閉視窗')
        self.actionChoose_Color.setStatusTip('使用調色盤選擇髮色')
        self.actionChoose_Photo.setStatusTip('拍照並儲存照片')
        self.actionChoose_GrayHair.setStatusTip('分析白頭髮區域')
        self.actionChoose_Start.setStatusTip('開啟/關閉手機鏡頭')
        self.cap_video=0
        self.flag = 0
        self.img = []
        QToolTip.setFont(QFont('SansSerif', 10))
        #setup style sheet
        #self.ui.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5()) #介面改為黑色

    #整理方法建議
    def selectChanged(self, index):
        sindex = self.comboBox.currentIndex()
        self.browser = QWebEngineView()
        if sindex == 1:
            self.browser.setWindowTitle('長髮整理')
            self.browser.load(QtCore.QUrl('https://www.youtube.com/results?search_query=%E9%95%B7%E9%AB%AE%E6%95%B4%E7%90%86'))
            self.browser.show()
        elif sindex == 2:
            self.browser.setWindowTitle('中長髮整理')
            self.browser.load(QtCore.QUrl('https://www.youtube.com/results?search_query=%E4%B8%AD%E9%95%B7%E9%AB%AE%E6%95%B4%E7%90%86'))
            self.browser.show()
        elif sindex == 3:
            self.browser.setWindowTitle('短髮整理')
            self.browser.load(QtCore.QUrl('https://www.youtube.com/results?search_query=%E7%9F%AD%E9%AB%AE%E6%95%B4%E7%90%86'))
            self.browser.show()
        elif sindex == 4:
            self.browser.setWindowTitle('男生髮型整理')
            self.browser.load(QtCore.QUrl('https://www.youtube.com/results?search_query=%E7%94%B7%E7%94%9F%E9%AB%AE%E5%9E%8B%E6%95%B4%E7%90%86'))
            self.browser.show()
        elif sindex == 5:
            self.browser.setWindowTitle('其他')
            self.browser.load(QtCore.QUrl('https://www.youtube.com/results?search_query=%E9%AB%AE%E5%9E%8B%E6%95%B4%E7%90%86'))
            self.browser.show()
        else:
            pass

    def menuselectChanged(self):
        pass

    #開啟資料夾選擇照片
    def fileOpen(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', 'c:\\Users\melod\Program\OurCam', "Image Files(*.jpg *.png)")
        imagePath = filename[0]
        print(imagePath)
        pixmap = QPixmap(imagePath)
        self.lPhoto.setPixmap(pixmap)
        # self.lPhoto.setScaledContents(True)

    #儲存照片至資料夾    
    def fileSave(self):
        photo = cv2.imread('photo.jpg')
        filename = QFileDialog.getSaveFileName(self, 'Save File', 'c:\\', "Image Files(*.jpg *.png)")
        
    #連接手機相機
    def showVideo(self):
        if (self.flag == 0):
            self.cap_video = cv2.VideoCapture('http://192.168.11.190:4747/mjpegfeed')
            self.timer.start(5);
            self.flag+=1
            self.bStart.setText("Turn\nOff")
        else:
            self.timer.stop()
            self.cap_video.release()
            self.lImage.clear()
            self.bStart.setText("Turn\nOn")
            self.flag=0

    #拍照
    def takePhoto(self):
        # thresh= 120
        # maxval= 255
        #def window (name):
            #cv2.namedWindow(name,cv2.WINDOW_NORMAL)
        if (self.flag == 1):
            ret, frame = self.cap_video.read()
            cv2.imwrite('photo.jpg',frame)
            img = cv2.imread("photo.jpg")
            # thresh= 120
            # maxval=255
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # 改為 RGB
            height, width, channel = frame.shape
            bytesPerline = channel * width
            img = QImage(frame, width, height, bytesPerline, QImage.Format_RGB888)
            self.lPhoto.setPixmap(QPixmap.fromImage(img))   # 顯示圖片
    
    #白頭髮 #合
    def grayHairAna(self):
        thresh= 120
        maxval= 255
        if (self.flag == 1):
            #下面兩行暫時註解掉。
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
             self.lImage.width(), self.lImage.height())
        self.lImage.setPixmap(jpg_out)