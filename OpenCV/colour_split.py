import cv2 as cv
import numpy as np

img = cv.imread('Photos/oggy_photo.jpg')

cv.imshow('Oggy',img)
blank=np.zeros(img.shape[:2],dtype='uint8')


b,g,r=cv.split(img)
blue=cv.merge([b,blank,blank])
cv.imshow('blueimg',blue)

cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)


cv.waitKey(0)