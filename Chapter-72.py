"""
Chapter 72: Sorting, Minimum and Maximum

Section 72.1: Make custom classes orderable
min, max, and sorted all need the objects to be orderable. To be properly orderable, the class needs to define all of
the 6 methods __lt__, __gt__, __ge__, __le__, __ne__ and __eq__:

functools.total_ordering decorator can be used simplifying the effort of writing these rich comparison methods.
If you decorate your class with total_ordering, you need to implement __eq__, __ne__ and only one of the __lt__,
__le__, __ge__ or __gt__, and the decorator will fill in the rest:

Notice how the > (greater than) now ends up calling the less than method, and in some cases even the __eq__
method. This also means that if speed is of great importance, you should implement each rich comparison method
yourself

Section 72.2: Special case: dictionaries

Section 72.3: Using the key argument

Section 72.4: Default Argument to max, min
You can't pass an empty sequence into max or min:
min([])
ValueError: min() arg is an empty sequence

However, with Python 3, you can pass in the keyword argument default with a value that will be returned if the
sequence is empty, instead of raising an exception:

max([], default=42)
# Output: 42
max([], default=0)
# Output: 0

Section 72.5: Getting a sorted sequence

Section 72.6: Extracting N largest or N smallest items from an iterable
To find some number (more than one) of largest or smallest values of an iterable, you can use the nlargest and
nsmallest of the heapq module:

This is much more efficient than sorting the whole iterable and then slicing from the end or beginning. Internally
these functions use the binary heap priority queue data structure, which is very efficient for this use case.

with open(filename) as f:
    longest_lines = heapq.nlargest(1000, f, key=len)

Section 72.7: Getting the minimum or maximum of several values
min(7,2,1,5)
# Output: 1
max(7,2,1,5)
# Output: 7

Section 72.8: Minimum and Maximum of a sequence
min([2, 7, 5])
# Output: 2
sorted([2, 7, 5])[0]
# Output: 2
The maximum is a bit more complicated, because sorted keeps order and max returns the first encountered value.
In case there are no duplicates the maximum is the same as the last element of the sorted return:
max([2, 7, 5])
# Output: 7
sorted([2, 7, 5])[-1]
# Output: 7


"""

#Section 72.2: Special case: dictionaries
print("------Section 72.2: Special case: dictionaries---------")
#Getting the minimum or maximum or using sorted depends on iterations over the object. In the case of dict, the
#iteration is only over the keys:
adict = {'a': 3, 'b': 5, 'c': 1}
print(min(adict))
# Output: 'a'
print(max(adict))
# Output: 'c'
print(sorted(adict))
# Output: ['a', 'b', 'c']

#To keep the dictionary structure, you have to iterate over the .items():
print(min(adict.items()))
# Output: ('a', 3)
print(max(adict.items()))
# Output: ('c', 1)
print(sorted(adict.items()))
# Output: [('a', 3), ('b', 5), ('c', 1)]

#For sorted, you could create an OrderedDict to keep the sorting while having a dict-like structure:

from collections import OrderedDict
import operator
print(OrderedDict(sorted(adict.items())))
# Output: OrderedDict([('a', 3), ('b', 5), ('c', 1)])
res = OrderedDict(sorted(adict.items()))
print(res['a'])
# Output: 3

#By value
#Again this is possible using the key argument:

print(min(adict.items(), key=lambda x: x[1]))
# Output: ('c', 1)
print(max(adict.items(), key=lambda x: x[1]))
print(max(adict.items(), key=operator.itemgetter(1)))
# Output: ('b', 5)
print(sorted(adict.items(), key=operator.itemgetter(1), reverse=True))
# Output: [('b', 5), ('a', 3), ('c', 1)]

#Section 72.3: Using the key argument
list_of_tuples = [(0, 10), (1, 15), (2, 8)]
print(min(list_of_tuples))
# Output: (0, 10)

#but if you want to sort by a specific element in each sequence use the key-argument:
print(min(list_of_tuples, key=lambda x: x[0]))  # Sorting by first element
# Output: (0, 10)
print(sorted(list_of_tuples, key=lambda x: x[0]))  # Sorting by first element (increasing)

# The operator module contains efficient alternatives to the lambda function
print(max(list_of_tuples, key=operator.itemgetter(0))) # Sorting by first element

#Section 72.4: Default Argument to max, min

#Section 72.5: Getting a sorted sequence
print(sorted((7, 2, 1, 5))) # tuple
# Output: [1, 2, 5, 7]
print(sorted(['c', 'A', 'b']))# list
# Output: ['A', 'b', 'c']
print(sorted({11, 8, 1})) # set
# Output: [1, 8, 11]
print(sorted({'11': 5, '3': 2, '10': 15})) # dict
# Output: ['10', '11', '3'] # only iterates over the keys
print(sorted('bdca')) # string
# Output: ['a','b','c','d']
#The result is always a new list; the original data remains unchanged

#Section 72.6: Extracting N largest or N smallest items from an iterable

import heapq

print(heapq.nlargest(5, range(10)))
# Output: [9, 8, 7, 6, 5]
print(heapq.nsmallest(5, range(10)))
# Output: [0, 1, 2, 3, 4]

