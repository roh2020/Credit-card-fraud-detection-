import cv2
import numpy as np

name = input("Enter your name : ")
capture = cv2.VideoCapture(0)
dataset = cv2.CascadeClassifier("data.xml")
faceData = []

while True:
    ret, img = capture.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = dataset.detectMultiScale(gray,1.3)
        for x,y,w,h in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,255),4)
            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (50,50))
            if len(faceData) < 500:
                faceData.append(face)
                # print(len(faceData))
        cv2.imshow('result',img)
        if cv2.waitKey(10) == 27 or len(faceData) >= 500:
            break
    else:
        print("Camera not working...")

faceData = np.asarray(faceData)
np.save('face/'+name+'.npy', faceData)

capture.release()
cv2.destroyAllWindows()
