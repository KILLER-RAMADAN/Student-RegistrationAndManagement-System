import sqlite3
from tkinter import messagebox

class databsae():

    def __init__(self, db):

        self.sq_con = sqlite3.connect(db)
        self.cur = self.sq_con.cursor()

        self.main_quary="""
        
        CREATE TABLE IF NOT EXISTS Full_Students_Data  (
            
            Id text Primary key,
            name text,
            gender text,
            age text,
            phone_number text,
            major text,
            email text,
            image BloP,
            password text
            
        )
        """
        self.cur.execute(self.main_quary)

        self.sq_con.commit()

    def insert_date(self, Id, password ,name, age, gender,phone_number,s_class,email, Image):

        self.cur.execute("INSERT INTO Full_Students_Data values (?,?,?,?,?,?,?,?,?)",
                         (Id, password, name, age, gender, phone_number, s_class, email, Image))

        self.sq_con.commit()
        
        
    def check_id(self,id_number): 
        get_id=self.cur.execute(
            f"""SELECT Id FROM Full_Students_Data WHERE Id == '{id_number}' """)
        self.sq_con.commit()
        Full_id=get_id.fetchall()
        self.cur.close()
        return Full_id
        
    def check_id_pass(self,id_number,password): 
        get_id_and_pass=self.cur.execute(
            f"""SELECT Id FROM Full_Students_Data WHERE Id == '{id_number}' AND password =='{password}' """)
    
        
        self.sq_con.commit()
        get_id=get_id_and_pass.fetchall()
        self.cur.close()
        
        return get_id
        
        
      
    def get_pass(self,id_number): 
        get_pass=self.cur.execute(
            f"""SELECT password FROM Full_Students_Data WHERE Id == '{id_number}' """)
    
        
        self.sq_con.commit()
        a_pass=get_pass.fetchall()[0][0]
        self.cur.close()
        
        return a_pass    
    
    def get_email(self,id_number): 
        a_mail=self.cur.execute(
            f"""SELECT email FROM Full_Students_Data WHERE Id == '{id_number}' """)
    
        
        self.sq_con.commit()
        a_mail=a_mail.fetchall()[0][0]
        self.cur.close()
        
        return a_mail  
            
    
            
    def check_admin(self,name,password): 
        get_id_and_pass=self.cur.execute(
            f"""SELECT name FROM Full_Students_Data WHERE name == '{name}' AND password =='{password}' """)
    
        
        self.sq_con.commit()
        get_id=get_id_and_pass.fetchall()
        self.cur.close()
        
        return get_id
        
    def fetch_all_studetnt(self,id):
        self.quary2 = f"""SELECT * FROM Full_Students_Data WHERE Id == '{id}' """
        self.rows = self.cur.execute(self.quary2).fetchall()

        return self.rows
        

    def fetch_all_admin(self,admin):
        self.quary2 = f"""SELECT * FROM Full_Students_Data WHERE name == '{admin}' """
        self.rows = self.cur.execute(self.quary2).fetchall()

        return self.rows
    
    def fetch_Students_count(self,major):
        self.quary2 = f"""SELECT major FROM Full_Students_Data WHERE major == '{major}' """
        self.rows = self.cur.execute(self.quary2).fetchall()

        return len(self.rows)
    
    def fetch_specific_student_mail(self,major):
        self.quary2 = f"""SELECT email FROM Full_Students_Data WHERE major == '{major}' """
        self.rows = self.cur.execute(self.quary2).fetchall()

        return self.rows
    
    
    
    def fetch_all_mail_to_all_students(self):
        self.quary2 = f"""SELECT email FROM Full_Students_Data WHERE major != '{"Admin"}' """
        self.rows = self.cur.execute(self.quary2).fetchall()
        
        return self.rows
    
    


    def ubdate_password(self,password,id):

        self.cur.execute("Update Full_Students_Data set password=? WHERE Id=? ",
                         (password,id))

        self.sq_con.commit()
        
        self.cur.close()
        
    
    def ubdate_data_without_photo(self,Name, Age,major ,Email, Phone,Id):
        
         self.cur.execute("Update Full_Students_Data set name=?,age=?,major=?,email=?,phone_number=? WHERE Id=? ",
                         (Name, Age ,major ,Email ,Phone, Id))
        
        
         self.sq_con.commit()
         self.cur.close()
         
         
        
    def ubdate_data_with_photo(self,image ,Name, Age,major ,Email, Phone,Id):
        
        if image!="":
         self.cur.execute("Update Full_Students_Data set image=?,name=?,age=?,major=?,email=?,phone_number=? WHERE Id=? ",
                         (image,Name, Age ,major ,Email ,Phone, Id))
        
        
         self.sq_con.commit()
         self.cur.close()
        else:
            self.ubdate_data_without_photo(Name, Age ,major ,Email ,Phone, Id)
        


    def remove(self, Id):
        self.cur.execute(" DELETE FROM Full_Students_Data WHERE Id=?", (Id,))
        self.sq_con.commit()
        self.cur.close()
        
    def remove_admin(self, name):
        self.cur.execute(" DELETE FROM Full_Students_Data WHERE name=?", (name,))
        self.sq_con.commit()
        self.cur.close()
        
        
    def serche_data(self, Ct, Et):
        self.cur.execute("SELECT * FROM Full_Students_Data WHERE " +
                         Ct+" like '%'||?||'%'", (Et,))
        self.rows = self.cur.fetchall()
        return self.rows



    











