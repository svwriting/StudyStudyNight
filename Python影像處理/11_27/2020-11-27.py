import cv2
import numpy as np


# m1=cv2.imread("udn2/image/49-3_A.jpg", 1)
# m1=cv2.cvtColor(m1, cv2.COLOR_BGR2HSV)

# print(m1.shape)
# print(m1)
# m1=cv2.cvtColor(m1, cv2.COLOR_BGR2GRAY)
# print(m1.shape)

# cv2.imwrite("udn2/image/49-3_A.jpg", m1,[cv2.IMWRITE_JPEG_QUALITY, 100])

# m1=cv2.cvtColor(m1, cv2.COLOR_GRAY2BGR)
# print(m1.shape)


# cv2.imshow("m1", m1)
# print(m1.shape)
# print("高：",m1.shape[0])
# print("寬：",m1.shape[1])


# cv2.waitKey(0)
# cv2.destroyAllWindows()


# p=cv2.VideoCapture("2020-11-27.mp4")
# # print("總共的畫面數量：",p.get(7))
# print("寬：",p.get(3))
# print("高：",p.get(4))
# print("FPS：",p.get(5))
# p.set(1, 5000)
# while p.isOpened()==True:
# 	ret, m1=p.read()
# 	if ret==True:
# 		# print("當前的畫面：",p.get(1))
# 		cv2.imshow("m1", m1)
# 		if cv2.waitKey(33)!=-1:
# 			break
# 	else:
# 		break
# cv2.destroyAllWindows()

# p=cv2.VideoCapture(0)
# w=int(p.get(3))
# h=int(p.get(4))
# r=cv2.VideoWriter(
# 	"1.mp4", 
# 	cv2.VideoWriter_fourcc(*'MP4V'), 
# 	30, 
# 	(w,h)
# )
# while p.isOpened()==True:
# 	ret, m1=p.read()
# 	if ret==True:
# 		r.write(m1)
# 		cv2.imshow("m1", m1)
# 		if cv2.waitKey(33)!=-1:
# 			break
# 	else:
# 		break
# r.release()
# cv2.destroyAllWindows()

from PIL import ImageFont, ImageDraw, Image

# m1=np.full((300, 500, 3), (255,255,255), np.uint8)

# m1=Image.fromarray(m1)
# ImageDraw.Draw(m1).text(
# 	(150,150), 
# 	"要寫的文字", 
# 	(0,0,255), 
# 	ImageFont.truetype("kaiu.ttf",50)
# )
# m1=np.array(m1)

# cv2.line(m1, (10,10), (200,10), (0,0,255), 2)

# cv2.rectangle(m1, (10,20), (100,100), (0,255,0), 2)
# cv2.rectangle(m1, (300,20), (400,100), (0,255,0), -1)

# cv2.circle(m1, (400,150), 100, (255,0,0), 2)
# cv2.circle(m1, (100,150), 100, (255,0,0), -1)

# cv2.imshow("m1", m1)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

i=0
while True:
	m1=np.full((300, 500, 3), (255,255,255), np.uint8)
	m1=Image.fromarray(m1)
	ImageDraw.Draw(m1).text(
		(150,150), 
		str(i), 
		(0,0,255), 
		ImageFont.truetype("kaiu.ttf",50)
	)
	m1=np.array(m1)
	i+=1

	cv2.imshow("m1", m1)
	if cv2.waitKey(33)!=-1:
		break

cv2.destroyAllWindows()
