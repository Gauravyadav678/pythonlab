a=int(input('enter the year'))
if a%4==0:
    if a%100==0:
        if a%400==0:
            print("{0} is leap year".format(a))
        else:
            print("{0} is not leap year".format(a))
    else:
        print("{0} is leap year ".format(a))
else:
    print("{0} is not leap year".format(a))
    
