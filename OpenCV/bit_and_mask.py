import cv2 as cv
import numpy as np

img = cv.imread('Photos/oggy_photo.jpg')
img = cv.resize(img, (400, 300))

# Create a blank image with 3 channels for mask
blank = np.zeros((300, 400, 3), dtype='uint8')

mask = cv.circle(blank, (200, 150), 100, (255, 255, 255), -1)
mask_gray = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
masked_image = cv.bitwise_and(src1=img, src2=img, mask=mask_gray)
cv.imshow('imaage',img)
cv.imshow('mask_gray',mask_gray)
cv.imshow("masked_image", masked_image)
cv.waitKey(0)
cv.destroyAllWindows()
