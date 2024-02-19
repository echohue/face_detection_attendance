from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x790+0+0")
        self.root.title("Face Recognition")
        title_lbl = Label(self.root,text="FACE DETECTOR", font=("times new roman",30,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1400,height=40)

        img_top=Image.open(r"imagesfrs\facedetector.png")
        img_top=img_top.resize((600,600),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=600,height=600)

        img_bottom=Image.open(r"imagesfrs\phoneimg.webp")
        img_bottom=img_bottom.resize((700,600),Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=600,y=45,width=700,height=600)

        #button
        btn1 = Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_reg,font=("times new roman",18,"bold"),bg="red",fg="white")
        btn1.place(x=250,y=530,width=200,height=40)
    
    def mark_attendance(self,i,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{d},{dtString},{d1},Present")




    def face_reg(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord = [] 
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))
                conn = mysql.connector.connect(host="127.0.0.1", username="root", password="C5V7A9X8!c", database="frs", port="3307")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT Name FROM students WHERE ID="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                my_cursor.execute("SELECT Dep FROM students WHERE ID =  "+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                my_cursor.execute("SELECT ID FROM students WHERE ID =  "+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)



                if confidence>77:
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Department:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"ID:{i}",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    self.mark_attendance(i,n,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Not recognized by the system",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,h]
            return coord
        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap = cv2.VideoCapture(0)
        while True:
            ret,img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognition",img)

            if cv2.waitKey(10000) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()









if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()
