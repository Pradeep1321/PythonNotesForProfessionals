"""
Chapter 69: Map Function
Parameter                       Details
function            function for mapping (must take as many parameters as there are iterables) (positional-only)
iterable            the function is applied to each element of the iterable (positional-only)

*additional_iterables see iterable, but as many as you like (optional, positional-only)

Section 69.1: Basic use of map, itertools.imap and future_builtins.map
The map function is the simplest one among Python built-ins used for functional programming. map() applies a
specified function to each element in an iterable:


names = ['Fred', 'Wilma', 'Barney']
Python 3.x Version ≥ 3.0
map(len, names) # map in Python 3.x is a class; its instances are iterable
# Out: <map object at 0x00000198B32E2CF8>
A Python 3-compatible map is included in the future_builtins module:
Python 2.x Version ≥ 2.6
from future_builtins import map # contains a Python 3.x compatible map()
map(len, names) # see below
# Out: <itertools.imap instance at 0x3eb0a20>
Alternatively, in Python 2 one can use imap from itertools to get a generator
Python 2.x Version ≥ 2.3
map(len, names) # map() returns a list
# Out: [4, 5, 6]
from itertools import imap
imap(len, names) # itertools.imap() returns a generator
# Out: <itertools.imap at 0x405ea20>
The result can be explicitly converted to a list to remove the differences between Python 2 and 3:
list(map(len, names))
# Out: [4, 5, 6]
map() can be replaced by an equivalent list comprehension or generator expression:
[len(item) for item in names] # equivalent to Python 2.x map()
# Out: [4, 5, 6]
(len(item) for item in names) # equivalent to Python 3.x map()
# Out: <generator object <genexpr> at 0x00000195888D5FC0>

Section 69.2: Mapping each value in an iterable

functools.partial is a convenient way to fix parameters of functions so that they can be used with map instead of
using lambda or creating customized functions.

Section 69.3: Mapping values of dierent iterables

There are different requirements if more than one iterable is passed to map depending on the version of python:
The function must take as many parameters as there are iterables:

def median_of_three(a, b, c):
    return sorted((a, b, c))[1]
list(map(median_of_three, measurement1, measurement2))
    TypeError: median_of_three() missing 1 required positional argument: 'c'

list(map(median_of_three, measurement1, measurement2, measurement3, measurement3))
    TypeError: median_of_three() takes 3 positional arguments but 4 were given

Python 2.x Version ≥ 2.0.1
map: The mapping iterates as long as one iterable is still not fully consumed but assumes None from the fully consumed iterables:

measurement1 = [100, 111, 99, 97]
measurement2 = [102, 117]
# Calculate difference between elements
list(map(operator.sub, measurement1, measurement2))
    TypeError: unsupported operand type(s) for -: 'int' and 'NoneType'

itertools.imap and future_builtins.map: The mapping stops as soon as one iterable stops:

import operator
from itertools import imap
measurement1 = [100, 111, 99, 97]
measurement2 = [102, 117]
# Calculate difference between elements
list(imap(operator.sub, measurement1, measurement2))
# Out: [-2, -6]
list(imap(operator.sub, measurement2, measurement1))
# Out: [2, 6]


Python 3.x Version ≥ 3.0.0
The mapping stops as soon as one iterable stops:
import operator
measurement1 = [100, 111, 99, 97]
measurement2 = [102, 117]
# Calculate difference between elements
list(map(operator.sub, measurement1, measurement2))
# Out: [-2, -6]
list(map(operator.sub, measurement2, measurement1))
# Out: [2, 6]

#Section 69.4: Transposing with Map: Using "None" as function argument (python 2.x only)
from itertools import imap
from future_builtins import map as fmap # Different name to highlight differences

image = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

list(map(None, *image))
# Out: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
list(fmap(None, *image))
# Out: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
list(imap(None, *image))
# Out: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

image2 = [[1, 2, 3],
            [4, 5],
            [7, 8, 9]]
list(map(None, *image2))
# Out: [(1, 4, 7), (2, 5, 8), (3, None, 9)] # Fill missing values with None
list(fmap(None, *image2))
# Out: [(1, 4, 7), (2, 5, 8)] # ignore columns with missing values
list(imap(None, *image2))
# Out: [(1, 4, 7), (2, 5, 8)] # dito

Python 3.x Version ≥ 3.0.0
list(map(None, *image))
    TypeError: 'NoneType' object is not callable

def conv_to_list(*args):
    return list(args)
list(map(conv_to_list, *image))
# Out: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

Section 69.5: Series and Parallel Mapping

Parallel mapping
In this case each argument of the mapping function is pulled from across all iterables (one from each iterable) in
parallel. Thus the number of iterables supplied must match the number of arguments required by the function.


"""

from functools import partial
from operator import mul
from functools import reduce
import pprint

#Section 69.2: Mapping each value in an iterable
print("---Section 69.2: Mapping each value in an iterable------")

print(list(map(abs, (1, -1, 2, -2, 3, -3)))) # the call to `list` is unnecessary in 2.x

#Anonymous function also support for mapping a list:
print(map(lambda x:x*2, [1, 2, 3, 4, 5]))

#or converting decimal values to percentages:
def to_percent(num):
    return num * 100


rate = 0.9 # fictitious exchange rate, 1 dollar = 0.9 euros
dollars = {'under_my_bed': 1000,
            'jeans': 45,
            'bank': 5000}
print(sum(map(partial(mul, rate), dollars.values())))

#Section 69.3: Mapping values of dierent iterables
print("-------Section 69.3: Mapping values of dierent iterables----")

def average(*args):
    return (sum(args)) / len(args) # cast to float - only mandatory for python 2.x
measurement1 = [100, 111, 99, 97]
measurement2 = [102, 117, 91, 102]
measurement3 = [104, 102, 95, 101]
print(list(map(average, measurement1, measurement2, measurement3)))
print((reduce(average,measurement1)))

#Python 3.x Version ≥ 3.0.0
#The mapping stops as soon as one iterable stops:
import operator
measurement1 = [100, 111, 99, 97]
measurement2 = [102, 117]
# Calculate difference between elements
print(list(map(operator.sub, measurement1, measurement2)))
# Out: [-2, -6]
print(list(map(operator.sub, measurement2, measurement1)))
# Out: [2, 6]

#Section 69.4: Transposing with Map: Using "None" as function argument (python 2.x only)
print("------#Section 69.4: Transposing with Map: Using --None-- as function argument (python 2.x only)------")
image = [[1, 2, 3],
            [4, 5,6],
            [7, 8, 9]]

def conv_to_list(*args):
    return list(args)
print(list(map(conv_to_list, *image)))
# Out: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

#print(list(map(None, *image))) --> This will give an error

# Section 69.5: Series and Parallel Mapping
print("-----Section 69.5: Series and Parallel Mapping---")

#Series mapping
insects = ['fly', 'ant', 'beetle', 'cankerworm']
f = lambda x: x + ' is an insect'
print(list(map(f, insects))) # the function defined by f is executed on each item of the iterable
print(list(map(len, insects))) # the len function is executed each item in the insect list

#Parallel mapping
carnivores = ['lion', 'tiger', 'leopard', 'arctic fox']
herbivores = ['african buffalo', 'moose', 'okapi', 'parakeet']
omnivores = ['chicken', 'dove', 'mouse', 'pig']
def animals(w, x, y, z):
    return '{0}, {1}, {2}, and {3} ARE ALL ANIMALS'.format(w.title(), x, y, z)

pprint.pprint(list(map(animals, insects, carnivores, herbivores, omnivores)))