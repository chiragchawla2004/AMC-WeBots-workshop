import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('Photos/group.jpg')

img=cv.resize(img,(300,300),interpolation=cv.INTER_AREA)
cv.imshow('Person',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person',gray)

haar_cascade=cv.CascadeClassifier('haar_face.xml')

faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
print(f'Number of faces found={len(faces_rect)}')

for(x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected Face',img)

cv.waitKey(0)