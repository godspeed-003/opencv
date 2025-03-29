"""
This program detects face.
Author: Vedant Korade
"""

import cv2 as cv

print(cv.__version__)
RED = (0, 0, 255)

img = cv.imread('assets/face.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

path = 'cascades/haarcascade_frontalface_default.xml'
face_detector = cv.CascadeClassifier(path)

face_rects = face_detector.detectMultiScale(gray,
        scaleFactor=1.1,
        minNeighbors=6, 
        minSize=(100, 100),
        flags = cv.CASCADE_SCALE_IMAGE)

print(f'found {len(face_rects)} face(s)')

for rect in face_rects:
    cv.rectangle(img, rect, RED, 2)

cv.imshow('window', img)
cv.waitKey(0)