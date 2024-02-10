n=int(input("enter the number"))
c=0
for i in range(0,n):
    for j in range(0,n-i-1):
        print(end=" ")
    c=c+2
    for j in range(c,0,-2):
        print(j,end=" ")
    print()

n=int(input("enter"))
for i in range(1,n+1):
    for j in range(1,n+n):
        if(i+j==n+1 or i==n or j-i==n-1):
           print("*",end="")
        else:
           print(end=" ")
    print()
