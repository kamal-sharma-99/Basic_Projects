import pymysql
mydb=pymysql.connect(host='localhost',user='root',password='')
mycursor=mydb.cursor()

mycursor.execute('create database if not exists hotelManagement')
mydb.commit()

mydb=pymysql.connect(host='localhost',user='root',password='',database='hotelManagement')
mycursor=mydb.cursor()

mycursor.execute('create table booking (id int primary key auto_increment, name varchar(20), address varchar(20), number int, days int, room varchar(20), payment varchar(20))')
mydb.commit()