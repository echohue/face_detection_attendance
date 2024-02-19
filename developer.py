from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
 
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Developer")
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",30,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1300,height=35)

        bgimg = Image.open(r"imagesfrs\devbg.jpg")
        bgimg = bgimg.resize((1300,600),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(bgimg)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=40,width=1300,height=600)

        #frame
        main_frame = Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=700,y=10,width=400,height=500)

        #developer info
        dev_label=Label(main_frame,text="The name of the developer is Harshika Singh",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=0,y=5)
        dev_label1=Label(main_frame,text="The project was built using Python",font=("times new roman",13,"bold"),bg="white")
        dev_label1.place(x=0,y=30)
        dev_label2=Label(main_frame,text="The project will help with attendance",font=("times new roman",13,"bold"),bg="white")
        dev_label2.place(x=0,y=55)






if __name__ == "__main__":
    root = Tk()
    obj=Developer(root)
    root.mainloop()
