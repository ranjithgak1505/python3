class overloading:
    def method(self,*args):
        sum=0
        for i in args:
            sum+=i
        print(sum)
obj=overloading()
obj.method(4)
obj.method(5,4,6)


