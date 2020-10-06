''''

Chapter 32: Iterables and Iterators
Section 32.1: Iterator vs Iterable vs Generator
An iterable is an object that can return an iterator. Any object with state that has an __iter__ method and returns
an iterator is an iterable. It may also be an object without state that implements a __getitem__ method. - The
method can take indices (starting from zero) and raise an IndexError when the indices are no longer valid.
Python's str class is an example of a __getitem__ iterable.
An Iterator is an object that produces the next value in a sequence when you call next(*object*) on some object.
Moreover, any object with a __next__ method is an iterator. An iterator raises StopIteration after exhausting the
iterator and cannot be re-used at this point.

Iterable classes:
Iterable classes define an __iter__ and a __next__ method

Generators are simple ways to create iterators. A generator is an iterator and an iterator is an iterable

Section 32.2: Extract values one by one
Start with iter() built-in to get iterator over iterable and use next() to get elements one by one until
StopIteration is raised signifying the end:
s = {1, 2} # or list or generator or even iterator
i = iter(s) # get iterator
a = next(i) # a = 1
b = next(i) # b = 2
c = next(i) # raises StopIteration

Section 32.3: Iterating over entire iterable
s = {1, 2, 3}
# get every element in s
for a in s:
print a # prints 1, then 2, then 3
# copy into list
l1 = list(s) # l1 = [1, 2, 3]

Section 32.4: Verify only one element in iterable
Use unpacking to extract the first element and ensure it's the only one
a, = iterable
def foo():
yield 1
a, = foo() # a = 1
nums = [1, 2, 3]
a, = nums # ValueError: too many values to unpack

Section 32.5: What can be iterable
Iterable can be anything for which items are received one by one, forward only. Built-in Python collections are
iterable:
[1, 2, 3] # list, iterate over items
(1, 2, 3) # tuple
{1, 2, 3} # set
{1: 2, 3: 4} # dict, iterate over keys
Generators return iterables:

Section 32.6: Iterator isn't reentrant!




'''