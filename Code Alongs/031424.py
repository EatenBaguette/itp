from random import random as r
list = []
width = 10
for i in range(width):
    list.append(width/2)
count = 0
while count < 100:
    for i in range(len(list)-1, 0, -1):
        list[i] = list[i-1]
    list[0]=int(r()*10)
    for i in range(1, width):
        
    count += 1