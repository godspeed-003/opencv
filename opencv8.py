"""
This script tries to recognize eyes on your face.
Author: Vedant Korade
"""

import cv2

cam = cv2.VideoCapture(1)  # Start webcam capture
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Add image preprocessing
    gray = cv2.equalizeHist(gray)  # Improve contrast
    gray = cv2.GaussianBlur(gray, (5, 5), 0)  # Reduce noise
    faces = face_cascade.detectMultiScale(
    gray, 
    scaleFactor=1.4,
    minNeighbors=6,  
    minSize=(100, 100))
    faces = [f for f in faces if f[2] > 50 and f[3] > 50]
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        #Region Of Interest
        eyes = eye_cascade.detectMultiScale(
        roi_gray, 
        scaleFactor=1.4,
        minNeighbors=4,
        minSize=(40, 40))
        eyes = [e for e in eyes if e[2] > 10 and e[3] > 10]
        for(ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 5)

    cv2.imshow('Webcam', frame)
    #print(cam.get(3)) #640
    #print(cam.get(4)) #480
    # Break the loop if the spacebar is pressed
    if cv2.waitKey(1) == ord(' '):
        break

cam.release()
cv2.destroyAllWindows()
