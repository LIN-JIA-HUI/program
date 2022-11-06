from cgitb import reset
import cv2
import numpy as np
import matplotlib.pyplot as plt

def window (name):
    cv2.namedWindow(name,cv2.WINDOW_NORMAL)
# def thresholding(img):
#     thresh=130
#     maxval=255
#     ret,thresh=cv2.threshold(img,thresh,maxval,cv2.THRESH_BINARY)
# def text(font):
#     cv2.putText(ori,'white hair', (10,30),font,0.8,(255,0,0),2)
# cv2.resizeWindow("res1", 500, 500) 

# ori = cv2.imread("7.jpg")
# img_gray = cv2.cvtColor(ori, cv2.COLOR_BGR2GRAY)
# font = cv2.FONT_HERSHEY_SIMPLEX

# res1 = cv2.add(ori,ori)
# res2 = ori +ori+ori

# 二分值
thresh= 120
maxval=255

# 鏡頭
vid = cv2.VideoCapture('http://192.168.8.106:4747/mjpegfeed') # /video
# cv2.namedWindow(cv2.WINDOW_NORMAL)
while (vid.isOpened()):
	
	# Capture the video frame
	# by frame
	ret, frame = vid.read()
	cv2.imshow('output',frame)
	# Display the resulting frame
    
	c=cv2.waitKey(1)
	if c == 13:
		cv2.imwrite('mypict.jpg',frame)
		break
		# #自適應閾值
		# dst_mean = cv2.adaptiveThreshold(img,maxval,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,5)
		# dst_gauss=cv2.adaptiveThreshold(img,maxval,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,-1)
		# cv2.imshow('adaptiveThreshold',dst_mean)
		# cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C",dst_gauss)
	if c==27:
		break
	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
	# if cv2.waitKey(0) & 0xFF == ord('q'):
	# 	break
vid.release()
cv2.destroyWindow('output')
img = cv2.imread("mypict.jpg")
thresh= 120
maxval=255
window("dst")
window("image_copy")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,dst=cv2.threshold(img_gray,thresh,maxval,cv2.THRESH_BINARY)
contours,hierarchy=cv2.findContours(dst,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
image_copy = img.copy()
cv2.drawContours(image_copy, contours, -1, (0, 255, 0),2, cv2.LINE_AA)
cv2.imshow("dst",dst)
cv2.imshow("image_copy",image_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
# cv2.imwrite('dst.jpg',dst)
# cv2.imwrite('image_copy.jpg',image_copy)

# ret,mask1=cv2.threshold(img_gray,thresh,maxval,cv2.THRESH_BINARY)
# maskcolor = cv2.cvtColor(mask1)
# res1 = cv2.add(ori,mask1)
# print(f"threshold={ret}")
# ori = cv2.bitwise_and(ori,ori,mask = mask1)
# img = cv2.bitwise_and(img,img,mask = mask1)
# cv2.addWeighted(ori,)

# cv2.waitKey(0)
# cv2.destroyAllWindows()