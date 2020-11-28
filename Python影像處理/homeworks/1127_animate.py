import cv2 ,os 
import numpy as np

# 速度想調成一樣太麻煩了，我放棄
# 這和距離增減值、等待秒數、還有程式碼效率有關
# 而距離增減值和程式碼效率也會影響動畫平滑度
square_=np.full((100,100,3),(255,0,0),np.uint8)         # 正方形
wholepic=np.full((300,500,3),(255,255,255),np.uint8)    # 畫布
frameN=0                                                # 第幾幀
d=2							# 距離增減值

def PSmerge(frameN):					# 把正方形放到白色畫布上
    return cv2.rectangle(wholepic.copy(),(frameN,101),(100+frameN,200),(255,0,0),-1)


while True:
    cv2.imshow("image",PSmerge(frameN))
    frameN+=d
    if cv2.waitKey(1)!=-1:
        break
    if frameN<=0 or frameN>=400:
        d*=-1
cv2.destroyAllWindows()