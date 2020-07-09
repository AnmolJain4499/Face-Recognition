import tkinter as tk
import os
from tkinter import messagebox
import cv2
import glob
import openpyxl


window = tk.Tk()
window.title("Face Detection")
window.configure(background='brown')
window.geometry("450x200+400+200")
window.minsize(570,200)


def videoTester():
    print("videoTester")
    os.system('videoTester.py')

def Train():
    print("Train")
    import faceRecognition as fr

    faces,faceID=fr.lables_for_traning_data('training_img')
    face_recognizer=fr.train_classifier(faces,faceID)
    face_recognizer.save('trainingData.yml')
    
def Svimg():
    print("New Entry")
    save = tk.Tk()
    save.title("Save Image")
    #save.configure(background='brown')
    save.geometry("200x100+400+200")
    save.minsize(300,100)

    ref1={0:'A1',1:'B1',2:'C1',3:'D1',4:'E1',5:'F1',6:'G1',7:'H1',8:'I1',9:'J1',10:'K1',11:'L1',12:'M1',13:'N1',14:'O1',15:'P1',16:'Q1',17:'R1',18:'S1',19:'T1',20:'U1',21:'V1',22:'W1',23:'X1',24:'Y1',25:'Z1',26:'AA1',27:'AB1',28:'AC1',29:'AD1',30:'AE1'}
    ref2={0:'A2',1:'B2',2:'C2',3:'D2',4:'E2',5:'F2',6:'G2',7:'H2',8:'I2',9:'J2',10:'K2',11:'L2',12:'M2',13:'N2',14:'O2',15:'P2',16:'Q2',17:'R2',18:'S2',19:'T2',20:'U2',21:'V2',22:'W2',23:'X2',24:'Y2',25:'Z2',26:'AA2',27:'AB2',28:'AC2',29:'AD2',30:'AE2'}
    def startsaving():
        naam=name.get("1.0",tk.END)
        list_of_files = glob.glob('training_img/*') # * means all if need specific format then *.csv
        try:
            latest_file = max(list_of_files, key=os.path.getctime)
            svb=int(latest_file[-1:len(latest_file )+1])
            svb=svb+1
        except:
            svb=0
        
        
        print(svb)
        print(naam)
        if len(naam)<3:
            messagebox.showwarning("Warning","Enter Valid Name")
        else:
            dirName= "training_img/" + str(svb)
            print(dirName)
            try:
                os.mkdir(dirName)
                print("Directory " , dirName ,  " Created ") 
            except FileExistsError:
                print("Directory " , dirName ,  " already exists")
        
            xfile = openpyxl.load_workbook('name.xlsx')
            sheet = xfile.get_sheet_by_name('Sheet1')
            sheet[ref1[svb]] = svb
            sheet[ref2[svb]] = naam
            xfile.save('name.xlsx')
        
        
            cap=cv2.VideoCapture(0)
            count = 0
            while True:
                ret,test_img=cap.read()
                if not ret :
                    continue
                cv2.imwrite(dirName + "/frame%d.jpg" % count, test_img)
                count += 1
                resized_img = cv2.resize(test_img, (1000, 700))
                cv2.imshow('face detection Tutorial ',resized_img)
                if cv2.waitKey(10) == ord('q'):
                    break
                elif count>100:
                    break
            cap.release()
            cv2.destroyAllWindows()    
            save.destroy()        
        


    namelbl=tk.Label(save,text="Name")
    namelbl.grid(row=0,column=0,padx=20,pady=20)
    name = tk.Text(save, height=1, width=20)
    name.grid(row=0,column=1,padx=20,pady=20)
    button =tk.Button(save,text="Start Saving",command=startsaving, width=20, height=1)
    button.grid(row=1,columnspan=2)
    save.mainloop()
               
     # Save Image End #  


    namelbl=tk.Label(save,text="Name")
    namelbl.grid(row=0,column=0,padx=20,pady=20)
    
    name = tk.Text(save, height=1, width=20)
    name.grid(row=0,column=1,padx=20,pady=20)
    
    button =tk.Button(save,text="Start Saving",command=startsaving, width=20, height=1)
    button.grid(row=1,columnspan=2)


    save.mainloop()
        
detect = tk.Button(window, text ="Detect Faces", command = videoTester, height = 3, width = 20)
detect.configure(background='orange')
detect.grid(row=0, column=0, padx=20, pady=70)

train = tk.Button(window, text ="Train Data", command = Train, height = 3, width = 20)
train.configure(background='orange')
train.grid(row=0, column=1, padx=20)

svimg = tk.Button(window, text ="Enter new Data", command = Svimg,  height = 3, width = 20)
svimg.configure(background='orange')
svimg.grid(row=0, column=2, padx=20)



window.mainloop()