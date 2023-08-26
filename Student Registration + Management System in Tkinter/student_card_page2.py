import tkinter as tk
from tkinter import *
import PIL
from PIL import Image ,ImageTk,ImageDraw,ImageFont
import win32api

import os



class Student_card(tk.Tk):
    
    def back_home(self):
        self.destroy()
        self.update()
        from admin_login import admin_dashboard
        app=admin_dashboard()
        app.mainloop()
    
    
    def print_card(self):
        self.card_img = Image.open(f"{self.home_directory}//card-id.png")
        self.card_img=ImageTk.PhotoImage(self.card_img)
        self.student_card_img.configure(image=self.card_img)   
             
        win32api.ShellExecute(0, 'Print',f'{self.home_directory}//card-id.png',None,'.',0)
    

    def __init__(self):

        super().__init__()
        
        
        self.home_directory = os.path.expanduser( '~' )
      


        self.iconbitmap("images//aou.ico")

        self.geometry("500x600+550+100")

        self.title("Student Card")

        self.overrideredirect(1)

        self.resizable(0, 0)

        # self.attributes("-topmost", True)

        self.bg_color = "#273b7a"
        
        # images #

        
        self.back_img=Image.open("images//previous.png").resize((30,30))
        self.back_img=ImageTk.PhotoImage(self.back_img)
        
        self.print_img = Image.open("images//printer.png").resize((17,17))
        self.print_img = ImageTk.PhotoImage(self.print_img)
        
        self.card_img = Image.open(f'{self.home_directory}//card-id.png')
        self.card_img = ImageTk.PhotoImage(self.card_img)
        
        # images #
        
        # card Fram #
        
        
        self.card_frame=tk.Frame(bg="white",highlightbackground=self.bg_color,highlightthickness=3)
        
        self.card_frame.place(x=50,y=30,width=400,height=450)
        
        
        self.header_lbl=tk.Label(self.card_frame,text="Student Card",font=("Bold",18),fg="white",bg=self.bg_color)
        
        self.header_lbl.place(x=0,y=0,width=400)
        
        
        
        self.pack_button=tk.Button(self.card_frame,command=self.back_home,image=self.back_img,bg="white",bd=0,activebackground="white")
        
        self.pack_button.place(x=5,y=40)
        
        
        
        self.student_card_img=tk.Label(self.card_frame,image=self.card_img,bg="white")
        
        self.student_card_img.place(x=50,y=50)
        
        
        
        
        # self.save_s_card=tk.Button(self.card_frame,text="Save Student Card",activeforeground="white",font=("Bold",15),bg=self.bg_color,fg="white",activebackground=self.bg_color)
        
        # self.save_s_card.place(x=45,y=375)
        
        self.print_s_card = tk.Button(self.card_frame,image=self.print_img,compound="left" ,text="Print Card", activeforeground="white", font=(
            "Bold", 15), bg=self.bg_color, fg="white",command=self.print_card, activebackground=self.bg_color,width=160)

        self.print_s_card.place(x=120, y=375)
        
        
        
        
        
        
       





# app=Student_card()
# app.mainloop()