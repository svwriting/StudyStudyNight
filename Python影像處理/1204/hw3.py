import cv2
import numpy as np


p=cv2.VideoCapture("h3.mp4")
while p.isOpened()==True:
	ret, m1=p.read()
	if ret==True:
		m2=cv2.inRange(m1, (83,0,0), (183,84,63))
		m2=cv2.dilate(m2, np.ones((20,20)))
		a, b=cv2.findContours(m2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
		for i in range(0,len(a),1):
			if b[0][i][3]==-1:
				x, y, w, h =cv2.boundingRect(a[i])
				cv2.rectangle(m1, (x,y), (x+w,y+h), (0,0,255), 2)
		cv2.imshow("m1", m1)
		cv2.imshow("m2", m2)
		if cv2.waitKey(33)!=-1:
			break
	else:
		break
cv2.destroyAllWindows()
