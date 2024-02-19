from tkinter import *
from tkinter import ttk
import tkinter 
from PIL import Image,ImageTk
import os
from time import strftime
from datetime import datetime
from studentdetails import Student
from train import Train
from face_recognizer import Face_recognition
from attendance import Attendance
from developer import Developer
from help import Help


class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")
        #upper image
        img = Image.open(r"imagesfrs\img1.jpg")
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        first1 = Label(self.root,image = self.photoimg)
        first1.place(x=0,y=0,width=500,height=130)

        img1 = Image.open(r"imagesfrs\img2.jpg")
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        sec2 = Label(self.root,image = self.photoimg1)
        sec2.place(x=500,y=0,width=500,height=130)

        img2 = Image.open(r"imagesfrs\img3.jpg")
        img2 = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        third3 = Label(self.root,image = self.photoimg2)
        third3.place(x=1000,y=0,width=500,height=130)

        #background image
        imgbg = Image.open(r"imagesfrs\collegebg.jpg")
        imgbg = imgbg.resize((1500,710),Image.ANTIALIAS)
        self.photoimgbg = ImageTk.PhotoImage(imgbg)
        four4 = Label(self.root,image = self.photoimgbg)
        four4.place(x=0,y=130,width=1500,height=710)
        title = Label(four4,text = "Face Recognition Attendance System", font = ("roboto",30,"bold"),bg = "white",fg = "blue")
        title.place(x=20,y=0,width=1350,height=45)

        def time():
             string = strftime('%H:%M:%S %p')
             lbl.config(text= string)
             lbl.after(1000,time)
        lbl = Label(four4,font=("times new roman",14,'bold'), fg="blue")
        lbl.place(x=50,y=50,width=110,height=30)
        time()

        #button image1
        btn1 = Image.open(r"imagesfrs\students.jpg")
        btn1 = btn1.resize((150,150),Image.LANCZOS)
        self.photobtn1 = ImageTk.PhotoImage(btn1)
        b1=Button(four4,image = self.photobtn1,command = self.student_details,cursor="hand2")
        b1.place(x=100,y=100,width=150,height=150)
        b1_text=Button(four4,text = "Student Details",command=self.student_details,cursor="hand2", font = ("roboto",15),bg = "white",fg = "blue")
        b1_text.place(x=100,y=250,width=150,height=40)

        #button image2
        btn2 = Image.open(r"imagesfrs\faced.webp")
        btn2 = btn2.resize((150,150),Image.LANCZOS)
        self.photobtn2 = ImageTk.PhotoImage(btn2)
        b2=Button(four4,image = self.photobtn2,cursor="hand2",command=self.facerecognition_button)
        b2.place(x=300,y=100,width=150,height=150)
        b2_text=Button(four4,text = "FaceDetection",cursor="hand2",command=self.facerecognition_button, font = ("roboto",15),bg = "white",fg = "blue")
        b2_text.place(x=300,y=250,width=150,height=40)

        #button image3
        btn3 = Image.open(r"imagesfrs\attendance.jpg")
        btn3 = btn3.resize((150,150),Image.LANCZOS)
        self.photobtn3 = ImageTk.PhotoImage(btn3)
        b3=Button(four4,image = self.photobtn3,command=self.attendance_button,cursor="hand2")
        b3.place(x=500,y=100,width=150,height=150)
        b3_text=Button(four4,text = "Attendance",command=self.attendance_button,cursor="hand2", font = ("roboto",15),bg = "white",fg = "blue")
        b3_text.place(x=500,y=250,width=150,height=40)

        #button image4
        btn4 = Image.open(r"imagesfrs\help.jpg")
        btn4 = btn4.resize((150,150),Image.LANCZOS)
        self.photobtn4 = ImageTk.PhotoImage(btn4)
        b4=Button(four4,image = self.photobtn4,command=self.help_btn,cursor="hand2")
        b4.place(x=700,y=100,width=150,height=150)
        b4_text=Button(four4,text = "Help",cursor="hand2",command=self.help_btn, font = ("roboto",15),bg = "white",fg = "blue")
        b4_text.place(x=700,y=250,width=150,height=40)

        #button image5
        btn5 = Image.open(r"imagesfrs\traindata.png")
        btn5 = btn5.resize((150,150),Image.LANCZOS)
        self.photobtn5 = ImageTk.PhotoImage(btn5)
        b5=Button(four4,image = self.photobtn5,command=self.train_button,cursor="hand2")
        b5.place(x=900,y=100,width=150,height=150)
        b5_text=Button(four4,text = "Train Data",command=self.train_button,cursor="hand2", font = ("roboto",15),bg = "white",fg = "blue")
        b5_text.place(x=900,y=250,width=150,height=40)

        #button image6
        btn6 = Image.open(r"imagesfrs\photos.webp")
        btn6 = btn6.resize((150,150),Image.LANCZOS)
        self.photobtn6 = ImageTk.PhotoImage(btn6)
        b6=Button(four4,image = self.photobtn6,command=self.open_img,cursor="hand2")
        b6.place(x=300,y=300,width=150,height=150)
        b6_text=Button(four4,text = "Photos",cursor="hand2",command=self.open_img, font = ("roboto",15),bg = "white",fg = "blue")
        b6_text.place(x=300,y=450,width=150,height=40)

         #button image7
        btn7 = Image.open(r"imagesfrs\developer.webp")
        btn7 = btn7.resize((150,150),Image.LANCZOS)
        self.photobtn7 = ImageTk.PhotoImage(btn7)
        b7=Button(four4,image = self.photobtn7,command=self.dev_btn,cursor="hand2")
        b7.place(x=500,y=300,width=150,height=150)
        b7_text=Button(four4,text = "Developer",command=self.dev_btn,cursor="hand2", font = ("roboto",15),bg = "white",fg = "blue")
        b7_text.place(x=500,y=450,width=150,height=40)

         #button image8
        btn8 = Image.open(r"imagesfrs\exit.jpg")
        btn8 = btn8.resize((150,150),Image.LANCZOS)
        self.photobtn8 = ImageTk.PhotoImage(btn8)
        b8=Button(four4,image = self.photobtn8,command=self.iexit,cursor="hand2")
        b8.place(x=700,y=300,width=150,height=150)
        b8_text=Button(four4,text = "Exit",cursor="hand2",command=self.iexit, font = ("roboto",15),bg = "white",fg = "blue")
        b8_text.place(x=700,y=450,width=150,height=40)
    
    def open_img(self):
         os.startfile("data")

    def iexit(self):
         self.iexit = tkinter.messagebox.askyesno("Warning","Are you sure you want to exit this application?",parent=self.root)
         if self.iexit>0:
              self.root.destroy()
         else:
              return


    #button functions
    def student_details(self):
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)
    def train_button(self):
         self.new_window=Toplevel(self.root)
         self.app=Train(self.new_window)
    def facerecognition_button(self):
         self.new_window=Toplevel(self.root)
         self.app=Face_recognition(self.new_window)
    def attendance_button(self):
         self.new_window=Toplevel(self.root)
         self.app=Attendance(self.new_window)
    def dev_btn(self):
         self.new_window=Toplevel(self.root)
         self.app=Developer(self.new_window)
    def help_btn(self):
         self.new_window=Toplevel(self.root)
         self.app=Help(self.new_window)
         









if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
