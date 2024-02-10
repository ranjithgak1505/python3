n=int(input("enter:"))
c=0
for i in range(0,n):
    for j in range(0,n-i-1):
         print(" ",end="")
    c+=2
    for j in range(0,2,2):
        print(j,end=" ")
    print()

