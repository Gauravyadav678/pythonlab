a=int(input('enter the value'))
b=int(input('enter the value'))
c=int(input('enter the value'))
d=b*b-4*a*c
if d<0:
    print('roots are imaginary')
elif d>0:
    x=-b*(d**.5)/2*a
    y=b*(d**.5)/2*a
    print(x)
    print(y)
