class A:
    def __init__(self,a):
        self.a=a
    def add(self):
        y=self.a+self.a
        print(y)
obj=A(5)
obj.add()
obj=A(6)
obj.add()
