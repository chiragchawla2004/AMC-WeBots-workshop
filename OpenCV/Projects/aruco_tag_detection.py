import numpy as np
import time
import cv2 as cv
from cv2 import aruco
from math import sqrt


ARUCO_DICT = {
	"DICT_4X4_50": aruco.DICT_4X4_50,
	"DICT_4X4_100": aruco.DICT_4X4_100,
	"DICT_4X4_250": aruco.DICT_4X4_250,
	"DICT_4X4_1000":aruco.DICT_4X4_1000,
	"DICT_5X5_50": aruco.DICT_5X5_50,
	"DICT_5X5_100": aruco.DICT_5X5_100,
	"DICT_5X5_250": aruco.DICT_5X5_250,
	"DICT_5X5_1000": aruco.DICT_5X5_1000,
	"DICT_6X6_50": aruco.DICT_6X6_50,
	"DICT_6X6_100": aruco.DICT_6X6_100,
	"DICT_6X6_250": aruco.DICT_6X6_250,
	"DICT_6X6_1000": aruco.DICT_6X6_1000,
	"DICT_7X7_50": aruco.DICT_7X7_50,
	"DICT_7X7_100": aruco.DICT_7X7_100,
	"DICT_7X7_250": aruco.DICT_7X7_250,
	"DICT_7X7_1000": aruco.DICT_7X7_1000,
	"DICT_ARUCO_ORIGINAL": aruco.DICT_ARUCO_ORIGINAL,
	"DICT_APRILTAG_16h5": aruco.DICT_APRILTAG_16h5,
	"DICT_APRILTAG_25h9": aruco.DICT_APRILTAG_25h9,
	"DICT_APRILTAG_36h10": aruco.DICT_APRILTAG_36h10,
	"DICT_APRILTAG_36h11": aruco.DICT_APRILTAG_36h11
}
X=[450,240,160,125,120,100,80]
y=[5,10,15,20,21,25,30]
coff = np.polyfit(X,y,2)

aruco_type = "DICT_5X5_250"

arucoDict = aruco.getPredefinedDictionary(ARUCO_DICT[aruco_type])

arucoParams = aruco.DetectorParameters()
detector = aruco.ArucoDetector(arucoDict, arucoParams)


cap = cv.VideoCapture(0)

cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
pTime =0

while cap.isOpened():
    
	success, img = cap.read()
	h, w, _ = img.shape
	width = 1000
	height = int(width*(h/w))
	img = cv.resize(img, (width, height), interpolation=cv.INTER_CUBIC)
 
	corners, ids, rejected = detector.detectMarkers(img)
	if len(corners) > 0:
		ids = ids.flatten()
		for (markerCorner, markerID) in zip(corners, ids):
			corners = markerCorner.reshape((4, 2))
			(topLeft, topRight, bottomRight, bottomLeft) = corners
			topRight = (int(topRight[0]), int(topRight[1]))
			bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
			bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
			topLeft = (int(topLeft[0]), int(topLeft[1]))
			cv.line(img, topLeft, topRight, (0, 255, 0), 1)
			cv.line(img, topRight, bottomRight, (0, 255, 0), 1)
			cv.line(img, bottomRight, bottomLeft, (0, 255, 0), 1)
			cv.line(img, bottomLeft, topLeft, (0, 255, 0), 1)

			x1,y1= topRight[0],topRight[1]
			x2,y2= topLeft[0],topLeft[1]
			distance=sqrt((x1-x2)**2+(y1-y2)**2)
	        
			A,B,C = coff
			distanceCM = A*distance**2+B*distance+C

			cv.putText(img, str(markerID),(topLeft[0], topLeft[1] - 10), cv.FONT_HERSHEY_SIMPLEX,
                0.75, (0, 255, 255), 2)
			cv.putText(img,f'Distance: {int(distanceCM)}',(bottomRight[0],bottomRight[1]+10),cv.FONT_HERSHEY_PLAIN,1,(0,255,255),2)
			print("[Inference] ArUco marker ID: {}".format(markerID))
	cTime = time.time()
	fps = 1/(cTime - pTime)
	pTime = cTime   
	cv.putText(img,f'FPS: {int(fps)}',(20,70),cv.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
	cv.imshow("Image", img)
	if cv.waitKey(20) & 0xFF==ord('d'):
		break

cv.destroyAllWindows()
cap.release()