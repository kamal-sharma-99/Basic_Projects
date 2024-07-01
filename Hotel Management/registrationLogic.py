import pymysql
mydb=pymysql.connect(host='localhost',user='root',password='',database='hotelManagement')
mycursor=mydb.cursor()

from tkinter import *


name = StringVar()
contact = IntVar()
email = StringVar()
gender = StringVar()
city = StringVar()
state = StringVar()

def registrationFunc():

    n=name.get()
    c=contact.get()
    e=email.get()
    g=gender.get()
    ci=city.get()
    s=state.get()



# Uploading Data To Server

    query="insert into guestregistration (name,contact,email,gender,city,state) values ('%s',%s,'%s','%s','%s','%s')"
    args=(n,c,e,g,ci,s)

    mycursor.execute(query%args)
    mydb.commit()