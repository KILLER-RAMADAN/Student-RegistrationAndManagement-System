import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk, ImageTk, ImageDraw, ImageFont
from tkinter import filedialog, StringVar,messagebox
import tkinter.ttk
from tkinter.ttk import *
import random
from database import databsae
import os



class Student_add_account(tk.Tk):
    
    def show_student_card(self,image):
        self.labels = """
Id Number:
Name:
Age:
Gender: 
Contact: 
Class: 
Email: 
"""
        self.data=f"""
{self.sid_entry.get()}
{self.sfn_entry.get().upper()}
{self.sage_entry.get()}
{self.student_gender.get()}
{self.spn_entry.get()}
{self.select_major.get()}
{self.semail_entry.get()}
"""     
        if self.select_major.get()=="Admin":
         s_card = Image.open("images//student_card_frame.png")
         pic = Image.open(image).resize((100,100))

         s_card.paste(pic, (15, 15))
         font = ImageFont.truetype("bahnschrift", 18)
         labels_font = ImageFont.truetype("arial", 15)
         data_font = ImageFont.truetype("bahnschrift", 13)

         draw = ImageDraw.Draw(s_card)
         draw.text(xy=(150, 60), text="Admin Card", fill=(0, 0, 0), font=font)

         draw.multiline_text(xy=(15, 113), text=self.labels,
                            fill=(0, 0, 0), font=labels_font, spacing=7)

         draw.multiline_text(xy=(95, 117), text=self.data,
                            fill=(0, 0, 0), font=data_font, spacing=10)

         s_card.save(f'{self.home_directory}//card-id.png')
        else:
         s_card = Image.open("images//student_card_frame.png")
         pic = Image.open(image).resize((100,100))

         s_card.paste(pic, (15, 15))
         font = ImageFont.truetype("bahnschrift", 18)
         labels_font = ImageFont.truetype("arial", 15)
         data_font = ImageFont.truetype("bahnschrift", 13)

         draw = ImageDraw.Draw(s_card)
         draw.text(xy=(150, 60), text="Student Card", fill=(0, 0, 0), font=font)

         draw.multiline_text(xy=(15, 113), text=self.labels,
                            fill=(0, 0, 0), font=labels_font, spacing=7)

         draw.multiline_text(xy=(95, 117), text=self.data,
                            fill=(0, 0, 0), font=data_font, spacing=10)

         s_card.save(f'{self.home_directory}//card-id.png')
     
    
    
    
    
    
    
    def generat_id(self):
        self.db = databsae("students_accounts.db")
        self.ran_id = random.randint(100000, 100000000)
        self.check = self.db.check_id(id_number=self.ran_id)
        print(self.check)
        if  self.check :
            messagebox.showinfo("Id Founded","This Id Already Taken By Another Student\nTry Another Id ... ")
            self.destroy()
            self.update()
            from Home import Student_Registration
            app=Student_Registration()
            app.mainloop()  
        elif len(str(self.ran_id))<8:
            messagebox.showinfo("ID MANAGER","ID Is Not Valid For You..")    
            self.destroy()
            self.update()
            from Home import Student_Registration
            app=Student_Registration()
            app.mainloop()  
        else:
            print("Id num"+str(self.ran))
            self.sid_entry.insert("end", self.ran)
             
            self.sid_entry.configure(state="readonly")
            

    
    
    
    def open_photo(self):
     

        self.file_name = filedialog.askopenfilename(
            filetypes=(("PNG", "*.png"), ("JPG", "*.jpg"), ("JPEG", "*.jpeg")), title="Select Photo")

        if self.file_name:

         
         self.s_image.set(self.file_name)

         open = ImageTk.PhotoImage(Image.open(
             self.file_name).resize((100, 100)))

         self.open_student_photo.configure(image=open)

         self.open_student_photo.image = open

        return print(self.s_image)
    
    def check_empty(self):
        
        Basic_mail="@gmail.com"
        if self.sfn_entry.get()=="" and self.spn_entry.get()=="" and self.saccpass_entry.get()=="" and self.semail_entry.get()=="" and self.sage_entry.get()=="" and self.spn_entry.get()=="":
            messagebox.showerror("Error","Make Sure To Fill ALL Fields....")
            self.sfn_entry.configure(highlightbackground="red")
            self.spn_entry.configure(highlightbackground="red")
            self.saccpass_entry.configure(highlightbackground="red")
            self.semail_entry.configure(highlightbackground="red")
            self.sage_entry.configure(highlightbackground="red")
            self.spn_entry.configure(highlightbackground="red")
        
        elif self.sfn_entry.get()=="":
            messagebox.showerror("Error", "Make Sure To Fill ALL Fields....")
            self.sfn_entry.configure(highlightbackground="red")
            
        elif self.spn_entry.get() == "":
            messagebox.showerror("Error", "Make Sure To Fill ALL Fields....")
            self.spn_entry.configure(highlightbackground="red")
            
        elif self.saccpass_entry.get() == "":
            messagebox.showerror("Error", "Make Sure To Fill ALL Fields....")
            self.saccpass_entry.configure(highlightbackground="red")
            
        elif len(self.saccpass_entry.get())<8:
            messagebox.showerror("Error", "Password Should be At Least 8 Char....")
            self.saccpass_entry.configure(highlightbackground="red")
            
        elif len(self.sage_entry.get())>2:
            messagebox.showerror("Error","You Are Very Old 😁 Enter Correct Age.")
            
        elif len(self.sfn_entry.get())>15:
            messagebox.showerror("Error","Enter Correct Name..")
        
    
    
        elif self.semail_entry.get()=="":
            messagebox.showerror("Error", "Make Sure To Fill ALL Fields....")
            self.semail_entry.configure(highlightbackground="red")
        
        elif self.sage_entry.get() == "":
            messagebox.showerror("Error", "Make Sure To Fill ALL Fields....")
            self.sage_entry.configure(highlightbackground="red")
        
        elif self.spn_entry.get() == "":
            messagebox.showerror("Error", "Make Sure To Fill ALL Fields....")
            self.spn_entry.configure(highlightbackground="red")
        
        elif Basic_mail not in self.semail_entry.get():
            messagebox.showerror("Error", "Enter Correct Mail !!")
            self.semail_entry.configure(highlightbackground="red")
            
        else:
            if self.s_image.get()!="":
             self.db = databsae("students_accounts.db")
             self.resize_bic=Image.open(self.s_image.get()).resize((100,100))
             self.resize_bic.save(f"students_images//student-id[{self.sid_entry.get()}].png")
             with open(f"students_images//student-id[{self.sid_entry.get()}].png", "rb") as f:
                self.image=f.read()
            
             self.db.insert_date(self.sid_entry.get(),
                                self.sfn_entry.get(),
                                self.student_gender.get(),
                                self.sage_entry.get(),
                                self.spn_entry.get(),
                                self.select_major.get(),
                                self.semail_entry.get(),
                                self.image,
                                self.saccpass_entry.get()
                                )
             messagebox.showinfo("Congratulations","Successfully Create Account...")
             self.show_student_card(self.s_image.get())
             self.destroy()
             self.update()
             from student_card_page import Student_card
             app=Student_card()
             app.mainloop()
             
            else:
             self.db = databsae("students_accounts.db")
             self.resize_bic=Image.open("images//student.png").resize((100,100))
             self.resize_bic.save(f"students_images//default-student.png")
             with open(f"students_images//default-student.png", "rb") as f:
                self.image=f.read()
            
             self.db.insert_date(self.sid_entry.get(),
                                self.sfn_entry.get(),
                                self.student_gender.get(),
                                self.sage_entry.get(),
                                self.spn_entry.get(),
                                self.select_major.get(),
                                self.semail_entry.get(),
                                self.image,
                                self.saccpass_entry.get()
                                )
             messagebox.showinfo("Congratulations","Successfully Create Account...")
             self.show_student_card("students_images//default-student.png")
             self.destroy()
             self.update()
             from student_card_page import Student_card
             app=Student_card()
             app.mainloop()
             
                
        
            
        
    
    def remove_highlight_warning(self,entry):
        if entry["highlightbackground"]!="grey":
            if entry.get()!="":
                entry.config(highlightcolor=self.bg_color,highlightbackground="green")
                
    
    def pack_home(self):
        x=messagebox.askokcancel("EXIT","Do You Want To Leave Registration Form !?")
        if x:
         self.destroy()
         self.update()
         from Home import Student_Registration
         app = Student_Registration()
         app.mainloop()
         
    
    

    def __init__(self):

        super().__init__()
        
        self.home_directory = os.path.expanduser( '~' )

        self.iconbitmap("images//aou.ico")

        self.geometry("500x600+550+100")

        self.title("Add New Student Account")

        self.overrideredirect(1)

        self.resizable(0, 0)

        self.attributes("-topmost", True)

        self.bg_color = "#273b7a"
        
        self.student_gender = tk.StringVar()
        
        self.s_image=tk.StringVar()
        
        self.s_image.set("")
        
        # images #
        
        self.student_img = Image.open("images//student.png").resize((100, 100))
        self.student_img = ImageTk.PhotoImage(self.student_img)
        
        # images #
        
        self.account_page_frame = tk.Frame(
            bg="white", highlightbackground=self.bg_color, highlightthickness=3)

        self.account_page_frame.pack(pady=5)

        self.account_page_frame.configure(width=480, height=580)
        
        self.open_student_photo = tk.Button(
            self.account_page_frame, image=self.student_img,command=self.open_photo, bg="#273b7a", relief="flat", bd=0, activebackground="#273b7a")
        
        self.open_student_photo.place(x=5,y=5)
        
        # self.open_student_photo.configure(state="disabled")
        
        
        self.s_full_name=tk.Label(self.account_page_frame,text="Enter Student Full Name:",font=("Bold",12),bg="white")
        
        self.s_full_name.place(x=5,y=130)
        
        
        self.sfn_entry=tk.Entry(self.account_page_frame,font=("bold",15),bg="white",highlightbackground="#273b7a",highlightthickness=3)
        
        self.sfn_entry.place(x=5,y=160,width=180)
        
        self.sfn_entry.bind(
            "<KeyRelease>", lambda e: self.remove_highlight_warning(self.sfn_entry))
        
        self.gender_label = tk.Label(
            self.account_page_frame, text="Select Student Gender:", font=("Bold", 12), bg="white")
        self.gender_label.place(x=5,y=210)
        
        
        self.male_button = tk.Radiobutton(text="Male", font=(
            "Bold", 12), bg="white", activebackground="white", variable=self.student_gender,value="Male")

        self.male_button.place(x=20,y=253)
        
        self.female_button = tk.Radiobutton(text="Female", font=(
            "Bold", 12), bg="white", activebackground="white", variable=self.student_gender, value="Female")
        
        self.student_gender.set("Male")

        self.female_button.place(x=95, y=253)
        
        self.sage_label = tk.Label(
            self.account_page_frame, text="Enter Student Age:", font=("Bold", 12), bg="white")
        self.sage_label.place(x=5, y=285)
        
        self.sage_entry=tk.Entry(self.account_page_frame,font=("bold",15),bg="white",highlightbackground="#273b7a",highlightthickness=3)
        
        self.sage_entry.place(x=5,y=315,width=180)
        
        self.sage_entry.bind(
            "<KeyRelease>", lambda e: self.remove_highlight_warning(self.sage_entry))
        
        self.scontact_label = tk.Label(
            self.account_page_frame, text="Enter Contact Phone Number:", font=("Bold", 12), bg="white")
        self.scontact_label.place(x=5, y=370)
        
        self.spn_entry=tk.Entry(self.account_page_frame,font=("bold",15),bg="white",highlightbackground="#273b7a",highlightthickness=3)
        
        self.spn_entry.place(x=5,y=400,width=180)
        
        self.spn_entry.bind(
            "<KeyRelease>", lambda e: self.remove_highlight_warning(self.spn_entry))

        self.smajor_label = tk.Label(
            self.account_page_frame, text="Select Student Major:", font=("Bold", 12), bg="white")
        self.smajor_label.place(x=5, y=455)
        
        self.select_major=tkinter.ttk.Combobox(self.account_page_frame,font=("Bold",12),values=["DS","WT","WD","Cyber-Security","AI","CS","Media","Admin"],state="readonly")
        self.select_major.set("DS")
        self.select_major.place(x=4,y=495,width=180,height=30)
        
        self.sid_label = tk.Label(
            self.account_page_frame, text="Student Id Number:", font=("Bold", 12), bg="white")
        self.sid_label.place(x=240, y=35)
        
        self.sid_entry = tk.Entry(self.account_page_frame, font=(
            "bold", 12), bg="white", highlightbackground="#273b7a", highlightthickness=3)

        self.sid_entry.place(x=380, y=35, width=80)
        self.ran = random.randint(10000, 100000000)
        
        
        
        
    
        
        
        self.id_info_lbl=tk.Label(text="Automatically Generated ID Number\nRemember To Use This ID Number\nIn Account Login.. ",justify="left",bg="white")
        
        self.id_info_lbl.place(x=250,y=79)
        
        self.semail_label = tk.Label(
            self.account_page_frame, text="Enter Student Email:", font=("Bold", 12), bg="white")
        self.semail_label.place(x=240, y=130)
        
        self.semail_entry = tk.Entry(self.account_page_frame, font=(
            "bold", 15), bg="white", highlightbackground="#273b7a", highlightthickness=3)
        
        self.semail_entry.bind(
            "<KeyRelease>", lambda e: self.remove_highlight_warning(self.semail_entry))

        self.semail_entry.place(x=240, y=160, width=180)
        
        self.email_info_lbl = tk.Label(
            text="Via Email Address Student Can\nRecover Account\n! In Case Forgetting Password\nAnd Also Student Will Get Future\nNotification", justify="left", bg="white")

        self.email_info_lbl.place(x=250, y=210)
        
        self.saccpass_label = tk.Label(
            self.account_page_frame, text="Create Account Password", font=("Bold", 12), bg="white")
        self.saccpass_label.place(x=240, y=288)
        
        self.saccpass_entry = tk.Entry(self.account_page_frame, font=(
            "bold", 15), bg="white", highlightbackground="#273b7a", highlightthickness=3)
        
        self.saccpass_entry.bind(
            "<KeyRelease>", lambda e: self.remove_highlight_warning(self.saccpass_entry))

        self.saccpass_entry.place(x=240, y=317, width=180)
        
        self.accpass_info_lbl = tk.Label(
            text="Via Student Created Password And\nProvided Student ID number\nStudent Can Login Account. ", justify="left", bg="white")

        self.accpass_info_lbl.place(x=250, y=365)
        
        
        
        self.home_button=tk.Button(text="Home",command=self.pack_home,bg="red",fg="white",font=("Bold",15),bd=0,activebackground="red",activeforeground="white")
        
        self.home_button.place(x=250,y=430)
        
        self.Submit_button = tk.Button(text="Submit",command=self.check_empty, bg="#273b7a", fg="white", font=(
            "Bold", 15), bd=0, activebackground="#273b7a", activeforeground="white")

        self.Submit_button.place(x=360, y=430)
        
        
        self.generat_id()



# app=Student_add_account()
# app.mainloop()