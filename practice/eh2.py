try:
    print(r)
except NameError:
    print("corect the name ")
except:
    print("hello world")


try:
    print("r")
except NameError:
    print("corect the name ")
except:
    print("hello world")
else:
    print("the element is corrct")
    


try:
    print(v)
except:
    print("corect the name ")
else:
    print("hello world")


x=5
if not type(x)is int:
    raise TypeError("only integers are allowed")
else:
    print("zn")

comment=int(input("Enter the value:"))
pass1=int(input("enter the value:"))
print(comment+pass1)
