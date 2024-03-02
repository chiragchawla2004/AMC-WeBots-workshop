import cv2 as cv
import mediapipe as mp
import pyautogui as pg

import numpy as np

def hello():
    return

cap =cv.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width,screen_height = pg.size()
index_y=0
while True:
    _,frame = cap.read()
    frame=cv.flip(frame,1)
    frame_height,frame_width,_= frame.shape
    rgb_frame=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands=output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
            landmarks=hand.landmark
            for id,landmark in enumerate(landmarks):
                    x=int(landmark.x*frame_width)
                    y=int(landmark.y*frame_height)
                    # print(x,y)
                    if id==8:
                         cv.circle(img=frame,center=(x,y),radius=10,color=(0,255,0))
                         index_x=screen_width/frame_width*x
                         index_y=screen_height/frame_height *y
                         pg.moveTo(index_x,index_y)
                    if id==4:
                         cv.circle(img=frame,center=(x,y),radius=10,color=(0,255,0))
                         thumb_x=screen_width/frame_width*x
                         thumb_y=screen_height/frame_height *y
                         print( abs(index_y-thumb_y))
                         if abs(index_y-thumb_y)<40:
                            pg.click()
                            pg.sleep(1)
                         


    cv.imshow('Frame',frame)

    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
