import pymysql
mydb=pymysql.connect(
    host="localhost",
    database="agalya1",
    user="root",
    password="Ranjith143"
    )
mycursor=mydb.cursor()
sql="delete from owner where name='ranjith'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"records(s) afffected")
    
