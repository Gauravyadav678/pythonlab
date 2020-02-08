a=int(input('enter the number'))
factorial=1
if a<0:
    print('no factorial')
elif a==1:
    print('yes factorial')
else:
    for i in range(1,a+1):
        factorial=factorial*i
print(factorial)        
    
