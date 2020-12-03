import cv2
import numpy as np


# m1=cv2.imread("udn2/image/5-1.jpg", 1)
# m2=cv2.imread("udn2/image/6-1.jpg", 1)
# m2=np.full(m1.shape,255,np.uint8)

# m3=cv2.add(m1,(200))
# m3=cv2.subtract(m1,m2)
# m3=cv2.absdiff(m1,m2)

# m3=cv2.divide(m1,m2)
# m3=cv2.multiply(m1,m2)
# m2=cv2.bitwise_not(m1)
# m2=m1+500
# print(m2)
# w=300
# h=int((w/m1.shape[1])*m1.shape[0])

# h=300
# w=int((h/m1.shape[0])*m1.shape[1])

# m2=cv2.resize(m1, (w,h))

# m2=cv2.flip(m1, 0)
# cx=int(m1.shape[1]/2)
# cy=int(m1.shape[0]/2)
# m2=cv2.warpAffine(m1, cv2.getRotationMatrix2D((cx,cy), 45, 1), (m1.shape[1],m1.shape[0]))

# m1=cv2.imread("udn2/image/5-1.jpg", 1)
# m2=cv2.imread("udn2/image/6-1.jpg", 1)
# m2=np.full(m1.shape,100,np.uint8)
# m2=m1[0:300,0:300].copy()
# m3=m1[:,:,0].copy()
# cv2.rectangle(m2, (0,100), (100,200), (255,255,255), -1)

# m2[100:400,100:400]=m1[0:300,0:300]
# cv2.rectangle(m2, (100,100), (200,200), (255,255,255), -1)

# m2[::2,::2]=m1[::2,::2]
# m1[0:300,0:300]=cv2.flip(m1[0:300,0:300], 0)
# m1[0:300,0:300]=cv2.add(m1[0:300,0:300], m2[0:300,0:300])

# print(m1.shape)
# cv2.imshow("m1", m1)

# print(m2.shape)
# cv2.imshow("m2", m2)

# print(m3.shape)
# cv2.imshow("m3", m3)


# cv2.imshow("m1 A1", m1[::2,::2])
# cv2.imshow("m1 A2", m1[:,:,1])
# cv2.imshow("m1 A3", m1[:,:,2])

# m1=cv2.cvtColor(m1,cv2.COLOR_BGR2GRAY)
# cv2.imshow("m1 B", m1)
# cv2.imshow("m2", m2)
# cv2.imshow("m3", m3)
# m1=cv2.imread("udn2/image/5-1.jpg", 1)
# m1=cv2.imread("1.jpg", 1)
# m2=m1.copy()

# th, m2[:,:,0]=cv2.threshold(m1[:,:,0], 127, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# print(th)
# th, m2[:,:,1]=cv2.threshold(m1[:,:,1], 127, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# print(th)
# th, m2[:,:,2]=cv2.threshold(m1[:,:,2], 127, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# print(th)
# m2[:,:,0]=cv2.adaptiveThreshold(m1[:,:,0],255,
# 	cv2.ADAPTIVE_THRESH_MEAN_C,
# 	cv2.THRESH_BINARY,
# 51,0)
# m2[:,:,1]=cv2.adaptiveThreshold(m1[:,:,1],255,
# 	cv2.ADAPTIVE_THRESH_MEAN_C,
# 	cv2.THRESH_BINARY,
# 51,0)
# m2[:,:,2]=cv2.adaptiveThreshold(m1[:,:,2],255,
# 	cv2.ADAPTIVE_THRESH_MEAN_C,
# 	cv2.THRESH_BINARY,
# 51,0)
# m2=cv2.Canny(m1,50,150)
# m3=cv2.Canny(m1,100,200)

# m2=cv2.blur(m1,(101,101))
# m2=cv2.medianBlur(m1,101)
m1=cv2.imread("h2.png", 1)
m2=m1.copy()
# m2[:,:,0]=cv2.equalizeHist(m1[:,:,0])
# m2[:,:,1]=cv2.equalizeHist(m1[:,:,1])
# m2[:,:,2]=cv2.equalizeHist(m1[:,:,2])

# m2=cv2.dilate(m1, np.ones((3,1)))
# m2=cv2.erode(m2, np.ones((3,1)))
# m2=cv2.morphologyEx(m1, cv2.MORPH_GRADIENT, np.ones((3,1)))
m2=cv2.inRange(m1, (0,0,255), (0,0,255))
# m2=cv2.bitwise_not(m2)
cv2.imshow("m1", m1)
cv2.imshow("m2", m2)
# cv2.imshow("m3", m3)
cv2.waitKey(0)
cv2.destroyAllWindows()