n="python"
for i in range(0,len(n)):
    for j in range(0,i+1):
        print(n[j],end=" ")
    print()
for i in range(0,len(n)):
    for j in range(len(n)-i-1):
         print(n[j],end=" ")
    print()
