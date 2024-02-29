count = 0
while (count<5):
    count+=1
    number=int(input('Enter the number of hashtags tall the pyramid should be: '))
    if number >= 1 and number <= 8:
        for i in range(number):
            print(' '*(number-i), end='')
            for j in range(number):
                if j <= i:
                    print('#', end='')
            print()
    else:
        print("Actually, there's a certain height range that we have to stay within. You know, zoning laws. What was that? You want to know the range? Too bad. You have four more tries.")
if count==5:
    print("Too bad, I guess we can't build it.")