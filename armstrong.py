a=int(input('enter the numbet'))
tem=a
rem=0
sum=0
while(a>0):
      digit=rem%10
      sum=sum*10+digit**3 
      a=a//10
if(sum==a):
       print(' number is armstrong')
else:
       print('not')
