import collections
dic1={'a':1,'b':2}
dic2={'b':3,'d':4}
dic3={'f':5}

chain=collections.ChainMap(dic1,dic2)
print(chain)

chain1=chain.new_child(dic3)
print(chain1.maps)

print("displaying new chainmap:")
print(chain1.maps)

print("value associated with b before reversing is:",end="")
print(chain1['b'])

chain1.maps=reversed(chain1.maps)

print("value associated with b after reversing is:",end="")
print(chain1['b'])


