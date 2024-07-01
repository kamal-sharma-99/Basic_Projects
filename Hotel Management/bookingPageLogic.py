import pymysql
mydb=pymysql.connect(host='localhost',user='root',password='',database='hotelManagement')
mycursor=mydb.cursor()
from tkinter import *

name=StringVar()
address=StringVar()
number=IntVar()
days=IntVar()
room=StringVar()
payment=StringVar()



def booking():
    d_name=name.get()
    d_address=address.get()
    d_number=number.get()
    d_days=days.get()
    d_room=room.get()
    d_payment=payment.get()

    query="insert into booking (name,address,number,days,room,payment) values ('%s','%s',%s,%s,'%s','%s')"
    args=(d_name,d_address,d_number,d_days,d_room,d_payment)
    print(d_name,d_address,d_number,d_days,d_room,d_payment)

    mycursor.execute(query%args)
    mydb.commit()