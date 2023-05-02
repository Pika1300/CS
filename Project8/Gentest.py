def firstn(n):
    num=0
    while num<n:
        yield num
        num+=1

first= firstn(5)
i=first.__next__()
print(i)
print(first.__next__())
print(first.__next__())
print(first.__next__())
print(first.__next__())
