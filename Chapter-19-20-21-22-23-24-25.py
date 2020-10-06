'''
Chapter 19: Dictionary:
Parameter           Details
key                 The desired key to lookup
value               The value to set or return

Section 19.1: Introduction to Dictionary
A dictionary is an example of a key value store also known as Mapping in Python

creating a dict
Dictionaries can be initiated in many ways:
literal syntax
    d = {} # empty dict
    d = {'key': 'value'} # dict with initial values
Python 3.x Version ≥ 3.5
# Also unpacking one or multiple dictionaries with the literal syntax is possible
# makes a shallow copy of otherdict
    d = {**otherdict}
# also updates the shallow copy with the contents of the yetanotherdict.
    d = {**otherdict, **yetanotherdict}

dict comprehension
    d = {k:v for k,v in [('key', 'value',)]}

built-in class: dict()
d = dict() # empty dict
d = dict(key='value') # explicit keyword arguments
d = dict([('key', 'value')]) # passing in a list of key/value pairs
# make a shallow copy of another dict (only possible if keys are only strings!)
d = dict(**otherdict)

It also possible to add list and dictionary as value:
    d['new_list'] = [1, 2, 3]
    d['new_dict'] = {'nested_dict': 1}
To delete an item, delete the key from the dictionary:
    del d['newkey']

Section 19.2: Avoiding KeyError Exceptions:
One way to avoid key errors is to use the dict.get method, which allows you to specify a default value to return in
the case of an absent key.
    value = mydict.get(key, default_value)
to add the key if key is not present:
    mydict.setdefault(key, default_value)

An alternative way to deal with the problem is catching the exception
try:
    value = mydict[key]
except KeyError:
    value = default_value

Section 20.1: List methods and supported operators
1. append(value) – appends a new element to the end of the list.
2. extend(enumerable) – extends the list by appending elements from another enumerable
Lists can also be concatenated with the + operator. Note that this does not modify any of the original lists:
3. index(value, [startIndex]) – gets the index of the first occurrence of the input value. If the input value is
not in the list a ValueError exception is raised. If a second argument is provided, the search is started at that
specified index.
4. insert(index, value) – inserts value just before the specified index. Thus after the insertion the new
element occupies position index.
5. pop([index]) – removes and returns the item at index. With no argument it removes and returns the last
element of the list.
6. remove(value) – removes the first occurrence of the specified value. If the provided value cannot be found, a
ValueError is raised.
7. reverse() – reverses the list in-place and returns None.
8. count(value) – counts the number of occurrences of some value in the list.
9. sort() – sorts the list in numerical and lexicographical order and returns None.

Better way to sort using attrgetter and itemgetter

10. clear() – removes all items from the list

11. Replication – multiplying an existing list by an integer will produce a larger list consisting of that many copies
of the original. This can be useful for example for list initialization
b = ["blah"] * 3
# b = ["blah", "blah", "blah"]

12. Element deletion – it is possible to delete multiple elements in the list using the del keyword and slice
notation:

13. Copying
The default assignment "=" assigns a reference of the original list to the new name. That is, the original name
and new name are both pointing to the same list object. Changes made through any of them will be reflected
in another. This is often not what you intended.

import copy
new_list = copy.copy(old_list) #inserts references to the objects found in the original.
This is a little slower than list() because it has to find out the datatype of old_list first.
If the list contains objects and you want to copy them as well, use generic copy.deepcopy():

Section 20.2: Accessing list values
Attempting to access an index outside the bounds of the list will raise an IndexError.
Negative indices are interpreted as counting from the end of the list.
    lst[start:end:step]

Advanced slicing:
When lists are sliced the __getitem__() method of the list object is called, with a slice object. Python has a builtin
slice method to generate slice objects

Section 20.3: Checking if list is empty
The emptiness of a list is associated to the boolean False, so you don't have to check len(lst) == 0, but just lst
or not lst

Section 20.4: Iterating over a list

Section 20.5: Checking whether an item is in a list

Section 20.5: Checking whether an item is in a list
'test' in lst
Note: the in operator on sets is asymptotically faster than on lists. If you need to use it many times on
potentially large lists, you may want to convert your list to a set, and test the presence of elements on
the set.

Section 20.6: Any and All
You can use all() to determine if all the values in an iterable evaluate to True
Likewise, any() determines if one or more values in an iterable evaluate to True


Section 20.7: Reversing list elements
You can use the reversed function which returns an iterator to the reversed list:

Section 20.8: Concatenate and Merge lists
merged = list1 + list2
For padding lists of unequal length to the longest one with Nones use itertools.zip_longest
(itertools.izip_longest in Python 2)
alist = ['a1', 'a2', 'a3']
blist = ['b1']
clist = ['c1', 'c2', 'c3', 'c4']
for a,b,c in itertools.zip_longest(alist, blist, clist):
    print(a, b, c)
# Output:
# a1 b1 c1
# a2 None c2
# a3 None c3
# None None c4

3. Insert to a specific index values:
alist.insert(index, [value])

Section 20.9: Length of a list
Use len() to get the one-dimensional length of a list.
len() also works on strings, dictionaries, and other data structures similar to lists.
Also note that the cost of len() is O(1), meaning it will take the same amount of time to get the length of a list
regardless of its length.

Section 20.10: Remove duplicate values in list
Removing duplicate values in a list can be done by converting the list to a set (that is an unordered collection of
distinct objects). If a list data structure is needed, then the set can be converted back to a list using the function
list():

To preserve the order of the list one can use an OrderedDict
import collections
>>> collections.OrderedDict.fromkeys(names).keys()

Section 20.11: Comparison of lists
It's possible to compare lists and other sequences lexicographically using comparison operators. Both operands
must be of the same type

If one of the lists is contained at the start of the other, the shortest list wins.

[1, 10] < [1, 10, 100]
# True

Section 20.12: Accessing values in nested list

Section 20.13: Initializing a List to a Fixed Number of Elements

Chapter 21: List comprehensions
List comprehensions in Python are concise, syntactic constructs

Section 21.1: List Comprehensions
A list comprehension creates a new list by applying an expression to each element of an iterable. The most basic
form is:
[ <expression> for <element> in <iterable> if <condition> ]

Generator expressions are evaluated lazily, but list comprehensions
evaluate the entire iterator immediately - consuming memory proportional to the iterator's length.

# Organize letters in words more reasonably - in an alphabetical order
sentence = "Beautiful is better than ugly"
["".join(sorted(word, key = lambda x: x.lower())) for word in sentence.split()]
# ['aBefiltuu', 'is', 'beertt', 'ahnt', 'gluy']

Double Iteration
Order of double iteration [... for x in ... for y in ...] is either natural or counter-intuitive. The rule of
thumb is to follow an equivalent for loop:
[str(x) for i in range(3) for x in foo(i)]

In-place Mutation and Other Side Effects

In-place Mutation and Other Side Effects
list.sort() sorts a list in-place (meaning that it modifies the original list) and returns the value None. Therefore, it
won't work as expected in a list comprehension:
[x.sort() for x in [[2, 1], [4, 3], [0, 1]]]
# [None, None, None]
Instead, sorted() returns a sorted list rather than sorting in-place:
[sorted(x) for x in [[2, 1], [4, 3], [0, 1]]]
# [[1, 2], [3, 4], [0, 1]]

Section 21.2: Conditional List Comprehensions
list comprehension of the form [e for x in y if c] (where e and c are expressions in terms of
x) is equivalent to list(filter(lambda x: c, map(lambda x: e, y))).
Despite providing the same result, pay attention to the fact that the former example is almost 2x faster than the
latter one.
... if ... else ... conditional expression (sometimes known as a ternary expression)

One can combine ternary expressions and if conditions. The ternary operator works on the filtered result:
[x if x > 2 else '*' for x in range(10) if x % 2 == 0]
# Out: ['*', '*', 4, 6, 8]
The same couldn't have been achieved just by ternary operator only:
[x if (x > 2 and x % 2 == 0) else '*' for x in range(10)]
# Out:['*', '*', '*', '*', 4, '*', 6, '*', 8, '*']
See also: Filters, which often provide a sufficient alternative to conditional list comprehensions

NOTE: The main difference above is after the for loop if there is if clause the filtered data is returned and hence u
 will have only few items, however if there is no filter, every data is returned and then u r trying to filter.

 Section 21.3: Avoid repetitive and expensive operations using conditional clause

 separate generator function is recommended over a complex one-liner
 Another way to prevent computing f(x) multiple times is to use the @functools.lru_cache()(Python 3.2+)
decorator on f(x)
The list comprehension just generates one list, once, and copies each item over (from its original place of residence
to the result list) also exactly once.

Section 21.4: Dictionary Comprehensions
If your dictionary is large, consider importing itertools and utilize izip or imap.

Merging Dictionaries
Merging Dictionaries
Combine dictionaries and optionally override old values with a nested dictionary comprehension.
dict1 = {'w': 1, 'x': 1}
dict2 = {'x': 2, 'y': 2, 'z': 2}
{k: v for d in [dict1, dict2] for k, v in d.items()}
# Out: {'w': 1, 'x': 2, 'y': 2, 'z': 2}
However, dictionary unpacking (PEP 448) may be a preferred.
Python 3.x Version ≥ 3.5
{**dict1, **dict2}
# Out: {'w': 1, 'x': 2, 'y': 2, 'z': 2}
Note: dictionary comprehensions were added in Python 3.0 and backported to 2.7+, unlike list comprehensions,
which were added in 2.0. Versions < 2.7 can use generator expressions and the dict() builtin to simulate the
behavior of dictionary comprehensions.

Section 21.5: List Comprehensions with Nested Loops

[ expression for target1 in iterable1 [if condition1]
        for target2 in iterable2 [if condition2]...
        for targetN in iterableN [if conditionN] ]

Section 21.6: Generator Expressions
Generator expressions are very similar to list comprehensions. The main difference is that it does not create a full
set of results at once; it creates a generator object which can then be iterated over.

These are two very different objects:
the list comprehension returns a list object whereas the generator comprehension returns a generator.
generator objects cannot be indexed and makes use of the next function to get items in order.

Note: We use xrange since it too creates a generator object. If we would use range, a list would be created. Also,
xrange exists only in later version of python 2. In python 3, range just returns a generator.

Python 2.x Version ≥ 2.4
g = (x**2 for x in xrange(10))
print(g.next())

Python 3.x Version ≥ 3.0
NOTE: The function g.next() should be substituted by next(g) and xrange with range since
Iterator.next() and xrange() do not exist in Python 3.

Use cases
Generator expressions are lazily evaluated, which means that they generate and return each value only when the
generator is iterated. This is often useful when iterating through large datasets, avoiding the need to create a
duplicate of the dataset in memory:

Section 21.7: Set Comprehensions
Set comprehension is similar to list and dictionary comprehension, but it produces a set, which is an unordered
collection of unique elements.

Note: Set comprehension is available since python 2.7+, unlike list comprehensions, which were added in 2.0. In
Python 2.2 to Python 2.6, the set() function can be used with a generator expression to produce the same result:

Section 21.8: Refactoring filter and map to list comprehensions
The filter or map functions should often be replaced by list comprehensions

filter(P, S) is almost always written clearer as [x for x in S if P(x)], and this has the huge
advantage that the most common usages involve predicates that are comparisons, e.g. x==42, and
defining a lambda for that just requires much more effort for the reader (plus the lambda is slower than
the list comprehension). Even more so for map(F, S) which becomes [F(x) for x in S]. Of course, in
many cases you'd be able to use generator expressions instead.

Refactoring - Quick Reference
Map
map(F, S) == [F(x) for x in S]
Filter
filter(P, S) == [x for x in S if P(x)]
where F and P are functions which respectively transform input values and return a bool

Section 21.9: Comprehensions involving tuples

Section 21.10: Counting Occurrences Using Comprehension
# Count the numbers in `range(1000)` that are even and contain the digit `9`:
print (sum(
1 for x in range(1000)
if x % 2 == 0 and
'9' in str(x)
))
# Out: 95
Note: Here we are not collecting the 1s in a list (note the absence of square brackets), but we are passing the ones
directly to the sum function that is summing them up. This is called a generator expression, which is similar to a
Comprehension.


Section 21.11: Changing Types in a List
# Convert a list of strings to integers.
items = ["1","2","3","4"]
[int(item) for item in items]
# Out: [1, 2, 3, 4]
# Convert a list of strings to float.
items = ["1","2","3","4"]
map(float, items)
# Out:[1.0, 2.0, 3.0, 4.0]

Section 21.12: Nested List Comprehensions

Section 21.13: Iterate two or more list simultaneously within list comprehension
For iterating more than two lists simultaneously within list comprehension, one may use zip() as:
>>> [(i, j, k) for i, j, k in zip(list_1, list_2, list_3)]


Chapter 22: List slicing (selecting parts of lists)

Section 22.1: Using the third "step" argument
lst[::2]

Section 22.2: Selecting a sublist from a list
lst[2:4]
Section 22.3: Reversing a list with slicing
b = a[::-1]

Section 22.4: Shifting a list using slicing


Chapter 23: groupby()
Parameter               Details
iterable                Any python iterable
key                     Function(criteria) on which to group the iterable

In Python, the itertools.groupby() method allows developers to group values of an iterable class based on a
specified property into another iterable set of values.

Section 23.1: Example 4

Section 23.2: Example 2

Section 23.3: Example 3

groupby :  group consecutive items together that are of the same occurence and hence we have to sort the items before
using gropby to get the proper values if not, the items that are not consecutive will be missed as shown in the below example3


Chapter 24: Linked lists
A linked list is a collection of nodes, each made up of a reference and a value. Nodes are strung together into a
sequence using their references. Linked lists can be used to implement more complex data structures like lists,
stacks, queues, and associative arrays.

Section 24.1: Single linked list example

Chapter 25: Linked List Node


'''


