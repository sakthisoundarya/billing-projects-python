from tkinter import*
from tkinter import messagebox
import mysql.connector

hi=Tk()
hi.title("LOG_IN")
hi.geometry("500x250")
hi.resizable(False,False)

Label(hi,text="SIGN IN",font=("arial",25)).pack(side="top")

def berry():
    username=a1.get()
    password=b1.get()
    if(username="" or password=""):
        messagebox.showinfo("ERROR","Fill the details!!!")
    else:
        comm=mysql.connector.connect(host="localhost",user="root",password="",database=




a=Label(hi,text="USERNAME   :").place(x=30,y=90)

a1=Entry(hi,width=20,bd=3)
a1.place(x=150,y=90)

b=Label(hi,text="PASSWORD   :").place(x=30,y=150)

b1=Entry(hi,width=20,bd=3)
b1.place(x=150,y=150)

o=StringVar()
o.set("Select The User ")
o2=OptionMenu(hi,o,"Staff","Doctor","Patient").place(x=350,y=115)

