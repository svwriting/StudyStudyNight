import cv2
import numpy as np

img=cv2.imread("h2.png", 1)

def method1(img_): # 矩陣做
  for i in range(img_.shape[0]):
    for j in range(img_.shape[1]):
      if img_[i][j][0]>0 or img_[i][j][1]>0 or img_[i][j][2]<255:
        img_[i][j]=[255,255,255]
      else:
        img_[i][j]=[0,0,0]
  return img_

def method2(img_): # inRange
  img_=cv2.inRange(img_, (0,0,255), (0,0,255))
  return 255-img_

def method3(img_): # cv2四則運算，但感覺效率待商榷
  R_=img_[:,:,2]
  img_=cv2.add(img_[:,:,0]+img_[:,:,1],254)
  img_=cv2.subtract(R_,img_)
  img_=cv2.multiply(1-img_,255)
  return img_

# 我不懂他要的是什麼 OTZ...
# cv2.imshow("img",method1(img.copy())) # 矩陣做，但老師說不要用迴圈和判斷
# cv2.imshow("img",method2(img.copy())) # inRange，但老師說要+-*/
cv2.imshow("img",method3(img.copy())) # 老師是要用cv2的四則運算？
cv2.waitKey()
