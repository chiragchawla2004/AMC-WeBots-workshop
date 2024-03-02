import cv2 as cv
img = cv.imread('Photos/oggy_photo.jpg')
cv.imshow("real_image",img)
img = cv.resize(img,(300,300))

img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("img_gray",img_gray)
# img_gray=cv.GaussianBlur(img_gray,(5,5),3)
# cv.imshow('Gaussian blur',img_gray)

gradients_sobelx = cv.Sobel(img_gray,-1,1,0)
gradients_sobely = cv.Sobel(img_gray,-1,0,1)
gradients_sobelxy = cv.addWeighted(gradients_sobelx,0.5,gradients_sobely,0.5,0)
gradients_laplacian = cv.Laplacian(img_gray,-1)

canny=cv.Canny(img_gray,125,175)
cv.imshow("Sobel X",gradients_sobelx)
cv.imshow("Sobel Y",gradients_sobely)
cv.imshow("Sobel x+y",gradients_sobelxy)
cv.imshow("Laplacian",gradients_laplacian)
cv.imshow("canny edges",canny)

# canny1=cv.Canny(img,125,175)
# cv.imshow("canny1 edges",canny1)
cv.waitKey(0)
cv.destroyAllWindows()



# Noise Reduction
# Gradient calculation
# Non-Maximum Suppression
# Double Thresholding and Edge Tracking by Hysteresis