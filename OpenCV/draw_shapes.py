import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')
# cv.imshow('Blank',blank)

# blank[200:350,300:400]= 0,255,0 
# cv.imshow('Green',blank)

cv.rectangle(blank,(50,50),(300,250),(0,255,0),thickness=-1)
cv.imshow('Rectangle',blank)
cv.circle(blank,(250,250),40,(0,0,255),thickness=3)
cv.imshow('Circle',blank)
cv.line(blank,(0,0),(235,435),(255,0,0),thickness=3)
cv.imshow('Line',blank)

cv.putText(blank,'Hello I am Aryan',(30,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,0,0),2)
cv.imshow('text',blank)
cv.waitKey(0)
cv.destroyAllWindows()