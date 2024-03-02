import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat3.jpg')

img=cv.resize(img,(500,300),interpolation=cv.INTER_AREA)
cv.imshow('Cat',img)


average=cv.blur(img,(3,3))
cv.imshow('Average blur',average)

gauss=cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian blur',gauss)

median=cv.medianBlur(img,3)
cv.imshow('Median blur',median)

bilateral = cv.bilateralFilter(img,10,35,25)
cv.imshow('Bilateral',bilateral)


cv.waitKey(0)