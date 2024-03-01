print("Hey. I'm the  architect. I'll help you build half of a pyramid. Yes, half. No, I don't know why. Anyways, how tall should I build it?")
count = 0
while (count<3):
    count+=1
    number = int(input('Enter the number of hashtags tall the pyramid should be: '))
    if number >= 1 and number <= 8:
        count = 5
        for i in range(number):
            print(' '*(number-i), end='')
            for j in range(number):
                if j <= i:
                    print('#', end='')
            print()
        print("There you go! My job here is done.")
    else:
        if count == 1:
            print("Actually, there's a certain height range that we have to stay within. You know, zoning laws. What was that? You want to know the range? Too bad. Guess. You have two more tries.")
        elif count == 2:
            print("Not gonna work buddy, I'm sorry. One more chance. How tall should it be? :)")
if count==3:
    print("Too bad, I guess we can't build it. :/")