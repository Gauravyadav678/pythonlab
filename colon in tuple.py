import copy
a=('hello',2,3,4,[2,5])
b=copy.deepcopy(a)
b[4][0]=5
print(a)
print(b)


