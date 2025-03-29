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
                    #start coordinate[top left], end coordinate[bottom right], BGR colour of line, thickness in pixel
    img = cv2.line(frame, (0,0), (width, height), (0, 0, 255), 5)
    img = cv2.line(img, (0, height), (width,0), (255, 0, 0), 5)
    img = cv2.rectangle(img, (270, 190), (370, 290), (0, 255, 0), 5)
    img = cv2.circle(img, (320, 240), 50, (128, 128, 128), 5)
    font = cv2.FONT_HERSHEY_TRIPLEX    #bottom left hand cornor of text, font, scale, colour, thickness, anti aliasing
    img = cv2.putText(img, "OP_Vedant", (150, 400), font, 1+1, (0, 0, 0), 5, cv2.LINE_AA)
    cv2.imshow('Webcam', img)

    if cv2.waitKey(1) == ord(' '):
        break

cam.release()
cv2.destroyAllWindows()