from godot import exposed, export
from godot import *
import cv2
import numpy as np
import HandTrackingModule as htm
import time
import pyautogui
import threading

@exposed
class PythonCaller(Node):
	pTime = 0
	detector = htm.HandDetector()
	landmarks = []

	sWidth, sHeight = pyautogui.size()
	cWidth, cHeight = int(16 * (sWidth / 100)), int(9 * (sHeight / 100))
	cap = cv2.VideoCapture(0)  # Moved the capture here
	moveLeft = False
	moveRight = False
	def _process(self, delta):
		self.webcam()

	def webcam(self):
		ret, img = self.cap.read()
		img = cv2.flip(img, 1)
		img = self.detector.findHands(img)
		self.landmarks = self.detector.findPos(img)
		cTime = time.time()
		fps = 1 / (cTime - self.pTime)
		self.pTime = cTime
		
		#if len(self.landmarks) != 0:
		#	print(self.landmarks[0])
		#	if self.landmarks[0].cx > 300:
		#		self.moveRight = True
		#	else:
		#			self.moveRight = True
		cv2.putText(img, f'FPS:{int(fps)}', (10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
		cv2.imshow("Img", img)

		if cv2.getWindowProperty("Img", cv2.WND_PROP_VISIBLE) > 0:
			cv2.moveWindow("Img", int((self.sWidth) - (self.cWidth * 2)), int((self.sHeight / 3) - (self.cHeight)))
			
	def _exit_tree(self):
		self.cap.release()  # Release the capture when the node is exiting

