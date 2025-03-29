"""
This script does something useful.
Author: Vedant Korade
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    #return if we can access cam(nobody using it), image itself in np array
    width = int(cap.get(3))
    height = int(cap.get(4))

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, :width//2] = cv2.flip(smaller_frame, 1)
    image[:height//2, width//2:] = cv2.flip(cv2.rotate(smaller_frame, cv2.ROTATE_180), 1)
    image[height//2:, width//2:] = smaller_frame

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord(' '):  # Check if the spacebar is pressed
        break

cap.release()
cv2.destroyAllWindows()