import tkinter as tk
import sqlite3

#############################################################

connection=sqlite3.connect(r"C:\Users\user33\Desktop\tk\database\DB.db",isolation_level=None)
data_base = connection.cursor()




##############################################################









TITLE_FONT = ("Helvetica", 18, "bold")

class oscarApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.m = self
        self.m.title("Main Page")
        self.m.geometry('300x500')
        self.m.config(bg = "black")
        self.m.resizable(False, False)
        

        self.frames = {}
        for F in (StartPage,Signin):
            page_name = F.__name__
            frame = F(self.m, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.m.button1=tk.Button(text="x",height =1,width = 2,command=lambda :self.show_frame("StartPage"),bg="gray",fg="black",font=("Helvetica", 22)).place(x=130 ,y=475)
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()




class StartPage(tk.Frame):


    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame1=tk.Frame(self,bg = "white",width=300,height=475)
        self.label1 = tk.Label(self.frame1, text = "USER NAME :",font=("Helvetica", 13),bg="white",fg="sea green").place(x=1, y=60)
        self.text1 = tk.Entry(self.frame1,width = 20,bg="white",	bd=0.9,font=("Helvetica", 9),fg="black").place(x=120,y=60)#bd=boderwidth
        self.label2 = tk.Label(self.frame1, text = "PASSWORD :",font=("Helvetica", 13),bg="white",fg="sea green").place(x=1, y=100)
        self.text2 = tk.Entry(self.frame1,width = 20,bg="white",show='*',bd=0.9,font=("Helvetica", 9),fg="black").place(x=120,y=100)#bd=boderwidth
        self.button1=tk.Button(self.frame1,height =1,width = 10,text="Login",bg="sea green",fg="black",bd=0.9,font=("Helvetica", 9),command=self.frame1).place(x=110 ,y=150)
        self.button2=tk.Button(self.frame1,text="Forget password?",bg="white",fg="sea green",bd=0,font=("Helvetica", 9),command=self.frame1).place(x=10 ,y=200)
        self.label2 = tk.Label(self.frame1, text = "X",font=("Helvetica", 20),bg="white",fg="sea green").place(x=137, y=270)
        self.label3 = tk.Label(self.frame1, text = " Finger Print",font=("Helvetica", 10),bg="white",fg="sea green").place(x=112, y=310)
        self.label4 = tk.Label(self.frame1, text = "",font=("Helvetica", 10),bg="white",fg="sea green").place(x=100, y=310)
        self.label5 = tk.Label(self.frame1, text = "Don't have an account?:",font=("Helvetica", 11),bg="white",fg="sea green").place(x=55, y=430)
        self.button3=tk.Button(self.frame1,text="Sign In",bg="sea green",fg="black",command=lambda: controller.show_frame("Signin"),bd=0.9,font=("Helvetica", 9)).place(x=220 ,y=430)
        
        
        self.frame1.pack()

class Signin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame2=tk.Frame(self,bg = "white",width=300,height=475)
        
        self.label1 = tk.Label(self.frame2,width=25,height=1, text = "SIGNIN",font=("Helvetica", 16),bd=0.9,bg="sea green",fg="white").place(x=0, y=0)
        
        self.data_1=tk.StringVar()
        self.label2 = tk.Label(self.frame2, text = "USER NAME :",font=("Helvetica", 11),bg="white",fg="sea green").place(x=1, y=60)
        self.text1 = tk.Entry(self.frame2,textvariable =self.data_1 ,width = 20,bg="white",bd=0.9,font=("Helvetica", 9),fg="black").place(x=140,y=60)#bd=boderwidth
        
        
        self.data_2=tk.StringVar()
        self.label3 = tk.Label(self.frame2, text = "PASSWORD :",font=("Helvetica", 11),bg="white",fg="sea green").place(x=1, y=100)
        self.text2 = tk.Entry(self.frame2,textvariable =self.data_2,width = 20,bg="white",show='*',bd=0.9,font=("Helvetica", 9),fg="black").place(x=140,y=100)#bd=boderwidth

        
        
        self.data_3=tk.StringVar()
        self.label4 = tk.Label(self.frame2, text = "RE-PASSWORD :",font=("Helvetica", 11),bg="white",fg="sea green").place(x=1, y=140)
        self.text3 = tk.Entry(self.frame2,textvariable =self.data_3,width = 20,bg="white",show='*',bd=0.9,font=("Helvetica", 9),fg="black").place(x=140,y=140)#bd=boderwidth
        
        
        
        self.data_4=tk.StringVar()
        self.label5 = tk.Label(self.frame2, text = "MOBILE-NUMBER :",font=("Helvetica", 11),bg="white",fg="sea green").place(x=1, y=180)
        self.text4 = tk.Entry(self.frame2,textvariable =self.data_4,width = 20,bg="white",bd=0.9,font=("Helvetica", 9),fg="black").place(x=140,y=180)#bd=boderwidth
        
        
        self.data_5=tk.StringVar()
        self.label6 = tk.Label(self.frame2, text = "EMAIL-ID :",font=("Helvetica", 11),bg="white",fg="sea green").place(x=1, y=220)
        self.text5 = tk.Entry(self.frame2,textvariable =self.data_5,width = 20,bg="white",bd=0.9,font=("Helvetica", 9),fg="black").place(x=140,y=220)#bd=boderwidth
        
        
        self.label7 = tk.Label(self.frame2, text = " Finger Print",font=("Helvetica", 11),bg="white",fg="sea green").place(x=110, y=280)
        self.label2 = tk.Label(self.frame2, text = "X",font=("Helvetica", 20),bg="white",fg="sea green").place(x=137, y=305)
        self.button1=tk.Button(self.frame2,text="Submit",bg="sea green",command=lambda :(Signin.submit_check(self,  controller,Signin)),fg="black",bd=0.9,font=("Helvetica", 10)).place(x=125 ,y=400)
        self.frame2.pack()
        
    def submit_check(self,controller,Signin):
        self.controller = controller
        self.username= self.data_1.get()
        self.password= self.data_2.get()
        self.re_password= self.data_3.get()
        self.mobile_no= self.data_4.get()
        self.email_id= self.data_5.get()
        user_name_db=data_base.execute("SELECT user_name FROM DB_1").fetchall()
        user_name_db = [r[0] for r in user_name_db]
        mobile_number_db=data_base.execute("SELECT mobile FROM DB_1").fetchall()
        mobile_number_db = [r[0] for r in mobile_number_db]
        email_id_db=data_base.execute("SELECT email_id FROM DB_1").fetchall()
        email_id_db = [r[0] for r in email_id_db]
        if len(self.password)==0:
            pass
        else:
            upper=0
            lower=0
            number=0
            for i in self.password:
                if i.isupper():
                    upper += 1
                elif i.islower():
                    lower += 1
                elif i.isdigit():
                    number += 1
        
        if len(self.username)==0 or len(self.password)==0 or len(self.re_password)==0 or len(self.mobile_no)==0 or len(self.email_id)==0 :
            string="fill all the feild"
            anchor ="nw"
            Error.error(self,string,anchor)
        elif upper==0 or lower==0 or number==0 or len(self.password)<8:
                string="password should contain\n at least one alphabet\n one number and should be\n 8 characters long"
                anchor ="nw"
                Error.error(self,string,anchor)
        elif self.password != self.re_password:
             string="Check password"
             anchor ="nw"
             Error.error(self,string,anchor)
        elif self.mobile_no in mobile_number_db:
             string="mobile number already exist"
             anchor ="nw"
             Error.error(self,string,anchor)
        elif self.username in user_name_db:
             string="User Name already exist"
             anchor ="nw"
             Error.error(self,string,anchor)
        elif self.email_id in email_id_db:
             string="Email ID already exist"
             anchor ="nw"
             Error.error(self,string,anchor)
        else:
             data_base.execute("INSERT INTO DB_1( user_name, password, mobile, email_id) VALUES (?, ?, ?,?)",(self.username,self.password,self.mobile_no,self.email_id))
             connection.commit()
             string="success"
             anchor ="nw"
             Error.error(self,string,anchor)
             controller.show_frame("StartPage")
        
class Error(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
    def error(self,value,x):
        window=tk.Tk()
        window.resizable(False, False)
        window.title("error")
        self.frame2=tk.Frame(window,bg = "white",width=200,height=100)
        self.label2 = tk.Label(self.frame2, text = value,font=("Helvetica", 11),bg="white",fg="sea green").place( anchor = x)
        self.frame2.pack()


        
        

        
        
        

if __name__ == "__main__":

    app = oscarApp()
    app.mainloop()


connection.commit()
connection.close()
