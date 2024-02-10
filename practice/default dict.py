from collections import defaultdict
def def_value():
    return"not present"
d=defaultdict(def_value)
d["a"]=1
d["b"]=2

print(d["a"])
print(d["b"])
print(d["h"])
