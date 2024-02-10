try:
    def function():
        print("Q")
    function()
except:
    print("fisrt you assign the q values")
else:
    print("printed")
try:
    a=10
    b=0
    print(a/b)
except NameError:
    print("something nameerror")
except ArithmeticError:
    print("arithmeticerror")
except:
    print("anything else")

