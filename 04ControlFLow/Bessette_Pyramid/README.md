# Documentation for Pyramid

## Iterations and Issues

1. Prints 1 less height than needed.
```python
print('This program makes a pyramid out of hashtags.')
number=int(input('Enter the number of hashtags tall the pyramid should be: '))
count = 0
while(count<number):
    print(' '*(number-count)+'#'*(count))
    count+=1
```
    
2. I don't think it can count backwards.
```python
print('This program makes a pyramid out of hashtags.')
number=int(input('Enter the number of hashtags tall the pyramid should be: '))
for i in range(number, 0):
    print(' '*(i-1)+'#'*abs(1-i))
```
    
3. This put too many space in between.
```python
print('This program makes a pyramid out of hashtags.')
number=int(input('Enter the number of hashtags tall the pyramid should be: '))
for i in range(number):
    for j in range(number):
        if j <= i:
            print(' '*(number)+'#', end='')
    print()
```

4. Prints the correct height but leans left.
```python
number=int(input('Enter the number of hashtags tall the pyramid should be: '))
for i in range(number):
    for j in range(number):
        if j <= i:
            print('#', end='')
    print()
```

5. This works for any height. It leans right. Now to put the restrictions.
```python
number=int(input('Enter the number of hashtags tall the pyramid should be: '))
for i in range(number):
    print(' '*(number-i), end='')
    for j in range(number):
        if j <= i:
            print('#', end='')
    print()
```
6. The important part of this is the fifth line reading ```if number >= 1 and number <= 8:``` This restricts it to between 1 and 8. Everything else was just flavor. Except whoops, it runs 5 times even if you enter a valid number and then displays too bad text. I have to separate the valid inputs from invalid in the count.
```python
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
```
7. I added more flavor to the description of what the program does. I changed the count to 3 chances. I kept the set count to five though because that terminates the loop (it's greater than 3. I added a second wrong entry flavor text. The third I changed to trigger on the third wrong entry.
```python
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
```

# Documentation for FizzBuzz

## Iterations and Issues

1. Prints no numbers, only words with space between them. I need to think about how the nested for loops are working.
```python
for i in range(1, 101, 1):
    for three in range(1, 101, 1):
        if three % 3 == 0 and three % 5 == 0:
            print('FizzBuzz')
        elif three % 3 == 0:
            print('Fizz')
        elif three % 5 == 0:
            print('Buzz')
        else:
            print()
```
2. Trying some pseudocode. First counter = 1. I need it to print unless certain conditions are true, then print something else. After some working I decided against this approach. I'll try to make an if for each possible condition.
</br>
3. The four possible conditions are that the number is evenly divisible by neither 3 or 5, both 3 and 5, 3 but not 5, and 5 but not 3. This code reflects that, and works.

```python
for i in range(1, 101, 1):
    if i % 3 != 0 and i % 5 != 0:
        print(i)
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    if i % 3 == 0 and i % 5 != 0:
        print('Fizz')
    if i % 5 == 0 and i % 3 != 0:
        print('Buzz')
```
