Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

Warning (from warnings module):
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python312/named tuple in python.py", line 2
    category1=namedtuple('dates'['date','month','year'])
SyntaxWarning: str indices must be integers or slices, not tuple; perhaps you missed a comma?
>>> 
===================================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python312/named tuple in python.py ====================================
Traceback (most recent call last):
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python312/named tuple in python.py", line 2, in <module>
    category1=namedtuple('dates'['date','month','year'])
TypeError: string indices must be integers, not 'tuple'

===================================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python312/named tuple in python.py ====================================
Traceback (most recent call last):
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python312/named tuple in python.py", line 5, in <module>
    tommrow=category(1,2,3343)
NameError: name 'category' is not defined. Did you mean: 'category1'?

===================================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python312/named tuple in python.py ====================================
dates(date=1, month=2, year=3343)
dates(date=1, month=3, year=4454)
dates(date=1, month=2, year=3343)

===================================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python312/named tuple in python.py ====================================
dates(date=1, month=2, year=3343)
dates(date=1, month=3, year=4454)
dates(date=1, month=2, year=3343)
3343
3
1

============================================================== RESTART: D:/practice/namedtuple std.py =============================================================
Traceback (most recent call last):
  File "D:/practice/namedtuple std.py", line 1, in <module>
    from collectons import namedtuple
ModuleNotFoundError: No module named 'collectons'
>>> 
============================================================== RESTART: D:/practice/namedtuple std.py =============================================================
Traceback (most recent call last):
  File "D:/practice/namedtuple std.py", line 1, in <module>
    from collectons import namedtuple
ModuleNotFoundError: No module named 'collectons'
>>> 
============================================================== RESTART: D:/practice/namedtuple std.py =============================================================
Traceback (most recent call last):
  File "D:/practice/namedtuple std.py", line 2, in <module>
    student1=namedtuple(student,['name','age','dob'])
NameError: name 'student' is not defined
>>> 
============================================================== RESTART: D:/practice/namedtuple std.py =============================================================
student(name='ranjith', age='12', dob='0134')
the student ags is:12
the student name is:ranjith
the student age is:12
>>> 
============================================================== RESTART: D:/practice/namedtuple std.py =============================================================
student(name='ranjith', age='12', dob='0134')
the student ags is:12
the student name is:ranjith
the student dob is:0134
>>> 
============================================================== RESTART: D:/practice/namedtuple std.py =============================================================
student(name='ranjith', age='12', dob='0134')
the student ags is:
12
the student name is:
ranjith
the student dob is:
0134
>>> 
============================================================== RESTART: D:/practice/namedtuple std.py =============================================================
student(name='ranjith', age='12', dob='0134')
the student ags is:12
the student name is:ranjith
the student dob is:0134
