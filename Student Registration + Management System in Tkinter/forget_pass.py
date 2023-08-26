import tkinter as tk
from tkinter import *
import PIL
from PIL import Image, ImageTk
from database import databsae
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import my_email 

class Forget_Pass_page(tk.Tk):
    
    
    def send_mail(self,mail,body,Subject):
        smtp_server="smtp.gmail.com"
        smtp_port=587
        
        username=my_email.defualt_email
        passw=my_email.email_password
        
        msg=MIMEMultipart()
        
        msg['Subject']=Subject
        msg['From']=username
        msg['To']=mail
        
        msg.attach(MIMEText(_text=body,_subtype="html"))
        
        smtp_connection=smtplib.SMTP(host=smtp_server,port=smtp_port)
        
        smtp_connection.starttls()
        
        smtp_connection.login(user=username,password=passw)
        
        smtp_connection.sendmail(from_addr=username,to_addrs=mail,msg=msg.as_string())
        
        print("Mail Send Successfully....")



    
    def check_id(self):
        
        if self.student_id_entry.get()=="":
            messagebox.showinfo("Invalid Input","Empty Faild !!! ")
            
        elif len(self.student_id_entry.get())<8:
            messagebox.showerror("Id Manager","Invalid Id Should Be At Least 8 Char..")
        
        else:
         self.db=databsae("students_accounts.db")
         get_id=self.db.check_id(self.student_id_entry.get())
         if get_id:
            self.db=databsae("students_accounts.db")
            self.a_pass=self.db.get_pass(self.student_id_entry.get())
            self.db=databsae("students_accounts.db")
            self.a_mail=self.db.get_email(self.student_id_entry.get())
            x=messagebox.askokcancel("Sending",f"We Will Send\nYour Forget Password\nVia Your Email Address:\n{self.a_mail}\nDo You Want To Continue!?")
            if x:
                msg=f"""<h1>👇 Your Forget Password Is</h1>
                <h2>{self.a_pass}</h2>
                <p>Once Remember Your Password After Deleting This Message...</P>"""
                
                self.send_mail(mail=self.a_mail,body=msg,Subject="Password Recovery")
                messagebox.showinfo("Done!","Successfully Sending Password Process...")

            
         else:
            messagebox.showerror("Error",f"Your Id Not Found...")
    
    def back_home(self):
        self.destroy()
        self.update()
        from Home import Student_Registration
        app=Student_Registration()
        app.mainloop()
        
    
    
        

    def __init__(self):
        super().__init__()

        self.lock = False

        self.iconbitmap("images//aou.ico")

        self.geometry("500x300+550+200")

        self.title("Forget Password Page")
        
        self.overrideredirect(1)

        self.resizable(0, 0)

        self.attributes("-topmost", True)

    
        self.bg_color = "#273b7a"
        
        
        # images #
        
        
        
        
        
        
        
        # images #
        
        self.arrow_pack_img = Image.open(
            "images//previous.png").resize((30, 30))

        self.arrow_pack_img = ImageTk.PhotoImage(self.arrow_pack_img)
        
        
        # Frame #
        
        
        self.header_forget_frame = tk.Frame(
            bg="#FAF9F6", highlightthickness=3, highlightbackground=self.bg_color)

        self.header_forget_frame.pack(pady=30)

        self.header_forget_frame.configure(width=350, height=250)
        
        
        self.header_text = tk.Label(
            self.header_forget_frame, text="Forgetting Password", bg=self.bg_color, fg="white", font=("Bold", 18))

        self.header_text.place(x=0, y=0, width=350)
        
        
        
        self.pack_home = tk.Button(
            self.header_forget_frame,command=self.back_home, image=self.arrow_pack_img, bg="#FAF9F6", bd=0, activebackground="#FAF9F6")

        self.pack_home.place(x=5, y=40)
        
        
        self.student_id_lbl=tk.Label(self.header_forget_frame,text="Enter Student Id Number",font=("Bold",13),bg="white",fg=self.bg_color)
        
        self.student_id_lbl.place(x=80,y=40)
        
        
        self.student_id_entry=tk.Entry(self.header_forget_frame,font=("Bold",15),justify="center",bg="white")
        
        self.student_id_entry.place(x=80,y=70,width=180)
        
        self.info_lbl=tk.Label(self.header_forget_frame,bg="white",text="Via Your Email Address\nWe Will Send To You\nYour Forgitten Password",justify="left")
        
        self.info_lbl.place(x=80,y=110)
        
        
        self.next_butt=tk.Button(text="Send",command=self.check_id,bg=self.bg_color,fg="white",activebackground=self.bg_color,activeforeground="white",font=("Bold",13))
        
        self.next_butt.place(x=210,y=200,width=80)
        
        
        
        
        
        
        
        
        
        
        
        
        
# app=Forget_Pass_page()
# app.mainloop()