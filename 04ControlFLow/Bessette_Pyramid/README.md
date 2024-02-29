```print('This program makes a pyramid out of hashtags.')
number=int(input('Enter the number of hashtags tall the pyramid should be: '))
count = 0
while(count<number):
    print(' '*(number-count)+'#'*(count))
    count+=1
```
    
* prints 1 less height than needed
    

```print('This program makes a pyramid out of hashtags.')
number=int(input('Enter the number of hashtags tall the pyramid should be: '))
for i in range(number, 0):
    print(' '*(i-1)+'#'*abs(1-i))
```
* I don't think it can count backwards
    
    
```print('This program makes a pyramid out of hashtags.')
number=int(input('Enter the number of hashtags tall the pyramid should be: '))
for i in range(number):
    for j in range(number):
        if j <= i:
            print(' '*(number)+'#', end='')
    print()
```
* This put too many space in between

```number=int(input('Enter the number of hashtags tall the pyramid should be: '))
for i in range(number):
    for j in range(number):
        if j <= i:
            print('#', end='')
    print()
* prints the correct height but leans left

number=int(input('Enter the number of hashtags tall the pyramid should be: '))
for i in range(number):
    print(' '*(number-i), end='')
    for j in range(number):
        if j <= i:
            print('#', end='')
    print()
```
* This works for any height. It leans right. Now to put the restrictions.

```count = 0
while (count<5):
    count+=1
    number=int(input('Enter the number of hashtags tall the pyramid should be: '))
    
    # this is the important restriction:
    if number >= 1 and number <= 8:**
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
* The important part has a comment. This restricts it to between 1 and 8. Everything else was just flavor.

