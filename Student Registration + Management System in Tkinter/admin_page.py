import tkinter as tk
from tkinter import *
import PIL
from PIL import Image, ImageTk
from database import databsae
from tkinter import messagebox

class Student_admin_page(tk.Tk):

    def home_pack(self):
        self.destroy()
        from Home import Student_Registration
        app = Student_Registration()
        app.mainloop()

    def show_pass(self):
        if not self.lock:
            self.lock = True
            self.lock_button.configure(image=self.lock_img)
            self.pass_entry.configure(show="*")
        else:
            self.lock = False
            self.lock_button.configure(image=self.open_lock_img)
            self.pass_entry.configure(show="")
    
    def remove_highlight_warning(self,entry):
        if entry["highlightbackground"]!="grey":
            if entry.get()!="":
                entry.config(highlightcolor=self.bg_color,highlightbackground="green")
    
    
    
    
    def admin_action(self):
        self.db=databsae("students_accounts.db")
        get_id=self.db.check_admin(self.name_entry.get(),self.pass_entry.get())
        if not get_id:
            messagebox.showerror("wrong","Invalid Admin <Name> or <Password>..")
            self.name_entry.configure(highlightcolor="red",highlightbackground="red")
            self.pass_entry.configure(highlightcolor="red",highlightbackground="red") 
        else:
            messagebox.showinfo("Welcome",f"Hello '{self.name_entry.get()}' ")
            with open("admin.txt","w") as f:
                 admin_id=f.write(self.name_entry.get())
                 f.close()
            self.destroy()
            self.update()
            from admin_login import admin_dashboard
            app=admin_dashboard()
            app.mainloop()
    
    def forgettin_pass(self):
        self.destroy()
        self.update()
        from forget_pass import Forget_Pass_page
        app=Forget_Pass_page()
        app.mainloop()
        
    
        

    def __init__(self):
        super().__init__()

        self.lock = False

        self.iconbitmap("images//aou.ico")

        self.geometry("500x600+550+100")

        self.title("Admin Page")
        
        self.overrideredirect(1)

        self.resizable(0, 0)

        self.attributes("-topmost", True)

    
        self.bg_color = "#273b7a"

        # Images #

        self.login_img = Image.open("images//account.png").resize((100, 100))

        self.login_img = ImageTk.PhotoImage(self.login_img)

        self.lock_img = Image.open("images//lock.png").resize((30, 30))

        self.lock_img = ImageTk.PhotoImage(self.lock_img)

        self.open_lock_img = Image.open("images//unlock.png").resize((30, 30))

        self.open_lock_img = ImageTk.PhotoImage(self.open_lock_img)

        self.arrow_pack_img = Image.open(
            "images//previous.png").resize((30, 30))

        self.arrow_pack_img = ImageTk.PhotoImage(self.arrow_pack_img)

        # Images #

        # window frame #

        self.header_login_frame = tk.Frame(
            bg="#FAF9F6", highlightthickness=3, highlightbackground=self.bg_color)

        self.header_login_frame.pack(pady=30)

        self.header_login_frame.configure(width=400, height=420)

        self.header_text = tk.Label(
            self.header_login_frame, text="Admin Page", bg=self.bg_color, fg="white", font=("Bold", 18))

        self.header_text.place(x=0, y=0, width=400)

        self.header_image = tk.Label(
            self.header_login_frame, image=self.login_img, bg="white")

        self.header_image.place(x=150, y=50)

        self.name_entry_label = tk.Label(text="Enter Admin User Name", font=(
            "Impact", 15), fg=self.bg_color, bg="#FAF9F6")

        self.name_entry_label.place(x=150, y=190)

        self.name_entry = tk.Entry(self.header_login_frame, font=(
            "Bold", 15), justify=tk.CENTER, relief="solid", highlightbackground=self.bg_color, highlightthickness=3)
        
        self.name_entry.bind(
            "<KeyRelease>", lambda e: self.remove_highlight_warning(self.name_entry))

        self.name_entry.place(x=80, y=190)
        
        
        

        self.pass_entry_label = tk.Label(text="Enter Admin Password", font=(
            "Impact", 15), fg=self.bg_color, bg="#FAF9F6")
        

        self.pass_entry_label.place(x=160, y=270)

        self.pass_entry = tk.Entry(self.header_login_frame, font=(
            "Bold", 15), justify=tk.CENTER, relief="solid", highlightbackground=self.bg_color, highlightthickness=3)
        
        
        self.pass_entry.bind(
            "<KeyRelease>", lambda e: self.remove_highlight_warning(self.pass_entry))
        
        

        self.pass_entry.place(x=80, y=270)

        self.lock_button = tk.Button(self.header_login_frame,
                                     bg="#FAF9F6", relief="flat",  command=self.show_pass, bd=0, activebackground="#FAF9F6")

        self.lock_button.place(x=330, y=270)

        self.lock_button.configure(image=self.open_lock_img)

        self.login_button = tk.Button(text="Login", command=self.admin_action,font=("arial", 18), width=10, relief="flat",
                                      bg=self.bg_color, fg="white", activebackground=self.bg_color, activeforeground="white")

        self.login_button.place(x=175, y=350)

        self.forget_pass = tk.Button(text="Forget Password ⚠️", font=(
            "arial", 10), bg="#FAF9F6", fg="red", relief="flat", bd=0,command=self.forgettin_pass, activebackground="#FAF9F6", activeforeground="red")
        self.forget_pass.place(x=190, y=405)

        self.pack_home = tk.Button(
            self.header_login_frame, command=self.home_pack, image=self.arrow_pack_img, bg="#FAF9F6", bd=0, activebackground="#FAF9F6")

        self.pack_home.place(x=5, y=40)


# app=Student_admin_page()
# app.mainloop()
