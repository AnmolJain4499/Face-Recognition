import cv2
import os
import numpy as np

def faceDetection(test_img):
    gray_img=cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
    face_haar_cascade=cv2.CascadeClassifier('C:/Users/Anirudh/.spyder-py3/Projects/Face/Haar cascade/haarcascade_frontalface_default.xml')
    faces=face_haar_cascade.detectMultiScale(gray_img,scaleFactor=1.32,minNeighbors=5)
    return faces,gray_img

def lables_for_traning_data(directory):
    faces=[]
    faceID=[]
    
    for path,subdirname,filenames in os.walk(directory):
        for filename in filenames:
            if filename.startswith("."):
                print("File is skipping beacuse it is starting with '.'")
                continue
            
            id=os.path.basename(path)
            img_path=os.path.join(path,filename)
            print("Image path : ",img_path)
            print("ID:",id)
            test_img=cv2.imread(img_path)
            if test_img is None:
                print("image is not loaded properly")
                continue
            faces_rect,gray_img=faceDetection(test_img)
            if len(faces_rect)!=1:
                continue
            (x,y,w,h)=faces_rect[0]
            roi_gray=gray_img[y:y+w,x:x+h]
            faces.append(roi_gray)
            faceID.append(int(id))
    return faces,faceID

def train_classifier(faces,faceID):
    face_recognizer=cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(faces,np.array(faceID))
    return face_recognizer

def draw_rect(test_img,face):
    (x,y,w,h)=face
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(0,0,255),thickness=2)
    
def put_text(test_img,text,x,y,w,h):
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(225,0,0),thickness=2)
    cv2.putText(test_img,text,(x,y),cv2.FONT_HERSHEY_DUPLEX,2,(255,0,0),4)    
