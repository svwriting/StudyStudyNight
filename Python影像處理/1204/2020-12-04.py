import cv2
import numpy as np


# m1=cv2.imread("1.png", 1)
# m2=cv2.inRange(m1, (200,200,200), (255,255,255))
# m2=cv2.erode(m2, np.ones((3,3)))


# a, b=cv2.findContours(m2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# print(a)
# print(b)
# r=cv2.VideoWriter(
# 	"2.mp4", 
# 	cv2.VideoWriter_fourcc(*'MP4V'), 
# 	30, 
# 	(m1.shape[1],m1.shape[0])
# )
# m3=np.full(m1.shape,255,np.uint8)
# cv2.drawContours(m3,a,-1,(0,0,255),2)
# for i in range(0,len(a),1):
	# m3=np.full(m1.shape,255,np.uint8)
	# m3=m1.copy()
	# cv2.drawContours(m3,a,i,(0,0,255),2)
	# x, y, w, h =cv2.boundingRect(a[i])
	# cv2.rectangle(m3, (x,y), (x+w,y+h), (0,0,255), 2)
	# r.write(m3)
	# cv2.imwrite("images/"+str(i)+".png", m1[y:y+h,x:x+w])
	# cv2.imshow("m3 "+str(i), m1[y:y+h,x:x+w])
	# cv2.waitKey(0)
# r.release()

# cv2.imshow("m1", m1)
# cv2.imshow("m2", m2)
# cv2.imshow("m3", m3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# m1=cv2.imread("udn2/image/49-3.jpg", 1)
# m2=cv2.inRange(m1, (0,0,180), (100,100,255))
# m2=cv2.erode(m2, np.ones((10,10)))
# m2=cv2.dilate(m2, np.ones((30,60)))
# m2=cv2.dilate(m2, np.ones((10,10)))
# m2=cv2.bitwise_not(m2)
# m2=cv2.cvtColor(m2,cv2.COLOR_GRAY2BGR)
# m2=cv2.add(m1,m2)
# a, b=cv2.findContours(m2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# m3=np.full(m1.shape,255,np.uint8)
# cv2.drawContours(m3,a,-1,(0,0,255),2)
# for i in range(0,len(a),1):
# 	x, y, w, h =cv2.boundingRect(a[i])
# 	cv2.rectangle(m1, (x,y), (x+w,y+h), (0,255,0), 2)
	# cv2.imshow("m1 "+str(i), m1[y:y+h,x:x+w])
# m1=cv2.imread("3.png", 1)
# m2=cv2.inRange(m1, (26,18,227), (46,38,247))
# m3=cv2.inRange(m1, (194,62,53), (214,82,73))
# m2=cv2.erode(m2, np.ones((3,3)))
# m3=cv2.erode(m3, np.ones((3,3)))
# m4=cv2.add(m2,m3)
# m4=cv2.erode(m4, np.ones((3,3)))
# m4=cv2.dilate(m4, np.ones((3,3)))
# m4=cv2.cvtColor(m4,cv2.COLOR_GRAY2BGR)
# m4=cv2.add(m1,m4)
# m4=cv2.inRange(m4, (200,200,200), (255,255,255))
# m1=cv2.imread("3.png", 1)
# m4=cv2.inRange(m1, (200,200,200), (255,255,255))
# m4=cv2.bitwise_not(m4)
# a, b=cv2.findContours(m4,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# m2=np.full(m1.shape,255,np.uint8)
# for i in range(0,len(a),1):
# 	if b[0][i][3]!=-1:
# 		cv2.drawContours(m2,a,i,(0,0,0),-1)
# 		# x, y, w, h =cv2.boundingRect(a[i])
# 		# cv2.rectangle(m1, (x,y), (x+w,y+h), (0,255,0), 2)
# m2=cv2.dilate(m2, np.ones((3,3)))
# m2=cv2.add(m1,m2)
# cv2.imshow("m1", m1)
# cv2.imshow("m2", m2)
# # cv2.imshow("m3", m3)
# # cv2.imshow("m4", m4)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import pytesseract as pt

