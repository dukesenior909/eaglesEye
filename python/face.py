import numpy as np
import cv2
def faceD(img):
	f_cascade=cv2.CascadeClassifier('C:\haarcascade_frontalface_default.xml')
	img1=img.copy()
	gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
	faces=f_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
	for(x,y,w,h) in faces:
		cv2.rectangle(img1,(x,y),(x+w,y+h),(255,0,255),3)
	return img1
