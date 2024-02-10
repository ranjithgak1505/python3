import pymysql
mydb=pymysql.connect(
    host="localhost",
    database="agalya1",
    user="root",
    password="Ranjith143"
    )
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE owner(name VARCHAR(255),ADDRESS VARCHAR(255))")
print("table created")
