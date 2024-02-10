print(ord('22'))
l="     welcome     to     backend     dev     "
for v in l:
    if v.count(ord(' '))>1:
        v.pop()
        print(v)    

