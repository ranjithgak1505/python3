n=int(input("enter the number"))
for i in range(n):
    for j in range(0,i+i):
        print(end=" ")
    for j in range(0,3-i):
        print("*",end=" ")
    print()


n=int(input("enter the number"))
for i in range(n):
    for j in range(0,i):
        print(end=" ")
    for j in range(0,3-i):
        print("*",end=" ")
    print()

n=int(input("enter the number"))
for i in range(n):
    for j in range(0,n-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()


n=int(input("enter the number"))
for i in range(0,5):
    for j in range(0,i+1):
        print(j,end=" ")
    print()
    
