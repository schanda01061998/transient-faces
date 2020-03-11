import cv2
import numpy as np
import os
import face_recognition
from datetime import datetime
j=0
i=0
m=0
face_cascade=cv2.CascadeClassifier('cascade/data/haarcascade_frontalface_default.xml')

cap=cv2.VideoCapture(0)

while(True):
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.5, minNeighbors=5)
    for(x,y,w,h)in faces:
        print(x,y,w,h)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        
        parent='C:/project'
        dire="user%s" %j
        path=os.path.join(parent,dire)
        mode=0o666
        os.mkdir(path,mode)
        cv2.imwrite('C:/project/All pictures/use'+str(m)+'.png',roi_color)
        m=m+1
        while(i<10):
	        cv2.imwrite('C:/project/user'+str(j)+'/id'+str(i)+'.png',roi_color)
	        cv2.waitKey(300)
	        f= open('C:/project/user'+str(j)+'/time_date.txt',"w+")
	        k=datetime.now()
	        f.write(str(k))
	        f.close()
	        i+=1
        i=0
        j+=1

        color=(250,0,0)
        stroke=3
        cord_x=x+w
        cord_y=y+h
        cv2.rectangle(frame,(x,y),(cord_x,cord_y),color,stroke)


        cv2.imshow('frame',frame)
        if cv2.waitKey(1)==13:
            exit()
cap.release() 
cv2.destroyAllWindows()
