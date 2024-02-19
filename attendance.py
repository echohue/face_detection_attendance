from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x790+0+0")
        self.root.title("Attendance")

        #variables
        self.var_attendanceid = StringVar()
        self.var_name = StringVar()
        self.var_attendance = StringVar()
        self.var_dep = StringVar()
        self.var_date = StringVar()
        self.var_time = StringVar()


        #image1
        img = Image.open(r"imagesfrs\attendance1.webp")
        img = img.resize((750,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width=750,height=150)

        #image2
        img1 = Image.open(r"imagesfrs\attendance_hands.jpg")
        img1 = img1.resize((700,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image = self.photoimg1)
        f_lbl.place(x=750,y=0,width=750,height=150)

        #bgimage
        bgimg = Image.open(r"imagesfrs\collegebg.jpg")
        bgimg = bgimg.resize((1500,600),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(bgimg)

        bgimg_label = Label(self.root,image=self.photoimg2)
        bgimg_label.place(x=0,y=130,width=1300,height=600)

        title_lbl = Label(bgimg_label,text="ATTENDANCE PAGE",font = ("times new roman",20,"bold"),bg = "white",fg = "blue")
        title_lbl.place(x=0,y=0,width=1350,height=45)

        
        #frame1
        main_frame = Frame(bgimg_label,bd=2)
        main_frame.place(x=10,y=50,width=1350,height=500)

        #leftframe
        left_frame = LabelFrame(main_frame,bd = 2,relief = RIDGE,text = "Attendance Details",font = ("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=600,height=500)

        left_frame1 = Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_frame1.place(x=5,y=5,width=590,height=480)

        #label and entry
        #attendanceid
        attendanceid_label = Label(left_frame1,text="Attendance ID", font = ("times new roman",12),bg="white")
        attendanceid_label.grid(row=0,column=0,padx=10)
        attendanceid_entry = ttk.Entry(left_frame1,width=20,textvariable=self.var_attendanceid,font=("times new roman",12))
        attendanceid_entry.grid(row=0,column=1,padx=2,pady=5)

        #studentname
        studentname_label= Label(left_frame1,text="Student Name",font = ("times new roman",12),bg="white")
        studentname_label.grid(row = 0,column=2,padx=10)
        studentname_entry = ttk.Entry(left_frame1,width=20,textvariable=self.var_name,font=("times new roman",12))
        studentname_entry.grid(row=0,column=3,padx=2,pady=5)

        #department
        dep_label= Label(left_frame1,text="Department",font = ("times new roman",12),bg="white")
        dep_label.grid(row = 1,column=0,padx=10)
        dep_entry = ttk.Combobox(left_frame1,font=("times new roman",12),textvariable=self.var_dep,state="readonly")
        dep_entry["values"] = ("Select department","BTECH","BBA","BA")
        dep_entry.current(0)
        dep_entry.grid(row=1,column=1,padx=2,pady=5)

        #time
        time_label= Label(left_frame1,text="Time",font = ("times new roman",12),bg="white")
        time_label.grid(row = 1,column=2,padx=10)
        time_entry = ttk.Entry(left_frame1,width=20,textvariable=self.var_time,font=("times new roman",12))
        time_entry.grid(row=1,column=3,padx=2,pady=5)

        #date
        date_label= Label(left_frame1,text="Date",font = ("times new roman",12),bg="white")
        date_label.grid(row = 2,column=0,padx=10)
        date_entry = ttk.Entry(left_frame1,width=20,textvariable=self.var_date,font=("times new roman",12))
        date_entry.grid(row=2,column=1,padx=2,pady=5)

        #attendance status
        attendance_label= Label(left_frame1,text="Status",font = ("times new roman",12),bg="white")
        attendance_label.grid(row = 2,column=2,padx=10)
        attendance_entry = ttk.Combobox(left_frame1,font=("times new roman",12),textvariable=self.var_attendance,state="readonly")
        attendance_entry["values"] = ("Attendance status","Present","Absent")
        attendance_entry.current(0)
        attendance_entry.grid(row=2,column=3,padx=2,pady=5)

        #button_frame
        btn_frame = LabelFrame(left_frame1,bg="white")
        btn_frame.place(x=0,y=170,width=590,height=200)


        #buttons
        import_btn = Button(btn_frame,text = "Import csv",command=self.importCsv,width=15,font = ("times new roman",12),bg="blue")
        import_btn.grid(row=0,column=0, padx=25,pady=5)

        export_btn = Button(btn_frame,text = "Export csv",command=self.exportCsv,width=15,font = ("times new roman",12),bg="blue")
        export_btn.grid(row=0,column=1, padx=25,pady=5)

        update_btn = Button(btn_frame,text = "Update",width=15,font = ("times new roman",12),bg="blue")
        update_btn.grid(row=0,column=2, padx=25,pady=5)

        reset_btn = Button(btn_frame,text = "Reset",command=self.resetbtn,width=15,font = ("times new roman",12),bg="blue")
        reset_btn.grid(row=1,column=0, padx=25,pady=5)



        #rigthframe
               
        right_frame = LabelFrame(main_frame,bd = 2,relief = RIDGE,text = "Attendance Details",font = ("times new roman",12,"bold"))
        right_frame.place(x=620,y=10,width=600,height=450)

        #table_frame
        table_frame = LabelFrame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=590,height=400)

        #scrollbar
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttedanceReportTable=ttk.Treeview(table_frame,column=("id","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command = self.AttedanceReportTable.xview)
        scroll_y.config(command = self.AttedanceReportTable.yview)

        self.AttedanceReportTable.heading("id",text="Attendance ID")
        self.AttedanceReportTable.heading("name",text="Name")
        self.AttedanceReportTable.heading("department",text="Department")
        self.AttedanceReportTable.heading("time",text="Time")
        self.AttedanceReportTable.heading("date",text="Date")
        self.AttedanceReportTable.heading("attendance",text="Attendance")
        self.AttedanceReportTable["show"] = "headings"

        self.AttedanceReportTable.pack(fill=BOTH,expand=1)
        self.AttedanceReportTable.bind("<ButtonRelease>",self.focusdata)

        #fetch data
    def fetchData(self,rows):
        self.AttedanceReportTable.delete(*self.AttedanceReportTable.get_children())
        for i in rows:
            self.AttedanceReportTable.insert("",END,values=i)


    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes = (("CSV File","*.csv"),("All Files","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes = (("CSV File","*.csv"),("All Files","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Exported","Your data exported to"+os.path.basename(fln)+" successfully")
        except Exception as ex:
            messagebox.showerror("Error",f"Due to :{str(ex)}",parent=self.root)
    
    def focusdata(self,event=""):
        dataf=self.AttedanceReportTable.focus()
        content=self.AttedanceReportTable.item(dataf)
        rows=content['values']
        self.var_attendanceid.set(rows[0])
        self.var_name.set(rows[1])
        self.var_dep.set(rows[2])
        self.var_time.set(rows[3])
        self.var_date.set(rows[4])
        self.var_attendance.set(rows[5])

    def resetbtn(self):
        self.var_attendanceid.set("")
        self.var_name.set("")
        self.var_dep.set("Select department")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("Attendance status")



            

    





        
        







if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
