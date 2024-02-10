import collections
de=collections.deque([1,2,3])
print("deque:",de)
print()

de.append(4)
print("the deque after append at right is:")
print(de)
print()

de.appendleft(6)
print("the deque after leftappend is:")
print(de)
print()

