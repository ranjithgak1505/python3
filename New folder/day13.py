n=int(input('enter your number:'))
for x in range(3):
    for y in range(0,x-n-1):
        print(" ",end=" ")
    for y in range(0,x+1):
        print("*",end=" ")
    print("")
    
