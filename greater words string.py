a=input('enter the string')
h=int(input('enter the length'))
k=a.split()
s=[]
m=' '
for i in k:
    if len(i)>h:
        s.append(i)
d=m.join(s)
print('words which is greater than given length: ',d)
