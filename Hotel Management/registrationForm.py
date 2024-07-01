from tkinter import *
screen=Tk()
screen.geometry("600x500")
screen.title("Hotel Management")
from registrationLogic import *

# Registration Form

r0=Label(screen,text='Please Enter Details Below',width=50,font=('white', 15,'bold'),background='orange')
r0.place(x=1,y=0)




r1=Label(screen,text='Name*',width=10,font=('black', 15,'bold'))
r1.place(x=30,y=50)

r2=Entry(screen,width=30,textvariable=name)
r2.place(x=200,y=50)




r3=Label(screen,text='Contact*',width=10,font=('black', 15,'bold'))
r3.place(x=30,y=100)

r4=Entry(screen,width=30,textvariable=contact)
r4.place(x=200,y=100)




r5=Label(screen,text='Email*',width=10,font=('black', 15,'bold'))
r5.place(x=30,y=150)

r6=Entry(screen,width=30,textvariable=email)
r6.place(x=200,y=150)




r7=Label(screen,text='Gender*',width=10,font=('black', 15,'bold'))
r7.place(x=30,y=200)



rbtn=Radiobutton(screen, text="Male",padx = 20, variable=gender, value='male')
rbtn.place(x=180,y=200)
rbtn=Radiobutton(screen, text="Female",padx = 20, variable=gender, value='female')
rbtn.place(x=300,y=200)





r8=Label(screen,text='City*',width=10,font=('black', 15,'bold'))
r8.place(x=30,y=250)

r9=Entry(screen,width=30,textvariable=city)
r9.place(x=200,y=250)



r10=Label(screen,text='State*',width=10,font=('black', 15,'bold'))
r10.place(x=30,y=300)

r11=Entry(screen,width=30,textvariable=state)
r11.place(x=200,y=300)




rb=Button(screen,width=20,text='Register',background='orange',font=('white', 10,'bold'),command=registrationFunc)
rb.place(x=200,y=350)


screen.mainloop()