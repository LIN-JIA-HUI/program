from cgitb import reset
import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

# def text(font):
#     cv2.putText(ori,'white hair', (10,30),font,0.8,(255,0,0),2)
# cv2.resizeWindow("res1", 500, 500) 

# font = cv2.FONT_HERSHEY_SIMPLEX
# if __name__ == '__main__':

#     parse = argparse.ArgumentParser()
#     parse.add_argument('-i', '--imgpath', default='picture/2.jpg', help='Input image')
#     parse.add_argument('-o', '--output', default='', help='Output image')
#     parse.add_argument('--model', default='models/79999_iter.pth', help='model path')
#     parse.add_argument('--color', default='230,50,20', type=str, help='set bgr colors to change')
#     parse.add_argument('--show', default=1, type=int, help='Show picture')

#     args = parse.parse_args()
# 鏡頭
# vid = cv2.VideoCapture('http://192.168.1.117:4747/mjpegfeed') # /video
# # cv2.namedWindow(cv2.WINDOW_NORMAL)
# while (vid.isOpened()):

#     # Capture the video frame
#     # by frame
#     ret, frame = vid.read()
#     cv2.imshow('output',frame)
#     # Display the resulting frame

#     c=cv2.waitKey(1)
#     if c == 13: #enter button
#         cv2.imwrite('mypict.jpg',frame)
#         break
#     if c==27: # esc button
#         break
#     # the 'q' button is set as the
#     # quitting button you may use any
#     # desired button of your choice
#     # if cv2.waitKey(0) & 0xFF == ord('q'):
#     # 	break
# vid.release()
# cv2.destroyWindow('output')
    # img = cv2.imread('mypict.jpg')
    # thresh= 150
    # maxval=255
    # cv2.namedWindow("gray_hair",cv2.WINDOW_NORMAL)
    # cv2.namedWindow("gray_hair_region",cv2.WINDOW_NORMAL)

    # 取高斯平滑
    # img = cv2.GaussianBlur(img, (3, 3), 0)
    # kernel = np.ones((3,3), np.uint8)
    # erosion = cv2.erode(img, kernel, iterations = 1)
    # img_gray = cv2.cvtColor(erosion, cv2.COLOR_BGR2GRAY)
    # ret,dst=cv2.threshold(img_gray,thresh,maxval,cv2.THRESH_BINARY)
    # contours,hierarchy=cv2.findContours(dst,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    # image_copy = img.copy()
    # cv2.drawContours(image_copy, contours, -1, (0, 255, 0),2, cv2.LINE_AA)
    # cv2.imshow("gray_hair",dst)
    # cv2.imshow("gray_hair_region",image_copy)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

img=cv2.imread('picture/10.png')  #mypict.jpg
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# lower_gray=np.array([0, 0, 135])
# upper_gray=np.array([180, 18, 243])
lower_gray=np.array([0, 0, 40])
upper_gray=np.array([180, 18, 230])
mask = cv2.inRange(hsv, lower_gray, upper_gray)
res = cv2.bitwise_and(img, img, mask=mask)

# kernel = np.ones((3,3), np.uint8)
# erosion = cv2.erode(img, kernel, iterations = 1)
# img_gray = cv2.cvtColor(erosion, cv2.COLOR_BGR2GRAY)
# ret,dst=cv2.threshold(img_gray,thresh,maxval,cv2.THRESH_BINARY)

# blur_img = cv2.GaussianBlur(erosion,(0,0),25)
# usm =cv2.addWeighted(img,1.5,blur_img,-0.5,0)
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# lower_gray=np.array([0, 0, 135])
# upper_gray=np.array([180, 18, 243])
# mask = cv2.inRange(hsv, lower_gray, upper_gray)
# res = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('Input',img)
cv2.imshow('Result', res)
# cv2.imshow("plus",plus)
cv2.waitKey(0)
cv2.destroyAllWindows()