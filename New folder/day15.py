n=int(input("enter"))
for i in range(6,n):
    for j in range(6,n-i+1):
         print(end=" ")
    for j in range(i,1,-1):
         print(j,end=" ")
    for j in range(4,i+1):
         print(j,end="")
    print()
