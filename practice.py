from cgitb import reset
import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

if __name__ == '__main__':

	parse = argparse.ArgumentParser()
	parse.add_argument('-i', '--imgpath', default='picture/2.jpg', help='Input image')
	parse.add_argument('-o', '--output', default='', help='Output image')
	parse.add_argument('--show', default=1, type=int, help='Show picture')

	args = parse.parse_args()
	image_path = args.imgpath

	image=cv2.imread(image_path)
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	lower_gray=np.array([0, 0, 40])
	upper_gray=np.array([180, 18, 230])
	mask = cv2.inRange(hsv, lower_gray, upper_gray)
	res = cv2.bitwise_and(image, image, mask=mask)

	if args.show == 1:
		cv2.imshow("gray_hair",image)
		cv2.imshow("gray_hair_region",res)

		cv2.waitKey(0)
		cv2.destroyAllWindows()

	if args.output != '':
		cv2.imwrite(args.output, image)
	# # 鏡頭
	# vid = cv2.VideoCapture('http://192.168.1.117:4747/mjpegfeed') # /video
	# # cv2.namedWindow(cv2.WINDOW_NORMAL)
	# while (vid.isOpened()):

	# # Capture the video frame
	# # by frame
	# ret, frame = vid.read()
	# cv2.imshow('output',frame)
	# # Display the resulting frame

	# c=cv2.waitKey(1)
	# if c == 13: #enter button
	# 	cv2.imwrite('mypict.jpg',frame)
	# 	break
	# if c==27: # esc button
	# 	break
	# # the 'q' button is set as the
	# # quitting button you may use any
	# # desired button of your choice
	# # if cv2.waitKey(0) & 0xFF == ord('q'):
	# # 	break
	# vid.release()
	# cv2.destroyWindow('output')
	# cv2.namedWindow("gray_hair",cv2.WINDOW_NORMAL)
	# cv2.namedWindow("gray_hair_region",cv2.WINDOW_NORMAL)
