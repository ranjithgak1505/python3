from collections import Counter
x=Counter("geeksforgeeks")
print(x)

for i in x.elements():
    print(i,end=" ")
print()
    
c=Counter({'geeks':3,'for':4,'geeeks':1})
for i in c.elements():
    print(i,end=" ")
print()


c=Counter([1,1,3,4,5,6,3,45,6,54])
for i in c.elements():
    print(i,end=" ")
print()
