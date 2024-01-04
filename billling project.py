

from tkinter import*

hi=Tk()
hi.title("BILLING PROCESS")
hi.geometry("1000x1000")
hi.resizable(False,False)

def clr():
    q1.delete(0,END)
    q2.delete(0,END)
    q3.delete(0,END)
    q4.delete(0,END)
    q5.delete(0,END)
    
def total():
    try:a1 =int(q1.get())
    except:a1=0
    try:a2 =int(q2.get())
    except:a2=0
    try:a3 =int(q3.get())
    except:a3=0
    try:a4 =int(q4.get())
    except:a4=0
    try:a5 =int(q5.get())
    except:a5=0

    StrawberryFalooda=a1*190
    StrawberryIcecreams=a2*150
    pinkcakes=a3*50
    candy=a4*50
    chocolatelava=a5*180
    total=(StrawberryFalooda+StrawberryIcecreams+pinkcakes+candy+chocolatelava)
    bill=str('%d' %total)

    y.config(text=total,bg="azure2",fg="black")

bg=PhotoImage(file='ap.png')
z=Label(hi,image=bg)
z.place(x=0,y=0)


x=Label(hi,font=("gabriola",45,"bold",),text="STRAWBERRY BAE")
x.place(x=600,y=8)
i=Label(hi,font="modern",text="ITEMS")
i.place(x=30,y=180)
q=Label(hi,font="modern",text="QUANTITY")
q.place(x=200,y=180)
p=Label(hi,font="modern",text="PRICE")
p.place(x=450,y=180)
t=Label(hi,font="modern",text="TOTAL")
t.place(x=750,y=180)
i1=Label(hi,text="STRAWBERRY FALOODA")
i1.place(x=10,y=230)
i2=Label(hi,text="STRAWBERRY ICE CREAMS")
i2.place(x=10,y=270)
i3=Label(hi,text="PINKY CAKES")
i3.place(x=10,y=310)
i4=Label(hi,text="CANDY")
i4.place(x=10,y=350)
i5=Label(hi,text="CHOCOLATE LAVA")
i5.place(x=10,y=390)
q1=Entry(hi,bd=3)
q1.place(x=170,y=230)
q2=Entry(hi,bd=3)
q2.place(x=170,y=270)
q3=Entry(hi,bd=3)
q3.place(x=170,y=310)
q4=Entry(hi,bd=3)
q4.place(x=170,y=350)
q5=Entry(hi,bd=3)
q5.place(x=170,y=390)

p1=Label(hi,text="STRAWBERRY FALOODA=RS.190")
p1.place(x=400,y=230)
p2=Label(hi,text="STRAWBERRY ICE CREAMS=RS.150")
p2.place(x=400,y=270)
p3=Label(hi,text="PINKY CAKES=RS.50")
p3.place(x=400,y=310)
p4=Label(hi,text="CANDY=RS.50")
p4.place(x=400,y=350)
p5=Label(hi,text="CHOCOLATE LAVA=RS.180")
p5.place(x=400,y=390)

y=Label(hi,bg="azure2",fg="black",text="",width=17)
y.place(x=700,y=230)

but=Button(hi,text="TOTAL",command=total).place(x=700,y=450)
but1=Button(hi,text="CLEAR",command=clr).place(x=530,y=450)
hi.mainloop()


