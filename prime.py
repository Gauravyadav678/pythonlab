l=[1,2,3,5,376,4,78,585,8,5,87]
primelist = []
for number in l:
        if number > 1 :
            for i in range(2,number):
               if(number%i) ==0:
                  break
            else:
               print(number,'is a prime')
print('prinmelist',primelist)
