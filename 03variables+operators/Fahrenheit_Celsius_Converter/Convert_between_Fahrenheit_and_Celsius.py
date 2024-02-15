print('This program converts between Fahrenheit and Celsius')
while True:
    F_or_C = input('Type F to convert to Fahrenheit or C to convert to Celsius: ')
    if len(F_or_C) > 0:
        if F_or_C == 'F':
            c = float(input('Type # of degrees Celsius: '))
            print(f'\n{c} degrees Celsius is {(9 / 5) * c + 32} degrees Fahrenheit.\n ')
        elif F_or_C == 'C':
            f = float(input('Type # of degrees Fahrenheit: '))
            print(f, 'degrees Fahrenheit is', (5/9) * (f - 32), 'degrees Celsius.')