import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat3.jpg')

img=cv.resize(img,(500,300),interpolation=cv.INTER_AREA)
cv.imshow('Cat',img)

blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank',blank)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# gray=cv.GaussianBlur(gray,(3,3),cv.BORDER_DEFAULT)


canny=cv.Canny(gray,125,175)
cv.imshow('Canny Edges',canny)

# ret,thresh= cv.threshold(gray,125,255,cv.THRESH_BINARY)
# cv.imshow("thresh",thresh)

contours,hierarchies = cv.findContours(canny, cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')

cv.drawContours(img,contours,-1,(0,0,255),1)
cv.imshow('Contour Blank',img)

cv.waitKey(0)