import itertools
import datetime
from operator import itemgetter,attrgetter


options = {
"x": ["a", "b"],
"y": [10, 20, 30]}
keys = options.keys()
values = (options[key] for key in keys)
combinations = [dict(zip(keys, combination)) for combination in itertools.product(*values)]
print (combinations)

class Person(object):
    def __init__(self, name, birthday, height):
        self.name = name
        self.birthday = birthday
        self.height = height
    def __repr__(self):
        return self.name


persons= [Person("John Cena", datetime.date(1992, 9, 12), 175),
Person("Chuck Norris", datetime.date(1990, 8, 28), 180),
Person("Jon Skeet", datetime.date(1991, 7, 6), 185)]

#persons=sort(key=lambda item: item.name)
by_age = itemgetter('age')
by_salary = itemgetter('salary')

person = [Person("John Cena", datetime.date(1992, 9, 12), 175),
            Person("Chuck Norris", datetime.date(1990, 8, 28), 180),
            Person("Jon Skeet", datetime.date(1991, 7, 6), 185)]

person.sort(key=attrgetter('name')) #sort by name
by_birthday = attrgetter('birthday')
person.sort(key=by_birthday) #sort by birthday

nums = [1, 1, 0, 1]
print(all(nums))
# False
chars = ['a', 'b', 'c', 'd']
print(all(chars))
# True

