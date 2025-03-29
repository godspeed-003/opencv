"""
This script does something useful.
Author: Vedant Korade
"""

import cv2

cam = cv2.VideoCapture(1)  # Start webcam capture, may be 0 or 1 depending on the system

while True:
    ret, frame = cam.read()
    if not ret:
        break

    cv2.imshow('Webcam', frame)
    #print(cam.get(3)) #640
    #print(cam.get(4)) #480
    # Break the loop if the spacebar is pressed
    if cv2.waitKey(1) == ord(' '):
        break

cam.release()
cv2.destroyAllWindows()
