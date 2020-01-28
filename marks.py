a = int(input('enter the marks in physics '))
b = int(input('enter the marks in chemistry '))
c = int(input('enter the marks in maths '))
f = int(input('enter the marks in english'))
g = int(input('enter the marks in programming '))
d = (a+b+c+f+g)/500
marks = d*100
if marks >= 75:
    print("*****")
    print('fassed from first devision')
elif marks >=60:
    print("***")
    print('fassed from 2 nd devision')
elif marks >=33:
    print("*")
    print('passsed from 3 rd devision')
else:
    print("no any star")
    print('you are fail please try again')
    

        
