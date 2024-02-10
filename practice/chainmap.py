from collections import ChainMap
d1={'a':1,'b':2,'c':3}
d2={'v':3,'d':3,'c':5}
c=ChainMap(d1,d2)
print(c)

import collections
d1={'a':1,'b':2,'c':3}
d2={'v':3,'d':3,'c':5}
Chain=collections.ChainMap(d1,d2)
print(Chain)

print("all the ChainMap content are:")
print(Chain.maps)

print("all the key values are:")
print(list(Chain.keys()))

print("all values of ChainMap are:")
print(list(Chain.values()))



