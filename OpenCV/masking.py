import cv2
import numpy as np

image = cv2.imread('Photos/oggy_photo.jpg')

lower_range = np.array([0,0,0])
upper_range = np.array([100,100,255])

mask = cv2.inRange(image,lower_range,upper_range)
cv2.imshow("mask",mask)
result = cv2.bitwise_and(image,image,mask=mask)

cv2.imshow("Result",result)
cv2.waitKey(0)
cv2.destroyAllWindows()