"""
This script does something useful.
Author: Vedant Korade
"""

import cv2

img1 = cv2.imread('assets/1.jpg')
img2 = cv2.imread('assets/2.jpg', -1)
img3 = cv2.imread('assets/3.jpg' , 0)
newimg1 = cv2.imread('assets/file.png', cv2.IMREAD_UNCHANGED)
# Convert to RGB (remove alpha channel)
#rgb_img = cv2.cvtColor(newimg1, cv2.COLOR_BGRA2BGR)

# Save as non-transparent file
#cv2.imwrite('no_tr.jpg', rgb_img)

cv2.namedWindow('Image', cv2.WINDOW_GUI_NORMAL)
img1 = cv2.rotate(img1, cv2.ROTATE_180)
img1 = cv2.resize(img1, (0,00), fx=0.33, fy=0.25)
cv2.imwrite('img1_v2.png', img1)
# Display images
cv2.imshow('Image', img1)
cv2.waitKey(1000)
cv2.imshow('Image', newimg1)
cv2.waitKey(1000)
cv2.imshow('Image', img2)
cv2.waitKey(1000)
cv2.imshow('Image', img3)
cv2.waitKey(1000)

cv2.destroyAllWindows()


