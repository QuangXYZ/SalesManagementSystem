import os, sys
import cv2
import numpy as np
import pickle

def faceRecognition():

    face_cascade = cv2.CascadeClassifier('..\SalesManagementSystem - Copy\Employee\cascade\data\haarcascade_frontalface_alt2.xml')
    recognition = cv2.face.LBPHFaceRecognizer_create()
    recognition.read("trainner.yml")

    labels = {"person_name: ":1}
    if os.path.getsize("label.pickle") > 0:
        with open("label.pickle",'rb') as f:
            print(f.name)

            og_labels = pickle.load(f)
            labels = {v:k for k,v in og_labels.items()}

    cap = cv2.VideoCapture(0)
    i = 0
    while(True):
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)

<<<<<<< Updated upstream
    def encode_faces(self):
        os.listdir('images/Face')
        for image in os.listdir('images/Face'):
            face_image = face_recognition.load_image_file(f"images/Face/{image}")
            face_encoding = face_recognition.face_encodings(face_image)[0]
=======
        # image_item = os.path.join('E:\Python\SalesManagementSystem - Copy\Images\Face_customer\CTM8197',f'CTM8197_{i}.png')
        # cv2.imwrite(image_item,roi_gray)
>>>>>>> Stashed changes

        for (x,y,w,h) in faces:
            print(x,y,w,h)

            roi_gray = gray[y:y+h,x:x+w]
            id_,conf = recognition.predict(roi_gray)
            if conf >= 45 and conf <= 80:
                print(id_)
                print(labels[id_])
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color = (255,0,0)
                stroke = 2
                cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)
                cv2.destroyAllWindows()
                return name

            color = (255,0,0)
            stroke =2
            endcord_x = x + w
            endcord_y = y + h
            cv2.rectangle(frame,(x,y),(endcord_x,endcord_y),color,stroke)

        cv2.imshow('frame',frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
        
        if i == 20:
            break
        
    cap.release()
    cv2.destroyAllWindows()