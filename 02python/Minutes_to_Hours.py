#converts minutes to hours
print('Enter minutes:')
m = int(input())
if m / 60 >= 2 or m / 60 < 1:
    print(m // 60, 'hours and', m % 60, 'minutes.')
else:
    print(m // 60, 'hour and', m % 60, 'minutes.')
