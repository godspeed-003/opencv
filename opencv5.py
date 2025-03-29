"""
This script does something useful.
Author: Vedant Korade
"""

import numpy as np
import cv2

cam = cv2.VideoCapture(1)

while True:
    ret, frame = cam.read()
    width = int(cam.get(3)) #top left to top right
    height = int(cam.get(4)) #top left to bottom left
    #hsv - hue saturation value & hsl - hue saturation lightness [brightness]
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([90, 50, 50])
    upper = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask = mask)
    cv2.imshow('Webcam', result)

    # Break the loop if the spacebar is pressed
    if cv2.waitKey(1) == ord(' '):
        break

cam.release()
cv2.destroyAllWindows()