"""
Chapter 53: Itertools Module
Section 53.1: Combinations method in Itertools Module

itertools.combinations will return a generator of the k-combination sequence of a list.

Section 53.2: itertools.dropwhile
itertools.dropwhile enables you to take items from a sequence after a condition first becomes False.

Section 53.3: Zipping two iterators until they are both exhausted
Similar to the built-in function zip(), itertools.zip_longest will continue iterating beyond the end of the shorter
of two iterables.

In Python 2.6 and 2.7, this function is called itertools.izip_longest

Section 53.4: Take a slice of a generator
Itertools "islice" allows you to slice a generator

Note that like a regular slice, you can also use start, stop and step arguments
itertools.islice(iterable, 1, 30, 3)


Section 53.5: Grouping items from an iterable object using a function

Only groups of consecutive elements are grouped. You may need to sort by the same key before calling groupby

Section 53.6: itertools.takewhile
itertools.takewhile enables you to take items from a sequence until a condition first becomes False

Section 53.7: itertools.permutations
itertools.permutations returns a generator with successive r-length permutations of elements in the iterable.

Section 53.8: itertools.repeat

Section 53.9: Get an accumulated sum of numbers in an iterable
Python 3.x Version ≥ 3.2
accumulate yields a cumulative sum (or product) of numbers.

Section 53.10: Cycle through elements in an iterator
cycle is an infinite iterator.
itertools.cycle('ABCD')
A B C D A B C D A B C D ...

Therefore, take care to give boundaries when using this to avoid an infinite loop.

Section 53.11: itertools.product
This function lets you iterate over the Cartesian product of a list of iterables


Section 53.12: itertools.count
This simple function generates infinite series of numbers. For example

Section 53.13: Chaining multiple iterators together
Use itertools.chain to create a single generator which will yield the values from several generators in sequence

While chain can take an arbitrary number of arguments, chain.from_iterable is the only way to chain an infinite
number of iterables.

"""
import itertools
from itertools import zip_longest
import operator

#Section 53.1: Combinations method in Itertools Module
print("------Section 53.1: Combinations method in Itertools Module-----")
a = [1,2,3,4,5]
b = list(itertools.combinations(a, 2))
print(b)
c = list(itertools.combinations(a, 3))
print(c)

#Section 53.2: itertools.dropwhile
print("-----Section 53.2: itertools.dropwhile-----------")
def is_even(x):
    return x % 2 == 0

lst = [0, 2, 4, 12, 18, 13, 14, 22, 23, 44]
result = list(itertools.dropwhile(is_even, lst))
print(result)
#(This example is same as the example for takewhile but using dropwhile.)

#Section 53.3: Zipping two iterators until they are both exhausted
print("-------Section 53.3: Zipping two iterators until they are both exhausted--------")
a = [i for i in range(5)] # Length is 5
b = ['a', 'b', 'c', 'd', 'e', 'f', 'g'] # Length is 7
for i in zip_longest(a, b):
    x, y = i # Note that zip longest returns the values as a tuple
    print(x, y)
#An optional fillvalue argument can be passed (defaults to '') like so:
for i in zip_longest(a, b, fillvalue='Hogwash!'):
    x, y = i # Note that zip longest returns the values as a tuple
    print(x, y)

#Section 53.4: Take a slice of a generator
print("--------Section 53.4: Take a slice of a generator----------")

#results = fetch_paged_results() # returns a generator
#limit = 20 # Only want the first 20 results
#for data in itertools.islice(results, limit):
#    print(data)

#Normally you cannot slice a generator:, however u can itertools to slice generator
def gen():
    n = 0
    while n < 20:
        n += 1
        yield n
for part in itertools.islice(gen(), 3):
    print(part)

#Section 53.5: Grouping items from an iterable object using a function
print("---------Section 53.5: Grouping items from an iterable object using a function-------")

lst = [("a", 5, 6), ("b", 2, 4), ("a", 2, 5), ("c", 2, 6)]

#Generate the grouped generator, grouping by the second element in each tuple:
def testGroupBy(lst):
    groups = itertools.groupby(lst, key=lambda x: x[1])
    for key, group in groups:
        print(key, list(group))
testGroupBy(lst)

#Only groups of consecutive elements are grouped. You may need to sort by the same key before calling groupby

lst = [("a", 5, 6), ("b", 2, 4), ("a", 2, 5), ("c", 5, 6)]
testGroupBy(lst)

#To correctly do sorting, create a list from the iterator before sorting

groups = itertools.groupby(lst, key=lambda x: x[1])
for key, group in sorted((key, list(group)) for key, group in groups):
    print(key, list(group))

#Section 53.6: itertools.takewhile
print("------Section 53.6: itertools.takewhile-----------")

def is_even(x):
    return x % 2 == 0
lst = [0, 2, 4, 12, 18, 13, 14, 22, 23, 44]
result = list(itertools.takewhile(is_even, lst))
print(result)

#Note that, the first number that violates the predicate (i.e.: the function returning a Boolean value) is_even is, 13.
#Once takewhile encounters a value that produces False for the given predicate, it breaks out.

#Section 53.7: itertools.permutations
print("-------Section 53.7: itertools.permutations------------")
a = [1,2,3]
print(list(itertools.permutations(a)))
print(list(itertools.permutations(a, 2)))

#if the list a has duplicate elements, the resulting permutations will have duplicate elements, you can use set to get
#unique permutations:
a = [1,2,1]
print(list(itertools.permutations(a)))
# to remove duplicate
print(set(itertools.permutations(a)))

#Section 53.8: itertools.repeat
print("----------Section 53.8: itertools.repeat---------")
for i in itertools.repeat('over-and-over', 3):
    print(i)

#Section 53.9: Get an accumulated sum of numbers in an iterable
print("---------Section 53.9: Get an accumulated sum of numbers in an iterable---------------")
print(list(itertools.accumulate([1,2,3,4,5])))
print(list(itertools.accumulate([1,2,3,4,5], func=operator.mul)))

#Section 53.10: Cycle through elements in an iterator
print("-------Section 53.10: Cycle through elements in an iterator-----------")
#Iterate over each element in cycle for a fixed range
cycle_iterator = itertools.cycle('abc123')
print([next(cycle_iterator) for i in range(0, 10)])

#Section 53.11: itertools.product
print("----Section 53.11: itertools.product-----------")
for x, y in itertools.product(range(10), range(10)):
    print(x, y)

#Like all python functions that accept a variable number of arguments, we can pass a list to itertools.product for
#unpacking, with the * operator
its = [range(10)] * 2
for x,y in itertools.product(*its):
    print(x, y)
a=[1,2,3,4]
b=['a','b','c']
print(itertools.product(a,b))
for i in itertools.product(a,b):
    print(i)

#Section 53.12: itertools.count
print("------Section 53.12: itertools.count-----------")
for number in itertools.count():
    if number > 20:
        break
    print(number)

#count() takes two arguments, start and step:
for number in itertools.count(start=10, step=4):
    print(number)
    if number > 20:
        break
#Section 53.13: Chaining multiple iterators together
print("------Section 53.13: Chaining multiple iterators together------------")
a = (x for x in ['1', '2', '3', '4'])
b = (x for x in ['x', 'y', 'z'])
print(' '.join(itertools.chain(a, b)))
# or
print("from_iterable")
print(' '.join(itertools.chain.from_iterable([a,b])))

