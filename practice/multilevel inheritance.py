class addition:
    def add(self):
        a=int(input("enter the a value:"))
        b=int(input("enter the b value:"))
        c=a+b
        print("The addition value is:",c)
class subtraction(addition):
    def sub(self):
        a=int(input("enter the a value:"))
        b=int(input("enter the b value:"))
        c=a-b
        print("The subtraction value is:",c)
class multiplication(subtraction):
    def mul(self):
        a=int(input("enter the a value:"))
        b=int(input("enter the b value:"))
        c=a*b
        print("The multiplication value is:",c)
class divison(multiplication):
    def div(self):
        a=int(input("enter the a value:"))
        b=int(input("enter the b value:"))
        c=a/b
        print("The divison value is:",c)
class final(divison):
    def logic(self):
        self.add()
        self.sub()
        self.mul()
        self.div()
obj=final()
obj.logic()

