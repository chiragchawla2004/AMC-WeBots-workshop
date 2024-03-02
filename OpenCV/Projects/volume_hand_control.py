import cv2 as cv
import time
import numpy as np
import HandTrackingProjects.HandTrackingModule as htm
import math
import pycaw 
from ctypes import cast,POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


wCam, hCam = 640,480
cap = cv.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime = 0


detector = htm.handDetector(detectionCon=0.75)


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

volRange = (volume.GetVolumeRange())
volume.SetMasterVolumeLevel(-20.0,None)
minVol = volRange[0]
maxVol = volRange[1]
vol=0   
volBar=400
volPer=0

while True:
    success, img = cap.read()
    img = cv.flip(img,1)
    img = detector.findHands(img)
    lmList= detector.findPosition(img,draw=False)
    if len(lmList) !=0:
        # print(lmList[4],lmList[8])

        x1,y1 = lmList[4][1],lmList[4][2]
        x2,y2 = lmList[8][1],lmList[8][2]
        cx = (x1+x2)//2
        cy = (y1+y2)//2

        cv.circle(img,(x1,y1),5,(255,0,255),cv.FILLED)
        cv.circle(img,(x2,y2),5,(255,0,255),cv.FILLED)
        cv.circle(img,(cx,cy),5,(255,0,255),cv.FILLED)
        cv.line(img,(x1,y1),(x2,y2),(255,0,255),1)

        length = math.hypot(x2-x1,y2-y1)
        # print(length)

        if length<50:
            cv.circle(img,(cx,cy),5,(0,255,0),cv.FILLED)
        
        vol = np.interp(length,[20,300],[minVol,maxVol])
        volBar = np.interp(length,[20,300],[400,150])
        volPer = np.interp(length,[20,300],[0,100])
        volume.SetMasterVolumeLevel(vol,None)

    cv.rectangle(img,(50,150),(85,400),(0,255,0),3)
    cv.rectangle(img,(50,int(volBar)),(85,400),(0,255,0),cv.FILLED)
    cv.putText(img, f'{int(volPer)}%',(40,450),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),3)


    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv.putText(img,f'FPS: {int(fps)}',(20,50),cv.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)
    cv.imshow("Image",img)
    if cv.waitKey(10) & 0xFF==ord('d'): 
        break