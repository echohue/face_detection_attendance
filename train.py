from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x790+0+0")
        self.root.title("Train Dataset")
        title_lbl=Label(self.root,text="TRAIN DATASET",font=("times new roman",30,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1300,height=35)

        img = Image.open(r"imagesfrs\img1.jpg")
        img = img.resize((500,230),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        first1 = Label(self.root,image = self.photoimg)
        first1.place(x=0,y=40,width=500,height=230)

        img1 = Image.open(r"imagesfrs\traindata.png")
        img1 = img1.resize((500,230),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        sec2 = Label(self.root,image = self.photoimg1)
        sec2.place(x=500,y=40,width=500,height=230)

        img2 = Image.open(r"imagesfrs\faced.webp")
        img2 = img2.resize((500,230),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        third3 = Label(self.root,image = self.photoimg2)
        third3.place(x=1000,y=40,width=500,height=230)

        #buttons
          
        btn1 = Button(self.root,text = "TRAIN DATA",command=self.train_classifier,width=15,font = ("times new roman",25),bg="blue")
        btn1.place(x=0,y=270,width=1300,height=70)

        img3 = Image.open(r"imagesfrs\frsbottom1.jpg")
        img3 = img3.resize((500,330),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        four4 = Label(self.root,image = self.photoimg3)
        four4.place(x=0,y=330,width=500,height=330)

        img4 = Image.open(r"imagesfrs\img3.jpg")
        img4 = img4.resize((500,330),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        five5 = Label(self.root,image = self.photoimg4)
        five5.place(x=500,y=330,width=500,height=330)
       
      

        img5 = Image.open(r"imagesfrs\bottom2.jpg")
        img5 = img5.resize((500,330),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        six6 = Label(self.root,image = self.photoimg5)
        six6.place(x=1000,y=330,width=500,height=330)
    
    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join (data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1) == 13 
        ids=np.array(ids)

        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Success","Training dataset completed!!")



        



if __name__ == "__main__" :
    root=Tk()
    obj=Train(root)
    root.mainloop()
