import pymysql
a=pymysql.connect(
    host="localhost",
    user="root",
    password="Ranjith143",
    database="naga"
    )

mycursor=a.cursor()
mycursor.execute("CREATE TABLE student_register(f_name VARCHAR(50),l_name VARCHAR(50),course VARCHAR(50),course_package VARCHAR(50),date VARCHAR(50),age INT(50),gender VARCHAR(50),birth INT(50),contact INT(50),email VARCHAR(50),current_course VARCHAR(50),pending_course VARCHAR(50),completed_course VARCHAR(50),Total_fees INT(50),paid_fees INT(50),balance_fees INT(50))")
