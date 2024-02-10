import collections
de=collections.deque([1,2,3])
print("deque:",de)
de.pop()

print("the deque after deleting the right side is:")
print(de)

de.popleft()
print("the deque after deleting the left side is:")
print(de)