# m1=cv2.imread("4.png", 1)

# text=pt.image_to_string(m1, "eng", "")
# for i in range(0,len(text)):
# 	if text[i]=="B":
# 		print(" ",end="")
# 		continue
# 	print(text[i],end="")


# cv2.imshow("m1", m1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# m1=cv2.imread("3.png", 1)
# m4=cv2.inRange(m1, (200,200,200), (255,255,255))
# m4=cv2.bitwise_not(m4)
# a, b=cv2.findContours(m4,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# m2=np.full(m1.shape,255,np.uint8)
# for i in range(0,len(a),1):
# 	if b[0][i][3]!=-1:
# 		cv2.drawContours(m2,a,i,(0,0,0),-1)
# m2=cv2.dilate(m2, np.ones((3,3)))
# m2=cv2.add(m1,m2)
# text=pt.image_to_string(m2, "eng", "")
# print(text)

# cv2.imshow("m1", m1)
# # cv2.imshow("m2", m2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# m1=cv2.imread("udn2/image/49-3.jpg", 1)
# m2=cv2.inRange(m1, (0,0,180), (100,100,255))
# m2=cv2.erode(m2, np.ones((10,10)))

# text=pt.image_to_string(m2, "eng", "")
# print(text)

# cv2.imshow("m1", m1)
# cv2.imshow("m2", m2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# m1=cv2.imread("5.png", 1)

# text=pt.image_to_string(m1, "my", "")
# print(text)

# cv2.imshow("m1", m1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

from pyzbar import pyzbar


# m1=cv2.imread("7.png", 1)

# ret=pyzbar.decode(m1)
# for d in ret:
# 	print("條碼類型：",d.type)
# 	try:
# 		print("存的資料：",d.data.decode("utf-8").encode("sjis").decode("utf-8"))
# 	except:
# 		print("存的資料：",d.data.decode("utf-8"))
# 	x,y,w,h=d.rect
# 	cv2.rectangle(m1, (x,y), (x+w,y+h), (0,0,255), 2)
# 	print("======================")


m1=cv2.imread("classifier_training/Data/Image.jpg", 1)
p1=cv2.CascadeClassifier("classifier_training/xml/cascade.xml")
ret=p1.detectMultiScale(m1,minNeighbors=3,minSize=(10,10))
for x,y,w,h in ret:
	cv2.rectangle(m1, (x,y), (x+w,y+h), (0,0,255), 2)

cv2.imshow("m1", m1)
cv2.waitKey(0)
cv2.destroyAllWindows()


# p=cv2.VideoCapture(0)
# p1=cv2.CascadeClassifier("cascade/haarcascade_frontalface_default.xml")
# while p.isOpened()==True:
# 	ret, m1=p.read()
# 	if ret==True:
# 		ret=p1.detectMultiScale(m1,minNeighbors=5,minSize=(10,10))
# 		for x,y,w,h in ret:
# 			cv2.rectangle(m1, (x,y), (x+w,y+h), (0,0,255), 2)

# 		cv2.imshow("m1", m1)
# 		if cv2.waitKey(33)!=-1:
# 			break
# 	else:
# 		break
# cv2.destroyAllWindows()

# p=cv2.VideoCapture(0)
# while p.isOpened()==True:
# 	ret, m1=p.read()
# 	if ret==True:
# 		ret=pyzbar.decode(m1)
# 		for d in ret:
# 			print("存的資料：",d.data.decode("utf-8"))
# 			x,y,w,h=d.rect
# 			cv2.rectangle(m1, (x,y), (x+w,y+h), (0,0,255), 2)

# 		cv2.imshow("m1", m1)
# 		if cv2.waitKey(33)!=-1:
# 			break
# 	else:
# 		break
# cv2.destroyAllWindows()