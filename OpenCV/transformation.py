import cv2 as cv
import numpy as np
img = cv.imread('Photos/oggy_photo.jpg')

img=cv.resize(img,(500,300),interpolation=cv.INTER_AREA)
cv.imshow('Cat',img)

def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

translated=translate(img,100,100)
cv.imshow('Translated',translated)

def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions)

rotated=rotate(img,-45)
cv.imshow('rotated',rotated)

flip=cv.flip(img,-1)
cv.imshow('Flip',flip)

cropped=img[200:300,100:300]
cv.imshow('Cropped',cropped)





cv.waitKey(0)
