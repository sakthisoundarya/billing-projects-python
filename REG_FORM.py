from tkinter import*
from tkinter import messagebox
import mysql.connector

def grapes():
    FIRSTNAME=a1. get()
    LASTNAME=b1. get()
    AGE=c1. get()
    CONTACT=d1. get()
    PASSWORD=e1. get()

    if(FIRSTNAME=="" or LASTNAME=="" or AGE=="" or CONTACT=="" or PASSWORD==""):
        messagebox.showinfo("ERROR","Empty Text are not Accetable!!!")
    else:
        comm=mysql.connector.connect(host="localhost",user="root",password="",database="bharath")
        curl=comm.cursor()
        sqll="INSERT INTO `spidy`(`FIRSTNAME`, `LASTNAME`, `AGE`, `CONTACT`, `PASSWORD`) VALUES (%s,%s,%s,%s,%s)"
        vall=(FIRSTNAME,LASTNAME,AGE,CONTACT,PASSWORD)
        curl.execute(sqll,vall)
        comm.commit()
        messagebox.showinfo("SUCCESS"," YOUR ACCOUNT HAS BEEN LOGINED")

        
hi=Tk()
hi.title("REGISTRATION FORM")
hi.geometry("450x350")
hi.resizable(False,False)
hi.config(bg="white")

a=Label(hi,bg="white",text="FIRSTNAME").place(x=10,y=10)
b=Label(hi,bg="white",text="LASTNAME").place(x=10,y=50)
c=Label(hi,bg="white",text="AGE").place(x=10,y=90)
d=Label(hi,bg="white",text="CONTACT").place(x=10,y=130)
e=Label(hi,bg="white",text="PASSWORD").place(x=10,y=170)
f=Label(hi,bg="white",text="GENDER").place(x=10,y=210)
g=Label(hi,bg="white",text="QUALIFICATION").place(x=10,y=250)
o=StringVar()
o.set("Select Any Standard")
o2=OptionMenu(hi,o,"6th","7th","8th","9th","10th","11th","12th").place(x=150,y=250)
f1=Radiobutton(hi,bg="white",text="MALE",value=1).place(x=145,y=210)
f2=Radiobutton(hi,bg="white",text="FEMALE",value=2).place(x=220,y=210)
f3=Radiobutton(hi,bg="white",text="OTHERS",value=3).place(x=295,y=210)
a1=Entry(hi,bd=3)
a1.place(x=150,y=10,width=135)
b1=Entry(hi,bd=3)
b1.place(x=150,y=50,width=135)
c1=Entry(hi,bd=3)
c1.place(x=150,y=90,width=135)
d1=Entry(hi,bd=3)
d1.place(x=150,y=130,width=135)
e1=Entry(hi,bd=3,show=".")
e1.place(x=150,y=170,width=135)
s=Button(hi,bd=3,text="SUBMIT",comm=grapes).place(x=200,y=300)
hi.mainloop()
