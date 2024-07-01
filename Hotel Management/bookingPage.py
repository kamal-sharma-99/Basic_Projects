from tkinter import *
screen=Tk()
screen.geometry("1000x650")
screen.title("Hotel Management system")
from bookingPageLogic import *


l1 = Label(screen,text='YOU CLICKED ON      :      CHECK IN',height=2,width=80,borderwidth=1,relief='solid',font=('black',15,'bold'))
l1.place(x=20,y=20)

r1 = Label(screen,text='ENTER YOUR NAME   :',font=('black',10,'bold'))
r1.place(x=200,y=100)
r2=Entry(screen,width=50,textvariable=name)
r2.place(x=500,y=100)
r1 = Label(screen,text='ENTER YOUR ADDRESS   :',font=('black',10,'bold'))
r1.place(x=200,y=150)
r3=Entry(screen,width=50,textvariable=address)
r3.place(x=500,y=150)
r1 = Label(screen,text='ENTER YOUR NUMBER   :',font=('black',10,'bold'))
r1.place(x=200,y=200)
r4=Entry(screen,width=50,textvariable=number)
r4.place(x=500,y=200)
r1 = Label(screen,text='NUMBER OF DAYS   :',font=('black',10,'bold'))
r1.place(x=200,y=250)
r5=Entry(screen,width=50,textvariable=days)
r5.place(x=500,y=250)


r1 = Label(screen,text='CHOOSE YOUR ROOM',font=('black',15,'bold'))
r1.place(x=350,y=300)
r1 = Label(screen,text='CHOOSE PAYMENT METHOD',font=('black',15,'bold'))
r1.place(x=350,y=450)






Button1 = Radiobutton(screen, text = "DELUXE",variable = room,value='DELUXE',height = 2,width = 10,font=('black',10,'bold'))
Button1.place(x=200,y=330)
Button1 = Radiobutton(screen, text = "GENERAL",variable = room,value='GENERAL',height = 2,width = 10,font=('black',10,'bold'))
Button1.place(x=200,y=380)
Button1 = Radiobutton(screen, text = "FULL DELUXE",variable = room,value='FULL DELUXE',height = 2,width = 10,font=('black',10,'bold'))
Button1.place(x=600,y=330)
Button1 = Radiobutton(screen, text = "JOINT",variable = room,value='JOINT',height = 2,width = 10,font=('black',10,'bold'))
Button1.place(x=600,y=380)


payment1 = Radiobutton(screen, text = "By Cash",variable = payment,value='By Cash',height = 2,font=('black',10,'bold'))
payment1.place(x=200,y=480)
payment1 = Radiobutton(screen, text = "By Credit Card / Debit Card",variable = payment,value='By Credit Card / Debit Card',height = 2,font=('black',10,'bold'))
payment1.place(x=600,y=480)






rb=Button(screen,width=20,text='SUBMIT',font=('black', 10,'bold'),height=2,command=booking)
rb.place(x=400,y=560)


screen.mainloop()