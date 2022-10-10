from cgitb import reset
import cv2

ori = cv2.imread("2.png")
img = cv2.imread("2.png",cv2.IMREAD_GRAYSCALE)
img_gray = cv2.cvtColor(ori, cv2.COLOR_BGR2GRAY)
# res1=cv2.add(img,img)

# 二分值
thresh= 50
maxval=255

# # 鏡頭
# vid = cv2.VideoCapture('http://192.168.43.150:4747/mjpegfeed') # /video
# # cv2.namedWindow(cv2.WINDOW_NORMAL)
# while (vid.isOpened()):
	
# 	# Capture the video frame
# 	# by frame
# 	ret, frame = vid.read()
# 	cv2.imshow('output',frame)

# 	# Display the resulting frame
    
# 	# cv2.imshow('output', frame)
# 	# gray_frame = cv2.cvtColor(frame,cv2.COLOR_BAYER_BG2BGR)
# 	# thresh= 52
# 	# maxval=255
# 	# ret,dst=cv2.threshold(gray_frame,thresh,maxval,cv2.THRESH_BINARY)
# 	# cv2.imshow("binary",dst)

# 	c=cv2.waitKey(1)
# 	if c == 13:
# 		cv2.imwrite('mypict.jpg',frame)
# 		img = cv2.imread("mypict.jpg",cv2.IMREAD_GRAYSCALE)
# 		# gray_frame = cv2.cvtColor(img,cv2.COLOR_BAYER_BG2BGR)
# 		#自己設定閾值
# 		thresh= 100
# 		maxval=255
# 		ret,dst=cv2.threshold(img,thresh,maxval,cv2.THRESH_BINARY)
# 		cv2.imshow('original',frame)
# 		cv2.imshow("binary",dst)
# 		#自適應閾值
# 		dst_mean = cv2.adaptiveThreshold(img,maxval,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,5)
# 		dst_gauss=cv2.adaptiveThreshold(img,maxval,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,-1)
# 		cv2.imshow('adaptiveThreshold',dst_mean)
# 		cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C",dst_gauss)
# 	if c==27:
# 		break
	
# 	# the 'q' button is set as the
# 	# quitting button you may use any
# 	# desired button of your choice
# 	# if cv2.waitKey(0) & 0xFF == ord('q'):
# 	# 	break
# vid.release()
# cv2.destroyAllWindows()

# ret,dst=cv2.threshold(res1,thresh,maxval,cv2.THRESH_BINARY)
ret,mask1=cv2.threshold(img_gray,thresh,maxval,cv2.THRESH_BINARY)
# res1 = cv2.add(ori,mask1)
# print(f"threshold={ret}")
ori = cv2.bitwise_and(ori,ori,mask = mask1)
img = cv2.bitwise_and(img,img,mask = mask1)
# cv2.addWeighted(ori,)
# dst_mean=cv2.adaptiveThreshold(img,maxval,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,-1)
# dst_gauss=cv2.adaptiveThreshold(img,maxval,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,-1)
# ret,dst=cv2.threshold(img,thresh,maxval,cv2.THRESH_BINARY)

cv2.imshow("mask1",ori)
cv2.imshow("mask2",img)
cv2.imshow("gray",img_gray)
# cv2.imshow("res",res1)
# cv2.imshow("gray",img)
# cv2.imshow("add",res1)
# cv2.imshow("thresh_binary",dst)
# for y in range(0,20):
#     for x in range()
# print(f"img = \n{img}")
# cv2.imshow("ADAPTIVE_THRESH_MEAN_C",dst_mean)
# cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C",dst_gauss)
# # cv2.imshow("counterclockwise",dst1)
cv2.waitKey(0)
cv2.destroyAllWindows()