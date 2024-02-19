from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
import os

class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Help")
        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",30,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1300,height=35)

        bgimg = Image.open(r"imagesfrs\helpdesk.jpg")
        bgimg = bgimg.resize((1300,600),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(bgimg)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=40,width=1300,height=600)

        #frame
        main_frame = Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=400,y=60,width=400,height=500)

        dev_label=Label(main_frame,text="  CONTACT US",font=("times new roman",20,"bold"),bg="white",fg="red")
        dev_label.place(x=0,y=5)
        dev_label1=Label(main_frame,text="For any issues or queries",font=("times new roman",13,"bold"),bg="white")
        dev_label1.place(x=0,y=40)
        dev_label2=Label(main_frame,text="Customer Support No. :123456890",font=("times new roman",13,"bold"),bg="white")
        dev_label2.place(x=0,y=65)
        dev_label2=Label(main_frame,text="Email:abc@gmail.com",font=("times new roman",13,"bold"),bg="white")
        dev_label2.place(x=0,y=90)


if __name__=="__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()