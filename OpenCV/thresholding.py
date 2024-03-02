import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('Photos/cat3.jpg')

img=cv.resize(img,(500,300),interpolation=cv.INTER_AREA)
cv.imshow('Cat',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

_,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('Simple Threshold',thresh)

_,thresh_inv=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Simple INVERSE Threshold',thresh_inv)


_,thresh_trunc=cv.threshold(gray,150,255,cv.THRESH_TRUNC)
cv.imshow('Truncated Threshold',thresh_trunc)


#Adaptive thresholding
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive Thresholding',adaptive_thresh)


cv.waitKey(0)