import cv2,os
import numpy as np


videof_=cv2.VideoCapture("h3.mp4")

while videof_.isOpened():
    _,frame_=videof_.read()
    #gframe_=cv2.inRange(frame_,(50,0,0),(255,60,60))
    frame_
    gframe_=cv2.cvtColor(frame_,cv2.COLOR_BGR2GRAY)
    _,bframe_=cv2.threshold(gframe_,0,255,cv2.THRESH_BINARY_INV)

    cframe_,clframe_=cv2.findContours(
        bframe_,
        cv2.RETR_LIST,
        cv2.CHAIN_APPROX_SIMPLE
    )
    cv2.drawContours(
        frame_,
        cframe_,
        -1,
        (0,0,255),
        3
    )
    cv2.imshow("Video",frame_)
    if cv2.waitKey(30)!=-1:
        break
cv2.destroyAllWindows()