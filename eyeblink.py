import cv2
import numpy as np
import pyautogui as p
port = 1
frame = 30
camera = cv2.VideoCapture(port)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
while (camera.isOpened()):
   ret,img = camera.read()
   gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
   faces = face_cascade.detectMultiScale(gray,1.2,5)
   c=0
   for (x,y,w,h) in faces:
        cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = gray[y:y+h, x:x+w]
        
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        for (ex,ey,ew,eh) in eyes:
           c=1
           cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
   if c==0:
    	p.press("down")
    	print("blinked")
    	    
   cv2.imshow('img',gray)
   cv2.imshow('gray',gray)
   k = cv2.waitKey(30) & 0xff
   if k==27:
        break
            
camera.release()
cv2.destroyAllWindows()
