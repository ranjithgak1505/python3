from collections import OrderedDict
od=OrderedDict()
od['a']=1
od['b']=2
od['c']=3
od['d']=4
od['e']=5

print("\n after deleting:\n")
od.pop('c')
for key,values in od.items():
    print(key,values)
print("\n after reinserting:\n")
od['c']=3
for key,values in od.items():
    print(key,values)
