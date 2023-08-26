import tkinter as tk
from tkinter import *
from PIL import Image ,ImageTk, ImageTk, ImageDraw, ImageFont
from database import databsae
import io
import os
from tkinter import messagebox
import tkinter.ttk
import tkinter.ttk as ttk
import tkinter.scrolledtext as tkscrolled
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import my_email 
import smtplib
import threading

class admin_dashboard(tk.Tk):
 

 def get_data_from_Table(self,event):
    self.focus=self.trev.focus()
    self.contents=self.trev.item(self.focus)
    self.row=self.contents['values']
    self.gsc_btn.config(state="normal")
    self.show_student_card()
    
    
 def show_student_card(self):
        self.db=databsae("students_accounts.db")
         
        
         
        data=self.db.fetch_all_studetnt(f"{self.row[0]}")
        img=data[0][7]
        img=io.BytesIO(img)
        self.home_directory=os.path.expanduser( '~' )
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
{data[0][0]}
{data[0][1]}
{data[0][3]}
{data[0][2]}
{data[0][4]}
{data[0][5]}
{data[0][6]}
"""
        if data[0][5] !="Admin":
         s_card = Image.open("images//student_card_frame.png")
         pic = Image.open(img).resize((100,100))

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
        else:
         s_card = Image.open("images//student_card_frame.png")
         pic = Image.open(img).resize((100,100))

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


 def print_card(self):
        self.destroy()
        self.update()
        from student_card_page2 import Student_card
        app=Student_card()
        app.mainloop()
        

 def log_out(self):
         y=messagebox.askokcancel("Logout Manager","Do You Want To Exit !?")
         if y:
          self.destroy()
          self.update()
          from Home import Student_Registration
          app=Student_Registration()
          app.mainloop()
         else:
           pass
 
 def get_search_data(self):
     
     if self.choose_otion_to_find.get()=="" or self.choose_entry.get()=="":
         messagebox.showerror("Serch Manager","Invalid Input...")
     else:
     
      self.db=databsae("students_accounts.db")
      
      self.trev.delete(*self.trev.get_children())
      
      self.full_data=self.db.serche_data(self.choose_otion_to_find.get(),self.choose_entry.get())
      
      if self.full_data:
       for row in self.full_data:
        self.trev.insert("","end",values=row)
      else:
         messagebox.showerror("Search Manager","Student Not Found...")
         
        
 
 def clean_up(self):
     self.choose_entry.delete(0,1000)
     self.gsc_btn.config(state="disable")
     self.trev.delete(*self.trev.get_children())\
         
 def send_Mail(self,subject,message,To):
     
     if self.subject_entry.get()=="":
         messagebox.showerror("Announcement Manager","Enter Subject...")
     elif self.message_entry.get("0.1","end")=="":
             messagebox.showerror("Announcement Manager","Enter Message...") 
     else:
      if To=="All Students":
              self.db=databsae("students_accounts.db")
        
              all_emails=self.db.fetch_all_mail_to_all_students()
              
              all_emails_list=[]
              for email in all_emails:
                all_emails_list.append(email[0][0:])
              
              print(all_emails_list)
              self.count=0
              for i in all_emails_list:
               self.count+=1
               smtp_server="smtp.gmail.com"
               smtp_port=587
               username=my_email.defualt_email
               passw=my_email.email_password
        
               msg=MIMEMultipart()
        
               msg['Subject']=subject
               msg['From']=username
               msg['To']=i
        
               msg.attach(MIMEText(_text=message,_subtype="html"))
        
               smtp_connection=smtplib.SMTP(host=smtp_server,port=smtp_port)
        
               smtp_connection.starttls()
        
               smtp_connection.login(user=username,password=passw)
         
               smtp_connection.sendmail(from_addr=username,to_addrs=i,msg=msg.as_string())
        
               self.send_state_lbl.configure(text=f"Total Sending Messages: {self.count}")
        
              messagebox.showinfo("Done",f"Successfully Sending All Messages")
              
      else:
       self.db=databsae("students_accounts.db")
     
       emails=self.db.fetch_specific_student_mail(To)
     
       emails_list=[]
     
       for email in emails:
        emails_list.append(email[0][0:])
       print(emails_list)
       self.count=0
       for i in emails_list:
        self.count+=1
        smtp_server="smtp.gmail.com"
        smtp_port=587
        
        username=my_email.defualt_email
        passw=my_email.email_password
        
        msg=MIMEMultipart()
        
        msg['Subject']=subject
        msg['From']=username
        msg['To']=i
        
        msg.attach(MIMEText(_text=message,_subtype="html"))
        
        smtp_connection=smtplib.SMTP(host=smtp_server,port=smtp_port)
        
        smtp_connection.starttls()
        
        smtp_connection.login(user=username,password=passw)
        
        smtp_connection.sendmail(from_addr=username,to_addrs=i,msg=msg.as_string())
        
        self.send_state_lbl.configure(text=f"Total Sending Messages: {self.count}")
        
       messagebox.showinfo("Done",f"Successfully Sending All Messages")
        
        
    
 def thread(self):
     threading.Thread(target=self.send_Mail(subject=self.subject_entry.get(),message=f'<h2>{self.message_entry.get("0.1","end")}</h2>',To=self.choose_otion_to_send_mail.get())).start()
        
 def delete_fun(self):
         
         ask=messagebox.askokcancel("Delete Manager","Are You Sure To Delete This Account !?")
         if ask:
          self.db=databsae("students_accounts.db")
         
          with open("admin.txt","r") as f:
                 admin_id=f.read()
                 f.close()
          self.db.remove_admin(admin_id)
          messagebox.showinfo("Delete Manager","Successfully Process....")
          self.destroy()
          self.update()
          from Home import Student_Registration
          app=Student_Registration()
          app.mainloop()
         
         
 def tes(self): 
        #  x=self.db.fetch_all_mail_to_all_students()
        #  print(x)
         pass
         
        
 def home_bage(self):
         
         
         self.db=databsae("students_accounts.db")
         
         with open("admin.txt","r") as f:
                 text_admin=f.read()
                 f.close()
         
         data=self.db.fetch_all_admin(f"{text_admin}")
         
         img=data[0][7]
         img=io.BytesIO(img)
         
         self.admin_image = Image.open(img).resize((100,100))
         
         self.admin_image=ImageTk.PhotoImage(self.admin_image)
         
         
         self.db=databsae("students_accounts.db")
         
         with open("admin.txt","r") as f:
                 text_admin=f.read()
                 f.close()
         
         data_ds=self.db.fetch_Students_count(f"DS")
         
         data_Ai=self.db.fetch_Students_count(f"AI")
         
         data_cyber=self.db.fetch_Students_count(f"Cyber-Security")
         
         data_WD=self.db.fetch_Students_count(f"WD")
         
         data_WT=self.db.fetch_Students_count(f"WT")
         
         data_CS=self.db.fetch_Students_count(f"CS")
         
         data_media=self.db.fetch_Students_count(f"Media")
         
         data_Admin=self.db.fetch_Students_count(f"Admin")
         
         
         
         home_bg_fm=tk.Frame(self.pages_frame,bg="white")
           
         home_bg_lbl=tk.Label(home_bg_fm,text="Number Of Students By Major",font=("Bold",13),bg=self.bg_color,fg="white")
         
         home_bg_lbl.place(x=120,y=100)
         
         self.photo_fm=tk.Frame(home_bg_fm,bg="grey")
         
         self.photo_fm.place(x=5,y=5,width=100,height=100)
         
         self.photo_lbl=tk.Label(self.photo_fm,image=self.admin_image,bg="white")
         
         self.photo_lbl.place(x=0,y=0,width=100,height=100)
         
         
         self.hi_lbl=tk.Label(home_bg_fm,text=f"Ahlan {data[0][1]}",font=("arial",15),bg="white")
         
         self.hi_lbl.place(x=130,y=40)
         
         self.Ds_lbl=tk.Label(home_bg_fm,text=f"Ds Major: {data_ds}",font=("Bold",15),bg="white")
         
         self.Ds_lbl.place(x=5,y=130)
         
         self.Ai_lbl=tk.Label(home_bg_fm,text=f"Ai Major: {data_Ai}",font=("Bold",15),bg="white")
         
         self.Ai_lbl.place(x=5,y=190)
         
         self.Cyber_Security_lbl=tk.Label(home_bg_fm,text=f"Cyber-Security Major: {data_cyber}",font=("Bold",15),bg="white")
         
         self.Cyber_Security_lbl.place(x=5,y=250)
         
         self.WD_lbl=tk.Label(home_bg_fm,text=f"WD Major: {data_WD}",font=("Bold",15),bg="white")
         
         self.WD_lbl.place(x=5,y=310)
         
         self.WT_lbl=tk.Label(home_bg_fm,text=f"WT Major: {data_WT}",font=("Bold",15),bg="white")
         
         self.WT_lbl.place(x=5,y=370)
         
         self.Cs_lbl=tk.Label(home_bg_fm,text=f"Cs Major: {data_CS}",font=("Bold",15),bg="white")
         
         self.Cs_lbl.place(x=5,y=430)
         
         self.Media_lbl=tk.Label(home_bg_fm,text=f"Media Major: {data_media}",font=("Bold",15),bg="white")
         
         self.Media_lbl.place(x=5,y=490)
         
         
         self.Media_lbl=tk.Label(home_bg_fm,text=f"Admins: {data_Admin}",font=("Bold",15),bg="white")
         
         self.Media_lbl.place(x=200,y=130)
         
         
         
         
         
         
         home_bg_fm.pack(fill="both",expand=True)
                 
 def Find_student_bage(self):
     
        
     
        Find_student_bg_fm=tk.Frame(self.pages_frame,bg="white")
        
        find_bg_lbl=tk.Label(Find_student_bg_fm,text="Find Student Record",font=("Bold",15),bg=self.bg_color,fg="white")
         
        find_bg_lbl.place(x=20,y=20,width=300)
        
        
        find_by_lbl=tk.Label(Find_student_bg_fm,text="Find By:",font=("Bold",15),bg="white")
         
        find_by_lbl.place(x=20,y=70)
        
        
        self.choose_otion_to_find=tkinter.ttk.Combobox(Find_student_bg_fm,state="readonly",values=["Id","name","gender","major"],font=("Bold",15))
        
        self.choose_otion_to_find.place(x=100,y=70,width=100)
        
        
        
        self.choose_otion_to_find.set("Id")
        
        
        self.choose_entry=tk.Entry(Find_student_bg_fm,font=("Bold",15),bg="white",justify="center",relief="solid")
        
        self.choose_entry.place(x=20,y=110)
        
        
        find_bg_lbl=tk.Label(Find_student_bg_fm,text="Record Table",font=("Bold",15),bg=self.bg_color,fg="white")
         
        find_bg_lbl.place(x=20,y=170,width=300)
        
        
        # self.table_frame=tk.Frame(Find_student_bg_fm,bg="white",width=300,height=400)
        # self.table_frame.place(x=0,y=300)
        
        
       
        
        style=ttk.Style()
        style.configure("mystile.Treeview",font=("calibri",15),rowhieght=100)
        style.configure("mystile.Treeview.Heading",font=("calibri",10),rowhieght=100)
        self.trev=ttk.Treeview(Find_student_bg_fm,columns=(1,2,3),style="mystile.Treeview")
        self.trev.bind("<ButtonRelease-1>") # self.get_data_from_Table
        self.trev.heading("1",text="ID")
        self.trev.column("1",width=80)
        self.trev.heading("2",text="Name")
        self.trev.column("2",width=150)
        self.trev.heading("3",text="Gender")
        self.trev.column("3",width=50)
        self.trev['show']='headings'
        self.trev.bind("<ButtonRelease-1>",self.get_data_from_Table)
        self.trev.place(x=0,y=220,height=250,width=345)
        
        
        self.Search_btn=tk.Button(Find_student_bg_fm,text="Search",justify="center",cursor="hand2",command=self.get_search_data,font=("Bold",15),bg=self.bg_color,fg="white",activebackground=self.bg_color,activeforeground="white")
        
        self.Search_btn.place(x=0,y=480)
        
        self.clear_btn=tk.Button(Find_student_bg_fm,text="Clean UP",cursor="hand2",command=self.clean_up,font=("Bold",15),bg=self.bg_color,fg="white",activebackground=self.bg_color,activeforeground="white")
        
        self.clear_btn.place(x=0,y=525)
        
        
        self.gsc_btn=tk.Button(Find_student_bg_fm,text="Generate Student Card",cursor="hand2",command=self.print_card,font=("Bold",15),bg=self.bg_color,fg="white",activebackground=self.bg_color,activeforeground="white")
        
        self.gsc_btn.place(x=120,y=480)
        
        self.gsc_btn.config(state="disabled")
        
         
        Find_student_bg_fm.pack(fill="both",expand=True)
        
        
         
 def annonuce_bage(self):
         
         
         
         annonuce_bg_fm=tk.Frame(self.pages_frame,bg="white")
         
         
         info_lbl=tk.Label(annonuce_bg_fm,text="Enter Announcement Subject",bg=self.bg_color,fg="white",font=("Bold",15))
         
         info_lbl.place(x=0,y=0)
         
         self.subject_entry=tk.Entry(annonuce_bg_fm,font=("Bold",15),bg="white",justify="center",relief="solid")
         
         self.subject_entry.place(x=0,y=40)
         
         
         message_lbl=tk.Label(annonuce_bg_fm,text="Enter Announcement Message",bg=self.bg_color,fg="white",font=("Bold",15))
         
         message_lbl.place(x=0,y=110)
         
         self.message_entry=tkscrolled.ScrolledText(annonuce_bg_fm,font=("Bold",12),bg="white")
         
         
         self.message_entry.place(x=0,y=150,height=200,width=345)
         
         send_lbl=tk.Label(annonuce_bg_fm,text="Choose Major To Send",bg=self.bg_color,fg="white",font=("Bold",15))
         
         send_lbl.place(x=0,y=380)
         
         
         self.choose_otion_to_send_mail=tkinter.ttk.Combobox(annonuce_bg_fm,state="readonly",values=["DS","WT","WD","Cyber-Security","AI","CS","Media","Admin","All Students"],font=("Bold",15))
        
         self.choose_otion_to_send_mail.place(x=0,y=430,width=150)
         
         self.choose_otion_to_send_mail.set("DS")
         
    
         self.send_btn=tk.Button(annonuce_bg_fm,text="Send Announcement",command=self.thread,font=("Bold",12),bg=self.bg_color,fg="white",activebackground=self.bg_color,activeforeground="white")
         
         self.send_btn.place(x=180,y=430)
         
         
         self.send_state_lbl=tk.Label(annonuce_bg_fm,fg="black",bg="white",font=("Bold",15))
         
         self.send_state_lbl.place(x=0,y=480)
         
         
         annonuce_bg_fm.pack(fill="both",expand=True)
        
        
 def delete_page(self):
          del_bg_fm=tk.Frame(self.pages_frame,bg="white")
          
          delete_bg_lbl=tk.Label(del_bg_fm,text="⚠️Delete Account",fg="white",bg="red",font=("Bold",15))
         
          delete_bg_lbl.place(x=25,y=100,width=300)
         
          del_btn=tk.Button(del_bg_fm,text="Delete Account",bg="red",fg="white",command=self.delete_fun,cursor="hand2",activebackground="red",activeforeground="white",font=("Bold",15))
         
          del_btn.place(x=75,y=200,width=200)
         
          
          
          del_bg_fm.pack(fill="both",expand=True)
         
 
         
 
 
        
 
        
 def switch(self,indicator,page):
        self.home_button_indec.configure(bg="#c3c3c3")
        self.Find_student_indec.configure(bg="#c3c3c3")
        self.Announce_btn_indec.configure(bg="#c3c3c3")
        self.del_btn_indec.configure(bg="#c3c3c3")
        indicator.config(bg=self.bg_color)
        
        for child in self.pages_frame.winfo_children():
                child.destroy()
                self.update()
                
        page()
        

        
        
 def __init__(self):
        
        
                
        
        
        
        super().__init__()
        
        self.lock=False
        
        self.home_directory=os.path.expanduser( '~' )
        
        self.db=databsae("students_accounts.db")
        

        self.iconbitmap("images//aou.ico")
        
        self.geometry("500x600+550+100")
        
        self.title("Admin Dashboard + Management System")
        
        self.overrideredirect(1)
        
        self.resizable(0,0)
        
        
        self.attributes("-topmost",True)
        
        self.bg_color = "#273b7a"
        
        
        
        
        # Frame #
        
        
        self.dash_frame=tk.Frame(bg="white")
        
        self.dash_frame.pack(pady=5)
        
        self.dash_frame.configure(width=480,height=580)
        
        
        self.options_frame=tk.Frame(self.dash_frame,bg="#c3c3c3",highlightbackground=self.bg_color,highlightthickness=3)
        
        self.options_frame.place(x=0,y=0,width=120,height=574)
        
        
        
        self.home_btn=tk.Button(self.dash_frame,text="Home",cursor="hand2",font=("Bold",15),command=lambda:self.switch(indicator=self.home_button_indec,page=self.home_bage),bg="#c3c3c3",fg=self.bg_color,bd=0,activebackground="#c3c3c3",activeforeground=self.bg_color)
        
        self.home_btn.place(x=10,y=50)
        
        
        self.home_button_indec=tk.Label(self.options_frame,bg=self.bg_color)
        
        self.home_button_indec.place(x=3,y=48,width=3,height=40)
        
        
        self.Find_student_btn=tk.Button(self.dash_frame,text="Find\nStudent",cursor="hand2",command=lambda:self.switch(indicator=self.Find_student_indec,page=self.Find_student_bage),justify="left",font=("Bold",15),bg="#c3c3c3",fg=self.bg_color,bd=0,activebackground="#c3c3c3",activeforeground=self.bg_color)
        
        self.Find_student_btn.place(x=10,y=100)
        
        
        self.Find_student_indec=tk.Label(self.options_frame,bg="#c3c3c3")
        
        self.Find_student_indec.place(x=3,y=108,width=3,height=40)
        
        
        self.Announce_btn=tk.Button(self.dash_frame,text="Announce\nMent📢",cursor="hand2",command=lambda:self.switch(indicator=self.Announce_btn_indec,page=self.annonuce_bage),justify="left",font=("Bold",15),bg="#c3c3c3",fg=self.bg_color,bd=0,activebackground="#c3c3c3",activeforeground=self.bg_color)
        
        self.Announce_btn.place(x=10,y=170)
        
        
        self.Announce_btn_indec=tk.Label(self.options_frame,bg="#c3c3c3")
        
        self.Announce_btn_indec.place(x=3,y=175,width=3,height=40)
        
    
        
        
        self.del_btn=tk.Button(self.dash_frame,text="Delete\nAccount",cursor="hand2",command=lambda:self.switch(indicator=self.del_btn_indec,page=self.delete_page),justify="left",font=("Bold",15),bg="#c3c3c3",fg=self.bg_color,bd=0,activebackground="#c3c3c3",activeforeground=self.bg_color)
        
        self.del_btn.place(x=10,y=250)
        
        
        self.del_btn_indec=tk.Label(self.options_frame,bg="#c3c3c3")
        
        self.del_btn_indec.place(x=3,y=255,width=3,height=40)
        
        
        
        self.logout_btn=tk.Button(self.dash_frame,text="Logout",cursor="hand2",command=self.log_out,justify="left",font=("Bold",15),bg="#c3c3c3",fg=self.bg_color,bd=0,activebackground="#c3c3c3",activeforeground=self.bg_color)
        
        self.logout_btn.place(x=10,y=330)
        
        
        # Pages Frame #
        
        self.pages_frame=tk.Frame(self.dash_frame,bg="white")
        
        self.pages_frame.place(x=125,y=5,width=345,height=565)
        
        
        
        
        
        
        # Pages Frame #
        
        self.tes()
        
        self.home_bage()


# app=admin_dashboard()
# app.mainloop()