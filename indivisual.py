import copy
a=(1,2,3,4,[5,'hello'],'python')
b=copy.deepcopy(a)
b[-2][0]='good'
print(a,id(a))
print(b,id(b))
