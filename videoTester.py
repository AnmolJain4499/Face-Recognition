import cv2
import faceRecognition as fr
import pandas

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
                    
face_recognizer.read('trainingData.yml')

file_name = 'name.xlsx'
names = pandas.read_excel(file_name)
named = names.to_dict('records')
name=named[0]
print(name)

cap=cv2.VideoCapture(0)

while True:
    ret,test_img=cap.read()
    faces_detected,gray_img=fr.faceDetection(test_img)

    for face in faces_detected:
        (x,y,w,h)=face
        roi_gray=gray_img[y:y+w, x:x+h]
        label,confidence=face_recognizer.predict(roi_gray)
        print("confidence:",confidence)
        print("label:",label)
        fr.draw_rect(test_img,face)
        predicted_name=name[label]
        if confidence < 60:#If confidence less than 37 then don't print predicted face text on screen
           fr.put_text(test_img,predicted_name,x,y,w,h)


    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('face recognition tutorial ',resized_img)
    if cv2.waitKey(10) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
