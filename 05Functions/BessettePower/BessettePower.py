def print_graph(n):
    print('*' * n)

def get_power(x, n):
    return x ** n

for i in range(-8, 9):
    print_graph(get_power(i, 2))