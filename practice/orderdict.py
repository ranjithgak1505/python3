from collections import OrderedDict
print("this is a Dict:\n")
d={}
d['a']=1
d['b']=2
d['c']=3
d['d']=4
d['e']=5
d['f']=6
d.pop('c')
for key,values in d.items():
    print(key,values)

    
print("this is a OrderedDict:\n")
od=OrderedDict()
od['a']=1
od['b']=2
od['c']=3
od.pop('c')
for key,values in od.items():
    print(key,values)

