def add(x,y):
    while y!=0:
        carry=x&y
        x=x^y
        y=carry<<1
    return x
print(add(3,7))


def subtract(x,y):
    while y!=0:
     borrow=(~x)&y
     x=x^y
     y=borrow<<1
    return x
print(subtract(4,2))
