#n=int(input("enter the number:"))
def recursive_factorial(l):
    if l==1:
        return l
    else:
        return l* recursive_factorial(l-1)
num=5
if num<0:
    print("invalid input!please enter a possitive number")
elif num==0:
    print("factorial of number 0 is 1")
else:
    print("factorial of number",num,"=",recursive_factorial(num))
