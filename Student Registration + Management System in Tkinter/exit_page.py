import tkinter as tk
from tkinter import *
import PIL
from PIL import Image, ImageTk
from tkinter import messagebox
import sys



class Security_page(tk.Tk):
    
    def check_password(self):
        
        if self.student_id_entry.get()=="":
            messagebox.showinfo("Invalid Input","Empty Faild !!! ")
            
        elif len(self.student_id_entry.get())<8:
            messagebox.showerror("Id Manager","Invalid Password Should Be At Least 8 Char..")
            
        else:
            if self.student_id_entry.get()=="aou_2030" or self.student_id_entry.get()=="AOU_2030":
                messagebox.showinfo("Thanks","Thanks For Using Our System..")
                self.destroy()
                sys.exit(0)
            else:
                messagebox.showerror("Exit Manager","Wrong Password..")
        
        

           
    
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
            self.header_forget_frame, text="Security Page", bg=self.bg_color, fg="white", font=("Bold", 18))

        self.header_text.place(x=0, y=0, width=350)
        
        
        
        self.pack_home = tk.Button(
            self.header_forget_frame,command=self.back_home, image=self.arrow_pack_img, bg="#FAF9F6", bd=0, activebackground="#FAF9F6")

        self.pack_home.place(x=5, y=40)
        
        
        self.student_id_lbl=tk.Label(self.header_forget_frame,text="Exit Password",font=("Bold",13),bg="white",fg=self.bg_color)
        
        self.student_id_lbl.place(x=110,y=40)
        
        
        self.student_id_entry=tk.Entry(self.header_forget_frame,font=("Bold",15),justify="center",bg="white")
        
        self.student_id_entry.place(x=80,y=70,width=180)
        
    
        
        
        self.next_butt=tk.Button(text="Exit",command=self.check_password,bg=self.bg_color,fg="white",activebackground=self.bg_color,activeforeground="white",font=("Bold",13))
        
        self.next_butt.place(x=210,y=200,width=80)

app=Security_page()
app.mainloop()