import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="Ranjith143",
    database="agalya1"
    )
mycursor=mydb.cursor()
sql="UPDATE owner SET address='ariyalur5' WHERE name='abi'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"records(s) afffected")
    
