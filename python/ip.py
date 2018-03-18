import face
import mail
import urllib.request
import cv2
import numpy as np
import argparse
import datetime

def ips():
	url="http://10.21.75.27:8080/shot.jpg"
	ap=argparse.ArgumentParser()	#parsing
	ap.add_argument("-a","--min-area",type=int,default=4000,help="minimum area size")
	args=vars(ap.parse_args())
	flag=1
	cnt=0
	imgResp=urllib.request.urlopen(url)
	imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
	first=cv2.imdecode(imgNp,-1)

	#convert to greyscale then blur it
	gray=cv2.cvtColor(first, cv2.COLOR_BGR2GRAY)
	gray=cv2.GaussianBlur(gray,(21,21),0)
	first=gray
	while(True):
		imgResp=urllib.request.urlopen(url)
		imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
		img=cv2.imdecode(imgNp,-1)
		img=face.faceD(img)
		gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		gray=cv2.GaussianBlur(gray,(21,21),0)
		delta=cv2.absdiff(first,gray)
		thresh=cv2.adaptiveThreshold(delta,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,4)
		thresh=cv2.dilate(thresh,None, iterations=2)
		(_,cnts,_)=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		for c in cnts:
			if cv2.contourArea(c)<args["min_area"]:
				continue
			cnt=cnt+1
			(x,y,w,h)=cv2.boundingRect(c)
			cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
		if(cnt>0 and flag==1):
				flag=0
				mail.mailx()
				print(cnt)
		cv2.imshow("test",img)
		cv2.waitKey(20)

    
