print('This program tells you which season it is in Boston.')
x = 0
while x==0:
    month = int(input("Enter a number from 1-12, corresponding to the months in the year: "))
    if month > 12 or month < 1:
        print("There are onlty 12 months in a year.")
    elif month <= 6 and month >= 4:
        print('Boston is in Spring.')
        x+=1
    elif month <= 9 and month >= 7:
        print('Boston is in Summer.')
        x+=1
    elif month <= 11 and month >= 10:
        print('Boston is in Autumn.')
        x+=1
    else:
        print('Boston is in Winter.')
        x+=1