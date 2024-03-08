# Power Documentation

I have to use these three functions:

```python
def print_graph(n):

def get_power(x, n):

for i in range(-8, 9):
```

To make this: 
```
****************************************************************
*************************************************
************************************
*************************
****************
*********
****
*

*
****
*********
****************
*************************
************************************
*************************************************
****************************************************************
```

First, I filled out the get_power function with a ```return x \** n```.

Then, I filled out the print_graph(n) with ```print('*' * n)``` to print an asterisk ```n``` times.

Finally, I filled out the ```for``` line. I called the print_graph function and printed the asterisk the number of times specified by calling the get_power function. In the get power function, I used ```i``` as the base and 2 as the exponent. The value given to i becomes the x in the y = x^2 function. It is squared for each i.