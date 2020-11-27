import cv2 ,os 
import numpy as np

def PSmerge(frameN):
    return cv2.rectangle(wholepic.copy(),(frameN,101),(100+frameN,200),(255,0,0),-1)

square_=np.full((100,100,3),(255,0,0),np.uint8)
#square_=cv2.rectangle(square_,(0,100),(100,100),(255,0,0),-1)
wholepic=np.full((300,500,3),(255,255,255),np.uint8)

cv2.imshow("image",wholepic)
wholepic= np.vstack([wholepic,])
KeyIn_=None
frameN=0
d=1
while True:
    cv2.imshow("image",PSmerge(frameN))
    frameN+=d
    if cv2.waitKey(5)!=-1:
        break
    if frameN<=0 or frameN>=400:
        d*=-1
cv2.destroyAllWindows()