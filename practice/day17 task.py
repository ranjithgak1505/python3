n=int(input("enter the number"))
for i in range(0,n):
    for j in range(0,n+4):
         if(i==1 and j==1)or(i==1and j==5)or(i==2 and j==1)or(i==2 and j==2)or(i==2 and j==4)or(i==2 and j==5)or(i==3 and j==1)or(i==3 and j==3)or(i==3 and j==5)or(i==4 and j==1)or(i==4 and j==5)or(i==5 and j==1)or(i==5 and j==5):
          print("*",end=" ")
         else:
             print(" ",end=" ")
    print()



n=int(input("enter the number"))
for i in range(1,n+1):
        for j in range(1,n+5):
            if(j==1)or(j==5)or(i==2 and j==2)or(i==3 and j==3)or(i==2 and j==4):
             print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    