# concatination

alist = ['a1', 'a2', 'a3']
blist = ['b1']
clist = ['c1', 'c2', 'c3', 'c4']
for a,b,c in itertools.zip_longest(alist, blist, clist):
    print(a, b, c)

#Instead, to initialize the list with a fixed number of different mutable objects, use:
my_list=[{1} for _ in range(10)]
print(my_list)

things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "harley"), \
("vehicle", "speed boat"), ("vehicle", "school bus")]
dic = {}
f = lambda x: x[0]
for key, grp in itertools.groupby(sorted(things, key=f), f):
    dic[key] = list(grp)
print(dic)

c = itertools.groupby(['goat', 'dog', 'cow', 1, 1, 2, 3, 11, 10, ('persons', 'man', 'woman')])
dic = {}
for k, v in c:
    dic[k] = list(v)
print(dic)

#non consecutive items that will be missed in group by if sorted is not used.
list_things = ['goat', 'dog', 'donkey', 'mulato', 'cow', 'cat', ('persons', 'man', 'woman'), \
'wombat', 'mongoose', 'malloo', 'camel']
c = itertools.groupby(list_things, key=lambda x: x[0])
dic = {}
for k, v in c:
    dic[k] = list(v)
print(dic)

# groupby working fine when sorted is used

list_things = ['goat', 'dog', 'donkey', 'mulato', 'cow', 'cat', ('persons', 'man', 'woman'), \
'wombat', 'mongoose', 'malloo', 'camel']
sorted_list = sorted(list_things, key = lambda x: x[0])
c = itertools.groupby(sorted_list, key=lambda x: x[0])
dic = {}
for k, v in c:
    dic[k] = list(v)
