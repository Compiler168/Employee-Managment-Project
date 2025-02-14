from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import os  # Import os module
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import psycopg2
from datetime import datetime


class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Employee Management System")
                # Database Connection
        try:
            self.conn = psycopg2.connect(
                host="localhost", database="Final", user="postgres", password="Majid345"
            )
            self.cursor = self.conn.cursor()
        except Exception as ex:
            messagebox.showerror("Database Error", f"Error connecting to database: {str(ex)}")
            exit()


        #varible
        self.var_Dep=StringVar()
        self.var_Name=StringVar()
        self.var_Designation=StringVar()
        self.var_Email=StringVar()
        self.var_MarriedStatus=StringVar()
        self.var_EmployeeID=StringVar()
        self.var_DOB=StringVar()
        self.var_DOJ=StringVar()
        self.var_Gender=StringVar()
        self.var_PhoneNo=StringVar()
        self.var_Country=StringVar()
        self.var_Salary=StringVar()
        

        # Title Frame
        title_frame = Frame(self.root, bg='#0F4C81')
        title_frame.place(x=0, y=0, width=1366, height=80)

        # Logo Image Path
        logo_path = "Image/Logo3.png"  # Ensure the path is correct
        try:
            image_logo = Image.open(logo_path)
            image_logo = image_logo.resize((60, 60), Image.LANCZOS)
            self.photo_Logo = ImageTk.PhotoImage(image_logo)
        except Exception as e:
            print(f"Error loading logo image from '{logo_path}': {e}")
            self.photo_Logo = None

        # Combined Frame for Logo and Title
        combined_frame = Frame(title_frame, bg='#0F4C81')
        combined_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Logo Label
        if self.photo_Logo:
            logo_label = Label(combined_frame, image=self.photo_Logo, bg='#0F4C81')
            logo_label.grid(row=0, column=0, padx=10)
        else:
            logo_label = Label(combined_frame, text='[Logo Missing]', font=('Arial', 12), bg='#0F4C81', fg='red')
            logo_label.grid(row=0, column=0, padx=10)

        # Title Label
        lbl_title = Label(
            combined_frame,
            text='Employee Management System',
            font=('Arial', 20, 'bold'),
            fg='white',
            bg='#0F4C81'
        )
        lbl_title.grid(row=0, column=1)
        
        # Image Frame
        image_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        image_frame.place(x=0, y=80, width=1366, height=120)
        
        # First Image
        try:
            img1_path = os.path.join('Image', 'Fourth.png')
            Img1 = Image.open(img1_path)
            Img1 = Img1.resize((455, 120), Image.LANCZOS)
            self.photo1 = ImageTk.PhotoImage(Img1)
            self.img_1 = Label(image_frame, image=self.photo1)
            self.img_1.place(x=0, y=0, width=455, height=120)
        except Exception as e:
            print(f"Error loading 'Fourth.png': {e}")
            self.img_1 = Label(image_frame, text="[Image Missing]", font=('Arial', 15), bg='white', fg='red')
            self.img_1.place(x=0, y=0, width=455, height=120)

        # Second Image
        try:
            img2_path = os.path.join('Image', 'second.webp')
            Img2 = Image.open(img2_path)
            Img2 = Img2.resize((455, 120), Image.LANCZOS)
            self.photo2 = ImageTk.PhotoImage(Img2)
            self.img_2 = Label(image_frame, image=self.photo2)
            self.img_2.place(x=455, y=0, width=455, height=120)
        except Exception as e:
            print(f"Error loading 'second.webp': {e}")
            self.img_2 = Label(image_frame, text="[Image Missing]", font=('Arial', 15), bg='white', fg='red')
            self.img_2.place(x=455, y=0, width=455, height=120)

        # Third Image
        try:
            img3_path = os.path.join('Image', 'third.jpg')
            Img3 = Image.open(img3_path)
            Img3 = Img3.resize((455, 120), Image.LANCZOS)
            self.photo3 = ImageTk.PhotoImage(Img3)
            self.img_3 = Label(image_frame, image=self.photo3)
            self.img_3.place(x=910, y=0, width=455, height=120)
        except Exception as e:
            print(f"Error loading 'third.jpg': {e}")
            self.img_3 = Label(image_frame, text="[Image Missing]", font=('Arial', 15), bg='white', fg='red')
            self.img_3.place(x=910, y=0, width=455, height=120)

        # Main Frame
        Main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=208, width=1250, height=600)

        # Upper Frame
        Upper_frame = LabelFrame(
            Main_frame,
            bd=2,
            relief=RIDGE,
            bg='white',
            text='Employee Information:',
            font=('Arial', 12, 'bold'),
            fg='Steel Blue'
        )
        Upper_frame.place(x=10, y=5, width=1227, height=202)

        # Down Frame
        Down_frame = LabelFrame(
            Main_frame,
            bd=2,
            relief=RIDGE,
            bg='white',
            text='Additional Information:',
            font=('Arial', 12, 'bold'),
            fg='Steel Blue'
        )
        Down_frame.place(x=10, y=213, width=1227, height=218)

        #LABLES AND ENTRIES:
        ibl_Dep=Label(Upper_frame,text='Departent',font=('Arial', 9, 'bold'),bg='white')
        ibl_Dep.grid(row=0,column=0, padx=2, sticky=W)
        combo_Dep=ttk.Combobox(Upper_frame, textvariable=self.var_Dep,font=('Arial', 9),width=23, state='readonly')
        combo_Dep['value'] = ( "Select",'HR', 'IT', 'CS', 'R&D', 'PR', 'Other')
        combo_Dep.current(0)
        combo_Dep.grid(row=0, column=1, padx=2, pady=7, sticky=W)
        #name
        ibl_Name=Label(Upper_frame,text='Name',font=('Arial', 9, 'bold'),bg='white')
        ibl_Name.grid(row=1,column=2, padx=2, sticky=W)
        txt_Name=ttk.Entry(Upper_frame, textvariable=self.var_Name, font=('Arial', 9), width=25)
        txt_Name.grid(row=1, column=3, padx=2, pady=7, sticky=W)
        #Des
        ibl_Designation=Label(Upper_frame,text='Designatione',font=('Arial', 9, 'bold'),bg='white')
        ibl_Designation.grid(row=1,column=0, padx=2, sticky=W)
        txt_Designation=ttk.Entry(Upper_frame, textvariable=self.var_Designation, font=('Arial', 9), width=25)
        txt_Designation.grid(row=1, column=1, padx=2, pady=7, sticky=W)
        #email
        ibl_Email=Label(Upper_frame,text='Email',font=('Arial', 9, 'bold'),bg='white')
        ibl_Email.grid(row=2,column=5, padx=2, sticky=W)
        txt_Email=ttk.Entry(Upper_frame,textvariable=self.var_Email, font=('Arial', 9), width=25)
        txt_Email.grid(row=2, column=6, padx=2, pady=7, sticky=W)
        #Married Status
        ibl_MarriedStatus=Label(Upper_frame,text='Married Status',font=('Arial', 9, 'bold'),bg='white')
        ibl_MarriedStatus.grid(row=0,column=5, padx=2, sticky=W)
        combo_MarriedStatus=ttk.Combobox(Upper_frame, textvariable=self.var_MarriedStatus,font=('Arial', 9),width=23, state='readonly')
        combo_MarriedStatus['value'] = ( "Select",'Married', 'UnMarried', 'Other')
        combo_MarriedStatus.current(0)
        combo_MarriedStatus.grid(row=0, column=6, padx=2, pady=7, sticky=W)
        #Employee ID
        #email
        ibl_EmployeeID=Label(Upper_frame,text='EmployeeID',font=('Arial', 9, 'bold'),bg='white')
        ibl_EmployeeID.grid(row=2,column=0, padx=2, sticky=W)
        txt_EmployeeID=ttk.Entry(Upper_frame,textvariable=self.var_EmployeeID, font=('Arial', 9), width=25)
        txt_EmployeeID.grid(row=2, column=1, padx=2, pady=7, sticky=W)
        #DOB
        ibl_DOB=Label(Upper_frame,text='DOB',font=('Arial', 9, 'bold'),bg='white')
        ibl_DOB.grid(row=3,column=0, padx=2, sticky=W)
        txt_DOB=ttk.Entry(Upper_frame,textvariable=self.var_DOB, font=('Arial', 9), width=25)
        txt_DOB.grid(row=3, column=1, padx=2, pady=7, sticky=W)
        #DOJ
        ibl_DOJ=Label(Upper_frame,text='DOJ',font=('Arial', 9, 'bold'),bg='white')
        ibl_DOJ.grid(row=3,column=2, padx=2, sticky=W)
        txt_DOJ=ttk.Entry(Upper_frame,textvariable=self.var_DOJ, font=('Arial', 9), width=25)
        txt_DOJ.grid(row=3, column=3, padx=2, pady=7, sticky=W)
        #Gender
        ibl_Gender=Label(Upper_frame,text='Gender',font=('Arial', 9, 'bold'),bg='white')
        ibl_Gender.grid(row=0,column=2, padx=2, sticky=W)
        combo_Gender=ttk.Combobox(Upper_frame, textvariable=self.var_Gender,font=('Arial', 9),width=23, state='readonly')
        combo_Gender['value'] = ( "Select",'Male', 'Female', 'Other')
        combo_Gender.current(0)
        combo_Gender.grid(row=0, column=3, padx=2, pady=7, sticky=W)
        #Phone No
        ibl_PhoneNo=Label(Upper_frame,text='Phone No',font=('Arial', 9, 'bold'),bg='white')
        ibl_PhoneNo.grid(row=3,column=5, padx=2, sticky=W)
        txt_PhoneNo=ttk.Entry(Upper_frame,textvariable=self.var_PhoneNo, font=('Arial', 9), width=25)
        txt_PhoneNo.grid(row=3, column=6, padx=2, pady=7, sticky=W)
        #Country
        ibl_Country=Label(Upper_frame,text='Country',font=('Arial', 9, 'bold'),bg='white')
        ibl_Country.grid(row=1,column=5, padx=2, sticky=W)
        txt_Country=ttk.Entry(Upper_frame, textvariable=self.var_Country, font=('Arial', 9), width=25)
        txt_Country.grid(row=1, column=6, padx=2, pady=7, sticky=W)
         #Salary
        ibl_Salary=Label(Upper_frame,text='Salary (CTC)" ',font=('Arial', 9, 'bold'),bg='white')
        ibl_Salary.grid(row=2,column=2, padx=2, sticky=W)
        txt_Salary=ttk.Entry(Upper_frame,textvariable=self.var_Salary, font=('Arial', 9), width=25)
        txt_Salary.grid(row=2, column=3, padx=2, pady=7, sticky=W)
        





        


        # Image in Upper Frame
        Image_frame = Frame(Upper_frame, bd=2, relief=RIDGE, bg='white')
        Image_frame.place(x=900, y=1, width=150, height=160)
        try:
            image_Majid = Image.open('Image/ulh.png')
            image_Majid = image_Majid.resize((145, 145), Image.LANCZOS)
            self.photoMajid = ImageTk.PhotoImage(image_Majid)
            self.image_Majid = Label(Image_frame, image=self.photoMajid)
            self.image_Majid.place(x=0, y=0, width=145, height=145)
        except Exception as e:
            print(f"Error loading 'ulh.png': {e}")

        # Button Frame
        Button_frame = Frame(Upper_frame, bd=2, relief=RIDGE, bg='white')
        Button_frame.place(x=1070, y=1, width=139, height=160)

        # Buttons
        Button_frame = Frame(Upper_frame, bd=2, relief=RIDGE, bg='white')
        Button_frame.place(x=1070, y=1, width=139, height=160)

        # Buttons
        btn_add=Button(Button_frame, text="Save", command=self.add_data, bg='#2196F3',fg='white', font=('Arial', 10, 'bold'), width=13, )
        btn_add.grid(row=1, column=0, padx=10, pady=5)
        btn_Update=Button(Button_frame,text="Update" ,command=self.update_data,bg='#FF9800',fg='white', font=('Arial', 10, 'bold'), width=13, )
        btn_Update.grid(row=2, column=0, padx=10, pady=5)
        btn_Delete=Button(Button_frame,text="Delete",command=self.Delete_data, bg='#F44336',fg='white', font=('Arial', 10, 'bold'), width=13, )
        btn_Delete.grid(row=3, column=0, padx=10, pady=5)
        btn_Clear=Button(Button_frame,text="Clear",bg='#9E9E9E',fg='white', font=('Arial', 10, 'bold'), width=13, )
        btn_Clear.grid(row=4, column=0, padx=10, pady=5)
         # Add functionality to buttons (Save, Update, Delete, Clear)

            # Search Frame
        Search_frame = LabelFrame(
            Down_frame,
            bd=2,
            relief=RIDGE,
            bg='white',
            text='Search:',
            font=('Arial', 12, 'bold'),
            fg='Steel Blue'
        )
        Search_frame.place(x=6, y=0, width=1211, height=60)
        # Search by Combo Box
        search_by = Label(Search_frame, text='Search By:', font=('Arial', 10), bg='white')
        search_by.grid(row=0, column=0, padx=5, sticky=W)
        #serach
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(Search_frame, font=('Arial', 12,'bold'), width=20, state='readonly')
        com_txt_search['value'] = ('Select', 'Employee ID', 'Name', 'Email', 'Phone')
        com_txt_search.current(0)
        com_txt_search.grid(row=0, column=1, padx=5,sticky=W)
        self.var_com_search=StringVar()
        txt_search=ttk.Entry(Search_frame, font=('Arial', 12, 'bold'), width=22)
        txt_search.grid(row=0, column=2, padx=5)

