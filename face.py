import cv2
import numpy as np
cap=cv2.VideoCapture(0)
kernel=np.ones((5,5),np.uint8)
while(True):
    hx,frame=cap.read()
    if hx is False:
        print("error")
        exit()
    img=frame.copy()
    frame=cv2.cvtColor(frame ,cv2.COLOR_BGR2GRAY)
    facedata=cv2.CascadeClassifier('C://Users//admin//PycharmProjects//parting//venv//face.xml')
    faceRect=facedata.detectMultiScale(frame,1.1,7)
    for (x,y,w,h) in faceRect:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0))
    cv2.namedWindow("videos",cv2.WINDOW_AUTOSIZE)
    cv2.imshow('videos',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()


