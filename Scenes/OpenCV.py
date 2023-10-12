from godot import exposed, export
from godot import *
import cv2
import mediapipe as mp
import time

@exposed
class OpenCV(Node):
	def __init__(self, mode=False, maxHands=2, modelComp=1, detectionCon=0.5, trackCon=0.5):
		self.mode = mode
		self.maxHands = maxHands
		self.detectionCon = detectionCon
		self.trackCon = trackCon
		self.modelComp = modelComp

		self.mpHands = mp.solutions.hands # type: ignore
		self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComp, self.detectionCon, self.trackCon)
		self.mpDraw = mp.solutions.drawing_utils # type: ignore

	def _ready(self):
		main()
		pass

	def findHands(self, img, draw = True):          
		imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		self.results = self.hands.process(imgRGB)

		if self.results.multi_hand_landmarks:
			for handLms in self.results.multi_hand_landmarks:
				if draw:
					self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
		return img
				
	def findPos(self, img, handNo = 0, draw = False):
		lmList = []
		if self.results.multi_hand_landmarks:
			myHand = self.results.multi_hand_landmarks[handNo]
			for id, lm in enumerate(myHand.landmark):
				h, w, c = img.shape 
				cx, cy = int(lm.x*w), int(lm.y*h)
				lmList.append([id,cx,cy])
				if draw:
					cv2.circle(img, (cx,cy), 25, (255,0,0), cv2.FILLED)
			
		return lmList
		
def main():
	##Frame Rate
	pTime = 0
	cTime = 0
	
	#Camera
	cap = cv2.VideoCapture(0)
	detector = OpenCV()
	while True:
		ret, img = cap.read()
		img = cv2.flip(img, 1) 
		img = detector.findHands(img)
		lmList = detector.findPos(img)
		if len(lmList) !=0:
			print(lmList[4])
		cTime = time.time()
		fps = 1/(cTime - pTime)
		pTime = cTime

		cv2.putText(img,f'FPS:{int(fps)}',(10,30),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
		
		cv2.imshow('Image', img)
		if cv2.waitKey(1) == ord('q'):
			break
#if __name__ == "__main__":
#	main()
