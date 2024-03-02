import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow('Gray Person',gray)

    haar_cascade=cv.CascadeClassifier('haar_face.xml')

    faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
    print(f'Number of faces found={len(faces_rect)}')

    for(x,y,w,h) in faces_rect:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)

    cv.imshow('Detected Face',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)