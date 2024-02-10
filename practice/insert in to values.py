import pymysql
mydb=pymysql.connect(
    host="localhost",
    database="agalya1",
    user="root",
    password="Ranjith143"
    )
mycursor=mydb.cursor()
sql="INSERT INTO owner (name,address) VALUES(%s,%s)"
val=[
    ('ranjith','chennai 4'),
    ('abi','ariyalur 4'),
    ('aswin','u patty 4')
    ]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"was inserted")
    
