from godot import exposed, export
from godot import *
import cv2
import numpy as np
import HandTrackingModule as htm
import time
import pyautogui




@exposed
class PythonCaller(Node):
	##Cam Width and height
	
	pTime = 0
	detector = htm.HandDetector()
	landmarks = []
	cWidth,cHeight = 380,180
	sWidth, sHeight= pyautogui.size()
	def webcam(self):
		cap = cv2.VideoCapture(0)	
		cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.cWidth)
		cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.cHeight)
		while True:
	  
			self.ret, img = cap.read()
			img = cv2.flip(img, 1) 
			img = self.detector.findHands(img)

			##Fps
			cTime = time.time()
			fps = 1/(cTime-self.pTime)
			self.pTime = cTime
			self.landmarks = self.detector.lmList
   
			##Draw
			if  len(self.landmarks) !=0:
				print(self.landmarks[4])
	
	
			cv2.putText(img,f'FPS:{int(fps)}',(10,30),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
			cv2.imshow("Img", img)
			
			if cv2.getWindowProperty("Img", cv2.WND_PROP_VISIBLE) > 0:
				cv2.moveWindow("Img", int((self.sWidth/2)-(self.cWidth/2)), 20)  # Adjust the (x, y) values as needed
			cv2.waitKey(1)
			
	def _ready(self):
		self.webcam()
	
	
