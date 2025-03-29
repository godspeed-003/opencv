"""
This script does something useful.
Author: Vedant Korade
"""

import numpy as np
import cv2

img = cv2.imread('assets/chessboard.png')
#(0, 0) tells OpenCV to calculate the output size based on the scaling factors fx and fy
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                                #img, no of best corner, quality level [0-1], min euclidean distance between corners
                                #euclidean distance = sqrt(dx^2 + dy^2) ie direct line joining them
corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int_(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img, (x,y), 5, (0, 0, 255), -1)

for i in range(len(corners)):
    for j in range(len(corners)):
        if i != j:
            corner1 = tuple(corners[i][0])
            corner2 = tuple(corners[j][0])
            color = tuple(int(x) for x in np.random.randint(0, 256, size=3))            
            cv2.line(img, corner1, corner2, color, 1)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()