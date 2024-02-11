print('This program makes a grid.')
print('Enter the width of the grid:')
w = int(input())
print('Enter the height of the grid:')
h = int(input())

# creates the rows
for i in range(h):
    # creates the columns
    print(('+ ' + '- ' * 4) * w + '+')
    for i in range(4):
        print(('/ ' + '  ' * 4) * w + '/')
# creates bottom border
print(('+ ' + '- ' * 4) * w + '+')

# by Ethan Bessette
