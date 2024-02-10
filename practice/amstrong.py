n=int(input("enter your number"))
copy=n
digit=0
string=str(n)
for i in string:
    digit+=1
print("digit",digit)
sum=0
while n>0:
    unit=n%10
    n=n//10
    sum+=(unit**digit)
print(sum)
if sum==copy:
    print("your number is amstrong number")
else:
    print("your number is not amstrong number")
    
