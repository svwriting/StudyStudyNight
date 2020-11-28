import cv2,os
import numpy as np

videof_=cv2.VideoCapture("h3.mp4")


def method1(frame_):    # 取S法二值化法
    frame_=cv2.cvtColor(frame_,cv2.COLOR_BGR2HSV)[:,:,1]
    _,frame_=cv2.threshold(frame_,150,255,cv2.THRESH_BINARY)
    return frame_

def method2(frame_):    # 算了懶得寫另外的方法了
    return frame_

overyet_,FIRSTframe_=videof_.read()
while videof_.isOpened():
    overyet_,frame_=videof_.read()
    if not overyet_:
        break

    cframe_=method1(frame_.copy())  # 判斷輪廓用的 cframe_

    Pss_,Ls_=cv2.findContours(cframe_, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(Pss_)>0:
        Ps_=Pss_[-1]
        x_,y_,w_,h_=cv2.boundingRect(Ps_)
        cv2.rectangle(frame_,(x_,y_),(x_+w_,y_+h_),(0,0,255),3)
    cv2.imshow("Video",frame_)
    if cv2.waitKey(30)!=-1:
        break
cv2.destroyAllWindows()