'''import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="Ranjith143"
    )
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE Ranjith")
'''


'''import pymysql
mydb=pymysql.connect(
    host="localhost",
    database="agalya",
    user="root",
    password="Ranjith143"
    )
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE owner(name VARCHAR(255),ADDRESS VARCHAR(255))")
print("table created")'''

'''import pymysql
mydb=pymysql.connect(
    host="localhost",
    database="agalya",
    user="root",
    password="Ranjith143"
    )
mycursor=mydb.cursor()
sql="insert into customers(name,address)VALUES(%s,%s)"
val=("john","chennai 2")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"was inserted.")
print("data inserted successfully")'''


'''import pymysql
mydb=pymysql.connect(
    host="localhost",
    database="agalya",
    user="root",
    password="Ranjith143"
    )
mycursor=mydb.cursor()
sql="delete from customers where name = 'john'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"records(s)deleted")'''

import pymysql
mydb=pymysql.connect(
    host="localhost",
    database="agalya",
    user="root",
    password="Ranjith143"
    )
mycursor=mydb.cursor()
sql="drop table owner"
mycursor.execute(sql)


'''import pymysql
mydb=pymysql.connect(
    host="localhost",
    database="agalya",
    user="root",
    password="Ranjith143"
    )
mycursor=mydb.cursor()
sql="drop table owner"
mycursor.execute(sql)'''


'''import pymysql
mydb=pymysql.connect(
    host="localhost",
    database="agalya",
    user="root",
    password="Ranjith143"
    )
mycursor=mydb.cursor()
sql="INSERT INTO customers (name,address) VALUES(%s,%s)"
val=[
    ('ranjith','chennai 4'),
    ('abi','ariyalur 4'),
    ('aswin','u patty 4')
    ]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"was inserted")'''
    


'''import pymysql
mydb=pymysql.connect(
    host="localhost",
    database="agalya",
    user="root",
    password="Ranjith143"
    )
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE owner(name VARCHAR(255),ADDRESS VARCHAR(255))")
print("table created")'''




