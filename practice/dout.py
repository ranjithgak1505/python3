 


n=int(input("enter row value"))
for i in range(1,n+1):
     for j in range(1,n+n):
          if(i+j==5 or i==n-1 or j-i==3):
               print("*",end=" ")
          else:
               print(end=" ")
     print()       
