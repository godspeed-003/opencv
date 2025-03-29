"""
This program matches a part of image with original image.
Author: Vedant Korade
"""

import numpy as np
import cv2

img = cv2.resize(cv2.imread('assets/soccer_practice.jpg', 0), (0, 0), fx=0.6, fy=0.6)
template = cv2.resize(cv2.imread('assets/shoe.PNG', 0), (0, 0), fx=0.6, fy=0.6)
height,width = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
#1 and 3 method doesn't work
for method in methods:
    img2 = img.copy()
    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    location = (0, 0)
    if method in [cv2.TM_SQDIFF_NORMED, cv2.TM_SQDIFF]:
        location = min_loc
    else:
        location = max_loc
    
    bottom_right = (location[0] + width, location[1] + height)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()