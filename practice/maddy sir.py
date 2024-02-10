n=int(input("enter the number:"))
for i in range(n):
    for j in range(0,n-i):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(1,i+1):
        print(end=" ")
    for j in range(0,n-i):
        print("*",end=" ")
    print()
    
