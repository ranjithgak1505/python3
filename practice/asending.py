#asscending order
#descending order
def sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr=[55,888,3,44,999,1000,666,222,3]
sort(arr)
print('1',arr)

print('='*50)

def sort2(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr=[55,888,3,44,999,1000,666,222,3]
sort2(arr)
print('2',arr)
