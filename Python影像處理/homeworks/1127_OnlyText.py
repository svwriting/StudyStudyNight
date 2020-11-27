import cv2
import numpy as np

img_=cv2.imread("h2.png", 1)
h_=img_.shape[0]
w_=img_.shape[1]
img_=cv2.inRange(img_, (0,0,255), (0,0,255))
tempimg_=
cv2.imshow("img",255-img_)
cv2.waitKey()