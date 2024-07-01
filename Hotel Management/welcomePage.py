import pymysql
mydb=pymysql.connect(host='localhost',user='root',password='',database='hotelManagement')
mycursor=mydb.cursor()

from tkinter import *
screen=Tk()
screen.geometry("600x750")
screen.title("Hotel Management")


l1=Label(screen,text='WELCOME',height=1,width=20,borderwidth=1,relief='solid',font=('black', 15,'bold'))
l1.place(x=220,y=20)
l2=Label(screen,text='HOTEL MANAGEMENT',height=2,width=30,font=('black', 15,'bold'))
l2.place(x=270,y=65)
l3=Label(screen,text='PYTHON TKINTER',height=2,width=30,font=('black', 15,'bold'))
l3.place(x=270,y=140)
l4=Label(screen,text='GUI',height=2,width=30,font=('black', 15,'bold'))
l4.place(x=270,y=220)

c_value=StringVar()

def checkin():
    value1="You Are Checked Inn"
    c_value.set(value1)

b1=Button(screen,width=30,height=2,text='1. CHECK INN',command=checkin)
b1.place(x=80,y=65)
l4=Label(screen,textvariable=c_value,height=2,width=30,font=('black', 15,'bold'))
l4.place(x=80,y=350)



guest_List=StringVar()

def guestListFunc():
    query='select * from booking'
    mycursor.execute(query)
    getAllData=mycursor.fetchone()
    guest_List.set(getAllData)

b2=Button(screen,width=30,height=2,text='2. SHOW GUEST LIST',command=guestListFunc)
b2.place(x=80,y=110)

l4=Label(screen,textvariable=guest_List,height=15,background='grey',width=60)
l4.place(x=80,y=470)

check_out=StringVar()

def checkout():
    value1="You Are Checked Out"
    check_out.set(value1)

b3=Button(screen,width=30,height=2,text='3. CHECK OUT',command=checkout)
b3.place(x=80,y=155)
l4=Label(screen,textvariable=check_out,height=2,width=30,font=('black', 15,'bold'))
l4.place(x=80,y=400)




b4=Button(screen,width=30,height=2,text='4. GET INFO OF ANY GUEST')
b4.place(x=80,y=200)

def exitFunc():
    quit()
b5=Button(screen,width=30,height=2,text='5. EXIT',command=exitFunc)
b5.place(x=80,y=245)



screen.mainloop()