def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname="vinith",lname="bvn",snmae="jdkjf")


def my_function(food):
    for x in food:
        print(x)
x=["apple","ornge","banana"]
my_function(x)

def add(a,b):
    return a+b
c=add(3,4)
print(c)

def recursive_factorial(n):
    if n==1:
        return n
    else:
        return n* recursive_factorial(n-1)
num=6
if num<0:
    print("invalid input!please enter a possitive number")
elif num==0:
    print("factorial of number 0 is 1")
else:
    print("factorial of number",num,"=",recursive_factorial(num))


x=lambda a:a + 10
print(x(30))


x=lambda a,b:a*b
print(x(4,2))

x=lambda a,b,c:a+b+c
print(x(2,3,4))

def myfun(n):
    return lambda a:a*n
mydoubler=myfun(2)
print(mydoubler(11))

def myfun(n):
    return lambda a:a*n
mydoubler=myfun(2)
mytripular=myfun(3)
print(mydoubler(11))
print(mytripular(11))