print(dic)

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, val):
        self.data = val
    def setNext(self, val):
        self.next = val

class LinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        """Check if the list is empty"""
        return self.head is None
    def add(self, item):
        """Add the item to the list"""
        new_node = Node(item)
        new_node.setNext(self.head)
        self.head = new_node
    def size(self):
        """Return the length/size of the list"""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.getNext()
        return count
    def search(self, item):
            """Search for item in list. If found, return True. If not found, return False"""
            current = self.head
            found = False
            while current is not None and not found:
                if current.getData() is item:
                    found = True
                else:
                    current = current.getNext()
            return found

    def remove(self, item):
                """Remove item from list. If item is not found in list, raise ValueError"""

                current = self.head
                previous = None
                found = False
                while current is not None and not found:
                    if current.getData() is item:
                        found = True
                    else:
                        previous = current
                        current = current.getNext()
                if found:
                    if previous is None:
                        self.head = current.getNext()
                    else:
                        previous.setNext(current.getNext())
                else:
                    raise ValueError
                    print('Value not found.')

    def insert(self, position, item):
            """
                Insert item at position specified. If position specified is
                out of bounds, raise IndexError
            """

            if position > self.size() - 1:
                raise IndexError
                print("Index out of bounds.")
            current = self.head
            previous = None
            pos = 0
            if position is 0:
                self.add(item)
            else:
                new_node = Node(item)
                while pos < position:
                    pos += 1
                    previous = current
                    current = current.getNext()
                previous.setNext(new_node)
                new_node.setNext(current)
    def index(self, item):
        """
            Return the index where item is found.
            If item is not found, return None.
        """
        current = self.head
        pos = 0
        found = False
        while current is not None and not found:
            if current.getData() is item:
                found = True
            else:
                current = current.getNext()
                pos += 1
        if found:
            pass
        else:
            pos = None
        return pos

    def pop(self, position = None):
        """
        If no argument is provided, return and remove the item at the head.
        If position is provided, return and remove the item at that position.
        If index is out of bounds, raise IndexError
        """
        if position > self.size():
            print('Index out of bounds')
            raise IndexError
        current = self.head
        if position is None:
            ret = current.getData()
            self.head = current.getNext()
        else:
            pos = 0
            previous = None
            while pos < position:
                previous = current
                current = current.getNext()
                pos += 1
                ret = current.getData()
            previous.setNext(current.getNext())
        print (ret)
        return ret

    def append(self, item):
        """Append item to the end of the list"""
        current = self.head
        previous = None
        pos = 0
        length = self.size()
        while pos < length:
            previous = current
            current = current.getNext()
            pos += 1
        new_node = Node(item)
        if previous is None:
            new_node.setNext(current)
            self.head = new_node
        else:
            previous.setNext(new_node)

    def printList(self):
        """Print the list"""
        current = self.head
        while current is not None:
            print(current.getData())
            current = current.getNext()

ll = LinkedList()
ll.add('l')
ll.add('H')
ll.insert(1,'e')
ll.append('l')
ll.append('o')
ll.printList()
