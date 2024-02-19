from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2



class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Student Details")

        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_stdid=StringVar()
        self.var_stdname=StringVar()
        self.var_div=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        

        #upper image
        img = Image.open(r"C:\Users\shars\OneDrive\Desktop\facerecognition\imagesfrs\upperstudent1.jpg")
        img = img.resize((500,100),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        first1 = Label(self.root,image = self.photoimg)
        first1.place(x=0,y=0,width=500,height=100)

        img1 = Image.open(r"C:\Users\shars\OneDrive\Desktop\facerecognition\imagesfrs\upperstudent2.jpg")
        img1 = img1.resize((500,100),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        sec2 = Label(self.root,image = self.photoimg1)
        sec2.place(x=500,y=0,width=500,height=100)

        img2 = Image.open(r"C:\Users\shars\OneDrive\Desktop\facerecognition\imagesfrs\upperstudent3.jpg")
        img2 = img2.resize((500,100),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        third3 = Label(self.root,image = self.photoimg2)
        third3.place(x=1000,y=0,width=500,height=100)

        #background image
        imgbg = Image.open(r"C:\Users\shars\OneDrive\Desktop\facerecognition\imagesfrs\collegebg.jpg")
        imgbg = imgbg.resize((1500,710),Image.ANTIALIAS)
        self.photoimgbg = ImageTk.PhotoImage(imgbg)
        four4 = Label(self.root,image = self.photoimgbg)
        four4.place(x=0,y=100,width=1500,height=710)
        title = Label(four4,text = "Student Management System", font = ("roboto",20,"bold"),bg = "white",fg = "blue")
        title.place(x=0,y=0,width=1350,height=45)
        back_btn = Button(title,text = "Back",command=self.backbtn,width=50,font = ("times new roman",12),bg="blue")
        back_btn.place(x=1100,y=0,width=60,height=40)


        #frame1
        main_frame = Frame(four4,bd=2)
        main_frame.place(x=10,y=50,width=1350,height=500)

        #leftframe
        left_frame = LabelFrame(main_frame,bd = 2,relief = RIDGE,text = "Student Details",font = ("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=600,height=450)
       

        #currentcourse
        curr_course = LabelFrame(left_frame,bd = 2,relief = RIDGE,text = "Course Info",font = ("times new roman",12,"bold"))
        curr_course.place(x=0,y=15,width=590,height=100)
        #department
        dep_label=Label(curr_course,text="Department",font = ("times new roman",12),bg="white")
        dep_label.grid(row=0,column=0,padx=10)
        dep_dropdown = ttk.Combobox(curr_course,textvariable=self.var_dep,font = ("times new roman",12),state="readonly")
        dep_dropdown["values"] = ("Select Department","BTECH","BBA","BA")
        dep_dropdown.current(0)
        dep_dropdown.grid(row=0,column=1,padx=2,pady=5)

        #course
        course_label = Label(curr_course,text = "Course",font = ("times new roman",12),bg="white")
        course_label.grid(row=0,column=2,padx=10)
        course_dropdown = ttk.Combobox(curr_course,textvariable=self.var_course,font = ("times new roman",12),state="readonly")
        course_dropdown["values"] = ("Select Course","course1","course2","course3")
        course_dropdown.current(0)
        course_dropdown.grid(row=0,column=3,padx=2,pady=5)
        
        #year
        year_label = Label(curr_course,text = "Year",font = ("times new roman",12),bg="white" )
        year_label.grid(row=1,column=0,padx=10)
        year_dropdown = ttk.Combobox(curr_course,textvariable=self.var_year,font = ("times new roman",12),state="readonly")
        year_dropdown["values"] = ("Select year","1","2","3")
        year_dropdown.current(0)
        year_dropdown.grid(row=1,column=1,padx=2,pady=5)

        #semester
        sem_label = Label(curr_course,text = "Semester",font = ("times new roman",12),bg="white" )
        sem_label.grid(row=1,column=2,padx=10)
        sem_dropdown = ttk.Combobox(curr_course,textvariable=self.var_semester,font = ("times new roman",12),state="readonly")
        sem_dropdown["values"] = ("Select semester","I","II","III","IV")
        sem_dropdown.current(0)
        sem_dropdown.grid(row=1,column=3,padx=2,pady=5)

        #classstudentinfo
        class_frame = LabelFrame(left_frame,bd=2, relief = "ridge", text = "Class Student Info", font = ("times new roman",12,"bold"))
        class_frame.place(x=0,y=120,width=590,height=350)
        #student_id
        studentid_label = Label(class_frame,text="Student ID", font = ("times new roman",12),bg="white")
        studentid_label.grid(row=0,column=0,padx=10)
        studentid_entry = ttk.Entry(class_frame,textvariable=self.var_stdid,width=20,font=("times new roman",12))
        studentid_entry.grid(row=0,column=1,padx=2,pady=5)

        #studentname
        studentname_label= Label(class_frame,text="Student Name",font = ("times new roman",12),bg="white")
        studentname_label.grid(row = 0,column=2,padx=10)
        studentname_entry = ttk.Entry(class_frame,textvariable=self.var_stdname,width=20,font=("times new roman",12))
        studentname_entry.grid(row=0,column=3,padx=2,pady=5)
        
        #classdiv
        classdiv_label= Label(class_frame,text="Division",font = ("times new roman",12),bg="white")
        classdiv_label.grid(row = 1,column=0,padx=10)
        classdiv_entry = ttk.Combobox(class_frame,textvariable=self.var_div,font=("times new roman",12),state="readonly")
        classdiv_entry["values"] = ("Select section","A","B","C","D")
        classdiv_entry.current(0)
        classdiv_entry.grid(row=1,column=1,padx=2,pady=5)

        #gender
        studentgender_label = Label(class_frame,text="Gender",font=("times new roman",12),bg="white")
        studentgender_label.grid(row=1,column=2,padx=10)
        studentgender_entry = ttk.Combobox(class_frame,textvariable=self.var_gender,font=("times new roman",12),state="readonly")
        studentgender_entry["values"] = ("Select Gender","Male","Female","Other")
        studentgender_entry.current(0)
        studentgender_entry.grid(row=1,column=3,padx=2,pady=5)

        #dob
        dob_label= Label(class_frame,text="DOB",font = ("times new roman",12),bg="white")
        dob_label.grid(row = 2,column=0,padx=10)
        dob_entry = ttk.Entry(class_frame,textvariable=self.var_dob,width=20,font=("times new roman",12))
        dob_entry.grid(row=2,column=1,padx=2,pady=5)

        #email
        email_label= Label(class_frame,text="Email",font = ("times new roman",12),bg="white")
        email_label.grid(row = 2,column=2,padx=10)
        email_entry = ttk.Entry(class_frame,textvariable=self.var_email,width=20,font=("times new roman",12))
        email_entry.grid(row=2,column=3,padx=2,pady=5)

        #phoneno
        phoneno_label= Label(class_frame,text="PhoneNo",font = ("times new roman",12),bg="white")
        phoneno_label.grid(row = 3,column=0,padx=10)
        phoneno_entry = ttk.Entry(class_frame,textvariable=self.var_phone,width=20,font=("times new roman",12))
        phoneno_entry.grid(row=3,column=1,padx=2,pady=5)

        #address
        address_label= Label(class_frame,text="Address",font = ("times new roman",12),bg="white")
        address_label.grid(row = 3,column=2,padx=10)
        address_entry = ttk.Entry(class_frame,textvariable=self.var_address,width=20,font=("times new roman",12))
        address_entry.grid(row=3,column=3,padx=2,pady=5)

        #radiobuttons
        self.var_radiobtn1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_frame,variable=self.var_radiobtn1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=4,column=0)
        self.var_radiobtn2 = StringVar()
        radiobtn2 = ttk.Radiobutton(class_frame,variable=self.var_radiobtn2,text="No photo sample",value="No")
        radiobtn2.grid(row=4,column=1)

        #button_frame
        btn_frame = LabelFrame(class_frame)
        btn_frame.place(x=0,y=170,width=590,height=200)


        #buttons
        save_btn = Button(btn_frame,text = "Save",command=self.add_data,width=15,font = ("times new roman",12),bg="blue")
        save_btn.grid(row=0,column=0, padx=25,pady=5)

        update_btn = Button(btn_frame,text = "Update",command=self.update_data,width=15,font = ("times new roman",12),bg="blue")
        update_btn.grid(row=0,column=1, padx=25,pady=5)

        delete_btn = Button(btn_frame,text = "Delete",command=self.delete_data,width=15,font = ("times new roman",12),bg="blue")
        delete_btn.grid(row=0,column=2, padx=25,pady=5)

        reset_btn = Button(btn_frame,text = "Reset",command=self.reset_data,width=15,font = ("times new roman",12),bg="blue")
        reset_btn.grid(row=1,column=0, padx=25,pady=5)

        takephoto_btn = Button(btn_frame,text = "Take Photo Sample",command=self.generate_dataset,width=15,font = ("times new roman",12),bg="blue")
        takephoto_btn.grid(row=1,column=1, padx=25,pady=5)

        updatephoto_btn = Button(btn_frame,text = "Update Photo Sample",width=15,font = ("times new roman",12),bg="blue")
        updatephoto_btn.grid(row=1,column=2, padx=25,pady=5)



        #rigthframe
        right_frame = LabelFrame(main_frame,bd = 2,relief = RIDGE,text = "Student Details",font = ("times new roman",12,"bold"))
        right_frame.place(x=620,y=10,width=600,height=450)

        #search system
        search_frame = LabelFrame(right_frame,bd=2,relief = RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=0,y=0,width = 590,height=130)

        search_label = Label(search_frame,text="Search by",font = ("times new roman",14),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5)
        search_combo = ttk.Combobox(search_frame,font=("times new roman",14),state="readonly")
        search_combo["values"] = ("Search","StudentId","PhoneNo")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10)
        search_entry = ttk.Entry(search_frame,width=20,font=("times new roman",13))
        search_entry.grid(row=0,column=2,padx=10,pady=5)
        search_btn = Button(search_frame,text="Search",width=15,font=("times new roman",13),bg="blue",fg="white")
        search_btn.grid(row=1,column=0,padx=10,pady=5)
        showall_btn = Button(search_frame,text="Show All",width=15,font=("times new roman",13),bg="blue",fg="white")
        showall_btn.grid(row=1,column=1,padx=10,pady=5)

        #tablefordata
        table_frame = Label(right_frame,bd=2,bg="white",relief="ridge")
        table_frame.place(x=0,y=140,width=590,height=290)

        #scrollbar
        scrollx = ttk.Scrollbar(table_frame,orient="horizontal")
        scrolly = ttk.Scrollbar(table_frame,orient="vertical")

        self.student_table=ttk.Treeview(table_frame,column=("ID","Dep","Course","Year","Sem","Name","Div","Gender","DOB","Email","PhoneNo","Address","Photo"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side="bottom",fill=X)
        scrolly.pack(side="right",fill=Y)
        scrollx.config(command=self.student_table.xview)
        scrolly.config(command=self.student_table.yview)

        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("ID",text="StudentID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Div",text="Division")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("PhoneNo",text="PhoneNo")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data() 
    
    #adding data function
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stdname.get()=="" or self.var_stdid.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="127.0.0.1", username="root", password="C5V7A9X8!c", database="frs", port="3307")
                my_cursor = conn.cursor()
                photo_sample = ""
                if self.var_radiobtn1.get() == "Yes":
                    photo_sample = "Yes"
                elif self.var_radiobtn2.get() == "No":
                    photo_sample = "No"
                my_cursor.execute("INSERT INTO students VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                self.var_stdid.get(),
                                self.var_dep.get(),
                                self.var_course.get(),
                                self.var_year.get(),
                                self.var_semester.get(),
                                self.var_stdname.get(),
                                self.var_div.get(),
                                self.var_gender.get(),
                                self.var_dob.get(),
                                self.var_email.get(),
                                self.var_phone.get(),
                                self.var_address.get(),
                                photo_sample
                            ))
                conn.commit()

                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added",parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error",f"Due to:{str(ex)}",parent=self.root)

    #fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="127.0.0.1", username="root", password="C5V7A9X8!c", database="frs", port="3307")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM students")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #get cursor
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_stdid.set(data[0]),
        self.var_dep.set(data[1]),
        self.var_course.set(data[2]),
        self.var_year.set(data[3]),
        self.var_semester.set(data[4]),
        self.var_stdname.set(data[5]),
        self.var_div.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_address.set(data[11]),
        self.var_radiobtn2.set(data[12])
    #update function
    def update_data(self):
            if self.var_dep.get()=="Select Department" or self.var_stdname.get()=="" or self.var_stdid.get()=="":
               messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                try:
                    Update = messagebox.askyesno("Update","Do you want to update?",parent=self.root)
                    if Update>0:
                            conn = mysql.connector.connect(host="127.0.0.1", username="root", password="C5V7A9X8!c", database="frs", port="3307")
                            my_cursor = conn.cursor()
                            my_cursor.execute("UPDATE students SET Dep=%s,Course=%s,Year=%s,Sem=%s,Name=%s,`Div`=%s,Gender=%s,DOB=%s,Email=%s,PhoneNo=%s,Address=%s,Photo=%s WHERE ID=%s",(
                               
                                self.var_dep.get(),
                                self.var_course.get(),
                                self.var_year.get(),
                                self.var_semester.get(),
                                self.var_stdname.get(),
                                self.var_div.get(),
                                self.var_gender.get(),
                                self.var_dob.get(),
                                self.var_email.get(),
                                self.var_phone.get(),
                                self.var_address.get(),
                                self.var_radiobtn2.get(),
                                self.var_stdid.get()


                             ))
                            
                    else:
                        if not Update:
                            return
                    messagebox.showinfo("Success","Successfully updates details",parent=self.root)
                   
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                            
                    
                    
                except Exception as ex:
                    messagebox.showerror("Error",f"Due to:{str(ex)}",parent=self.root)
    
    #delete function
    def delete_data(self):
        if self.var_stdid.get()=="":
            messagebox.showerror("Error","Student ID is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Confirm","Do you want to delete the student info?",parent=self.root)
                if delete>0:
                        conn = mysql.connector.connect(host="127.0.0.1", username="root", password="C5V7A9X8!c", database="frs", port="3307")
                        my_cursor = conn.cursor()
                        sql="DELETE FROM students WHERE ID=%s"
                        val=(self.var_stdid.get(),)
                        my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Message successfully deleted")
            except Exception as ex:
                messagebox.showerror("Error",f"Due to:{str(ex)}",parent=self.root)
    #reset data
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_stdname.set(""),
        self.var_div.set("Select Section"),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_radiobtn2.set(""),
        self.var_radiobtn1.set(""),
        self.var_stdid.set("")

#take photo samples
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_stdname.get()=="" or self.var_stdid.get()=="":
                    messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
               conn = mysql.connector.connect(host="127.0.0.1", username="root", password="C5V7A9X8!c", database="frs", port="3307")
               my_cursor = conn.cursor()
               my_cursor.execute("SELECT * FROM students")
               myresult = my_cursor.fetchall()
               id=0
               for x in myresult:
                id+=1
               my_cursor.execute("UPDATE students set Dep=%s,Course=%s,Year=%s,Sem=%s,Name=%s,`Div`=%s,Gender=%s,DOB=%s,Email=%s,PhoneNo=%s,Address=%s,Photo=%s WHERE ID=%s ",(
                                self.var_dep.get(),
                                self.var_course.get(),
                                self.var_year.get(),
                                self.var_semester.get(),
                                self.var_stdname.get(),
                                self.var_div.get(),
                                self.var_gender.get(),
                                self.var_dob.get(),
                                self.var_email.get(),
                                self.var_phone.get(),
                                self.var_address.get(),
                                self.var_radiobtn2.get(),
                                self.var_stdid.get()==id+1
                    
               ))
               conn.commit()
               self.fetch_data()
               self.reset_data()
               conn.close()
               face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
               def face_cropped(img):
                   gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                   faces=face_classifier.detectMultiScale(gray,1.3,5)
                   for(x,y,w,h) in faces:
                       face_cropped=img[y:y+h,x:x+w]
                       return face_cropped
               cap=cv2.VideoCapture(0)
               img_id=0
               while True:
                   ret,my_frame=cap.read()
                   if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face",face)
                   if cv2.waitKey(1)==13 or int(img_id)==100:
                       break
               cap.release()
               cv2.destroyAllWindows()
               messagebox.showinfo("Success","Generating dataset completed")
            except Exception as ex:
                messagebox.showerror("Error",f"Due to:{str(ex)}",parent=self.root)
    
    def backbtn(self):
            self.root.destroy()
            





    

        









if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()