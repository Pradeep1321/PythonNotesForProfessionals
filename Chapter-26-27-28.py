'''
Chapter 26: Filter
Parameter           Details
function            callable that determines the condition or None then use the identity function for filtering (positionalonly)
iterable            iterable that will be filtered (positional-only)

Section 26.1: Basic use of filter
To filter discards elements of a sequence based on some criteria:

Section 26.2: Filter without function
If the function parameter is None, then the identity function will be used:

Section 26.3: Filter as short-circuit check
filter (python 3.x) and ifilter (python 2.x) return a generator so they can be very handy when creating a shortcircuit
test like or or and:
Python 2.x Version ≥ 2.0.1
# not recommended in real use but keeps the example short:
from itertools import ifilter as filter
Python 2.x Version ≥ 2.6.1
from future_builtins import filter

Section 26.4: Complementary function: filterfalse, ifilterfalse
There is a complementary function for filter in the itertools-module
Python 2.x Version ≥ 2.0.1
# not recommended in real use but keeps the example valid for python 2.x and python 3.x
from itertools import ifilterfalse as filterfalse
Python 3.x Version ≥ 3.0.0
from itertools import filterfalse
which works exactly like the generator filter but keeps only the elements that are False:

Chapter 27: Heapq
Section 27.1: Largest and smallest items in a collection
To find the largest items in a collection, heapq module has a function called nlargest, we pass it two arguments, the
first one is the number of items that we want to retrieve, the second one is the collection name:

Section 27.2: Smallest item in a collection
The most interesting property of a heap is that its smallest element is always the first element: heap[0]

Chapter 28: Tuple
tuple is an immutable list of values. Tuples are one of Python's simplest and most common collection types, and
can be created with the comma operator (value = 1, 2, 3).
To create a singleton tuple it is necessary to have a trailing comma.Also, no white
space after the trailing comma
t2 = ('a',)

Another way to create a tuple is the built-in function tuple.
t = tuple('lupins')

Section 28.2: Tuples are immutable
One of the main differences between lists and tuples in Python is that tuples are immutable, that is, one cannot
add or modify items once the tuple is initialized
Similarly, tuples don't have .append and .extend methods as list does. Using += is possible, but it changes the
binding of the variable, and not the tuple itself:

Be careful when placing mutable objects, such as lists, inside tuples. This may lead to very confusing outcomes
when changing them.

Section 28.3: Packing and Unpacking Tuples
The assignment a = 1, 2, 3 is also called packing because it packs values together in a tuple.
Note that a one-value tuple is also a tuple. To tell Python that a variable is a tuple and not a single value you can use
a trailing comma

Section 28.4: Built-in Tuple Functions

Comparison
If elements are of the same type, python performs the comparison and returns the result. If elements are different
types, it checks whether they are numbers.
If numbers, perform comparison.
If either element is a number, then the other element is returned.
Otherwise, types are sorted alphabetically .
If we reached the end of one of the lists, the longer list is "larger." If both list are same it returns 0.

Max of a tuple
The function max returns item from the tuple with the max value

Min of a tuple
The function min returns the item from the tuple with the min value

Convert a list into tuple
The built-in function tuple converts a list into a tuple.

Tuple concatenation
Use + to concatenate two tuples


Section 28.5: Tuple Are Element-wise Hashable and Equatable

Section 28.6: Indexing Tuples

Section 28.7: Reversing Elements
 using reversed (reversed gives an iterable which is converted to a tuple):



'''

import itertools
import heapq

#Section 26.1: Basic use of filter
names = ['Fred', 'Wilma', 'Barney']
def long_name(name):
    return len(name) > 5

print(list(filter(long_name, names)))

# () is used as generator and the object can be used as next to get the next item or we can use [] list to get all the items.
# if we use list then lot of memory is used at once to hold the list so always better to use generators to load big data
(name for name in names if len(name) > 5) # equivalent generator expression
# Out: <generator object <genexpr> at 0x000001C6F49BF4C0>

print(list(filter(None, [1, 0, 2, [], '', 'a']))) # discards 0, [] and ''

#Section 26.3: Filter as short-circuit check
#The next-function gives the next (in this case first) element of and is therefore the reason why it's short-circuit.
car_shop = [('Toyota', 1000), ('rectangular tire', 80), ('Porsche', 5000)]
def find_something_smaller_than(name_value_tuple):
    print('Check {0}, {1}$'.format(*name_value_tuple))
    return (name_value_tuple[1] < 100)
print(next(filter(find_something_smaller_than, car_shop)))

# HeapQ
numbers = [1, 4, 2, 100, 20, 50, 32, 200, 150, 8]
print(heapq.nlargest(4, numbers)) # [200, 150, 100, 50]
print(heapq.nsmallest(4, numbers)) # [1, 2, 4, 8]
people = [
            {'firstname': 'John', 'lastname': 'Doe', 'age': 30},
            {'firstname': 'Jane', 'lastname': 'Doe', 'age': 25},
            {'firstname': 'Janie', 'lastname': 'Doe', 'age': 10},
            {'firstname': 'Jane', 'lastname': 'Roe', 'age': 22},
            {'firstname': 'Johnny', 'lastname': 'Doe', 'age': 12},
            {'firstname': 'John', 'lastname': 'Roe', 'age': 45}
        ]
oldest = heapq.nlargest(2, people, key=lambda s: s['age'])
print(oldest)

youngest = heapq.nsmallest(2, people, key=lambda s: s['age'])
print(youngest)

numbers = [10, 4, 2, 100, 20, 50, 32, 200, 150, 8]
heapq.heapify(numbers)
print(numbers)
heapq.heappop(numbers) # 2
print(numbers)

#Tuple

#Section 28.3: Packing and Unpacking Tuples
a = 1 # a is the value 1
a = 1, # a is the tuple (1,)

#A comma is needed also if you use parentheses
a = (1,) # a is the tuple (1,)
a = (1) # a is the value 1 and not a tuple

#To unpack values from a tuple and do multiple assignments use
# unpacking AKA multiple assignment
x, y, z = (1, 2, 3)

#The symbol _ can be used as a disposable variable name if one only needs some elements of a tuple, acting as a placeholder:
a = 1, 2, 3, 4
_, x, y, _ = a

#Python 3.x Version ≥ 3.0
first, *more, last = (1, 2, 3, 4, 5)
print(first,last,more)