# Search Button
        btn_search = Button(Search_frame, text='Search', font=('Arial', 10, 'bold'), bg='#2196F3', fg='white', width=12)
        btn_search.grid(row=0, column=3, padx=5)

# Show All Button
        btn_show_all = Button(Search_frame, text='Show All', font=('Arial', 10, 'bold'), bg='#4CAF50', fg='white', width=12)
        btn_show_all.grid(row=0, column=4, padx=5)
        # Hide All Button
        btn_hide_all = Button(Search_frame, text='Hide All', font=('Arial', 10, 'bold'), bg='#F44336', fg='white', width=12)
        btn_hide_all.grid(row=0, column=5, padx=5)

        # TABLE_FRAME
        Table_frame = Frame(Down_frame, bd=3, relief=RIDGE)
        Table_frame.place(x=6, y=60, width=1211, height=130)
        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.Employee_table=ttk.Treeview(Table_frame,column=("Employee ID", "Dep","Name","Desi","Email","Married Status","DOB","DOJ","Gender","Phone No","Country","Salary",),xscrollcommand=scroll_x.set ,yscrollcommand=scroll_y.set )

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Employee_table.xview)
        scroll_y.config(command=self.Employee_table.yview)

        self.Employee_table.heading('Dep',text="Department")
        self.Employee_table.heading('Name',text="Name")
        self.Employee_table.heading('Desi',text="Designation")
        self.Employee_table.heading('Email',text="Email")
        self.Employee_table.heading('Married Status',text="Married Status")
        self.Employee_table.heading('Employee ID',text="Employee ID")
        self.Employee_table.heading('DOB',text="DOB")
        self.Employee_table.heading('DOJ',text="DOJ")
        self.Employee_table.heading('Gender',text="Gender")
        self.Employee_table.heading('Phone No',text="Phone No")
        self.Employee_table.heading('Country',text="Country")
        self.Employee_table.heading('Salary',text="Salary")

        self.Employee_table['show']='headings'
        self.Employee_table.column("Dep", width=100)
        self.Employee_table.column("Name",width=100)
        self.Employee_table.column("Desi",width=100)
        self.Employee_table.column("Email",width=100)
        self.Employee_table.column("Married Status",width=100)
        self.Employee_table.column("Employee ID",width=100)
        self.Employee_table.column("DOB",width=100)
        self.Employee_table.column("DOJ",width=100)
        self.Employee_table.column("Gender",width=100)
        self.Employee_table.column("Phone No",width=100)
        self.Employee_table.column("Country",width=100)
        self.Employee_table.column("Salary",width=100)
        
       

        self.Employee_table.pack(fill=BOTH,expand=1)
        self.Employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        #----------Function Declaration-----
    def add_data(self):
       if self.var_Dep.get() == "" or self.var_Email.get() == "":
        messagebox.showerror('Error', 'All fields are Required')
       else:
        try:
            # Establish database connection
            conn = psycopg2.connect(
                host='localhost',
                user='postgres',
                password='Majid345',
                database='Final'
            )
            my_cursor = conn.cursor()
            create_script = '''CREATE TABLE IF NOT EXISTS Final(
                employee_id SERIAL PRIMARY KEY,
                department VARCHAR(50),
                name VARCHAR(100),
                designation VARCHAR(100),
                email VARCHAR(100),
                married_status VARCHAR(20),
                dob DATE,
                doj DATE,
                gender VARCHAR(20),
                phone_no VARCHAR(20),
                country VARCHAR(50),
                salary VARCHAR(20)
            )'''
            my_cursor.execute(create_script)
            conn.commit()
            
            # Insert data into the employee table
            insert_query = '''INSERT INTO Final (department, name, designation, email, married_status, dob, doj, gender, phone_no, country, salary)
                  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            my_cursor.execute(insert_query, (
    self.var_Dep.get(),
    self.var_Name.get(),
    self.var_Designation.get(),
    self.var_Email.get(),
    self.var_MarriedStatus.get(),
    self.var_DOB.get(),
    self.var_DOJ.get(),
    self.var_Gender.get(),
    self.var_PhoneNo.get(),
    self.var_Country.get(),
    self.var_Salary.get()
))

            conn.commit()
            self.fetch_data()
            conn.close()
            
            messagebox.showinfo('Success', 'Employee data added successfully',parent=self.root)
        except Exception as ex:
            messagebox.showerror('Error', f'Due to: {str(ex)}',parent=self.root)
    #Fetch Data
    def fetch_data(self):
            conn = psycopg2.connect(
                host='localhost',
                user='postgres',
                password='Majid345',
                database='Final'
            )
            my_cursor = conn.cursor()
            my_cursor.execute(("SELECT * FROM Final"))
            data=my_cursor.fetchall()
            if len(data)!=0:
                self.Employee_table.delete(*self.Employee_table.get_children())
                for i in data:
                    self.Employee_table.insert("",END,values=i)
                    conn.commit()
            conn.close()
     
    #get Curoser
    def get_cursor(self,event=" "):
            cursor_row=self.Employee_table.focus()
            content=self.Employee_table.item(cursor_row)
            data=content['values']
            self.var_EmployeeID.set(data[0]) 
            self.var_Name.set(data[1])
            self.var_Designation.set(data[2])
            self.var_Email.set(data[3])
            self.var_MarriedStatus.set(data[4])
            self.var_EmployeeID.set(data[5])
            self.var_DOB.set(data[6])
            self.var_DOJ.set(data[7])
            self.var_Gender.set(data[8])
            self.var_PhoneNo.set(data[9])
            self.var_Country.set(data[10])
            self.var_Salary.set(data[11])
   # Update Data
    def update_data(self):
        if self.var_Dep.get() == "" or self.var_Email.get() == "":
            messagebox.showerror('Error', 'All fields are Required', parent=self.root)
        else:
            try:
                Update = messagebox.askyesno('Update', 'Are you sure you want to update this Employee?', parent=self.root)
                if Update:
                    # Establish database connection
                    conn = psycopg2.connect(
                        host='localhost',
                        user='postgres',
                        password='Majid345',
                        database='Final'
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                         '''UPDATE Final 
       SET name=%s, designation=%s, email=%s, married_status=%s, dob=%s, 
           doj=%s, gender=%s, phone_no=%s, country=%s, salary=%s 
       WHERE department=%s''',
                        (
                            self.var_Name.get(),
        self.var_Designation.get(),
        self.var_Email.get(),
        self.var_MarriedStatus.get(),
        self.var_DOB.get(),
        self.var_DOJ.get(),
        self.var_Gender.get(),
        self.var_PhoneNo.get(),
        self.var_Country.get(),
        self.var_Salary.get(),
        self.var_Dep.get() 
                        )
                    )
                    
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo('Success', 'Employee data updated successfully', parent=self.root)
            except Exception as ex:
                messagebox.showerror('Error', f'Due to: {str(ex)}', parent=self.root)
    # Delete Data
    def Delete_data(self):
        if self.var_EmployeeID.get() == "":
            messagebox.showerror('Error', 'All fields are Required', parent=self.root)
        else:
            try:
                Update = messagebox.askyesno('Update', 'Are you sure you want to Delete this Employee?', parent=self.root)
                if Update:
                    # Establish database connection
                    conn = psycopg2.connect(
                        host='localhost',
                        user='postgres',
                        password='Majid345',
                        database='Final'
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        '''UPDATE Final 
       SET name=%s, designation=%s, email=%s, married_status=%s, dob=%s, 
           doj=%s, gender=%s, phone_no=%s, country=%s, salary=%s 
       WHERE department=%s''',
                        (
                           self.var_Name.get(),
        self.var_Designation.get(),
        self.var_Email.get(),
        self.var_MarriedStatus.get(),
        self.var_DOB.get(),
        self.var_DOJ.get(),
        self.var_Gender.get(),
        self.var_PhoneNo.get(),
        self.var_Country.get(),
        self.var_Salary.get(),
        self.var_Dep.get() 
                        )
                    )
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo('Success', 'Employee data updated successfully', parent=self.root)
            except Exception as ex:
                messagebox.showerror('Error', f'Due to: {str(ex)}', parent=self.root)
    





        

        

if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()
