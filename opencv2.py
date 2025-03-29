"""
This script does something useful.
Author: Vedant Korade
"""

import cv2
import random

img1 = cv2.imread('assets/1.jpg')
img2 = cv2.imread('assets/2.jpg', -1)
img3 = cv2.imread('assets/3.jpg' , 0)
newimg1 = cv2.imread('assets/file.png', cv2.IMREAD_UNCHANGED)

#print(img1)  #BGR 0-255
#print(type(img1))
#print(img1.shape) # (height, width, channels)
#print(img1[0][500])

#for i in range(100): #100 rows
    #for j in range(img1.shape[1]): #all columns
        #img1[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

#cv2.imshow('Image', img1)
#cv2.waitKey(00)
#cv2.destroyAllWindows()
cv2.namedWindow('Image', cv2.WINDOW_GUI_NORMAL)

#start_row:end_row, start_column:end_column
img2part = img2 [400:800,400:800]
img2[100:500,300:700] = img2part

cv2.imshow('Image', img2)
cv2.waitKey(00)
cv2.destroyAllWindows()