l=[2,23,56,56,78,65,4,456,67,78]
large=l[0]
small=l[0]
for num in l:
    if num>large:
        large=num
    if num<small:
        small=num
#l=[2,23,56,56,78,65,4,456,67,78]
print("large number",large)
print("small number",small)
            
