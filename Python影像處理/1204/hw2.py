import cv2
import numpy as np

m1=cv2.imread("h2.png", 1)

m2=cv2.bitwise_not(m1[:,:,2])
m2=cv2.add(m2,m1[:,:,1])
m2=cv2.add(m2,m1[:,:,0])
m2=cv2.multiply(m2, np.full(m2.shape,255,np.uint8))

cv2.imshow("m1", m2)
cv2.waitKey(0)
cv2.destroyAllWindows()