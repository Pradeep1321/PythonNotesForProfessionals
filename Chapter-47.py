''''
Chapter 47: Collections module
The built-in collections package provides several specialized, flexible collection types that are both highperformance
and provide alternatives to the general collection types of dict, list, tuple and set.

Counter is a dict sub class that allows you to easily count objects. It has utility methods for working with the
frequencies of the objects that you are counting.


Section 47.2: collections.OrderedDict

The order of keys in Python dictionaries is arbitrary: they are not governed by the order in which you add them
The collections.OrderedDict class provides dictionary objects that retain the order of keys. OrderedDicts can be
created as shown below with a series of ordered items

Section 47.3: collections.defaultdict
collections.defaultdict(default_factory) returns a subclass of dict that has a default value for missing keys
it defaults to None

A typical usage of defaultdict is to use one of the builtin types such as str, int, list or dict as the
default_factory, since these return empty types when called with no arguments:

Section 47.4: collections.namedtuple

Section 47.5: collections.deque
Returns a new deque object initialized left-to-right (using append()) with data from iterable. If iterable is not
specified, the new deque is empty.

Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended
queue”). Deques support thread-safe, memory efficient appends and pops from either side of the deque with
approximately the same O(1) performance in either direction

Though list objects support similar operations, they are optimized for fast fixed-length operations and incur O(n)
memory movement costs for pop(0) and insert(0, v) operations which change both the size and position of the
underlying data representation.

If maxlen is not specified or is None, deques may grow to an arbitrary length. Otherwise, the deque is bounded to the
specified maximum length. Once a bounded length deque is full, when new items are added, a corresponding
number of items are discarded from the opposite end. Bounded length deques provide functionality similar to the
tail filter in Unix. They are also useful for tracking transactions and other pools of data where only the most recent
activity is of interest.

Section 47.6: collections.ChainMap
ChainMap is new in version 3.3
Returns a new ChainMap object given a number of maps. This object groups multiple dicts or other mappings
together to create a single, updateable view.

The maps parameter list is ordered from first-searched to last-searched. Lookups search the underlying mappings
successively until a key is found. In contrast, writes, updates, and deletions only operate on the first mapping.


'''
import collections
from collections import OrderedDict
from collections import deque


#Section 47.1: collections.Counter
print("----Section 47.1: collections.Counter----------")


counts = collections.Counter([1,2,3])
print(counts)
#Letter Counter
print(collections.Counter('Happy Birthday'))

#Word Counter
print(collections.Counter('I am Sam Sam I am That Sam-I-am That Sam-I-am! I do not like that Sam-Iam'.split()))

#Recipes
c = collections.Counter({'a': 4, 'b': 2, 'c': -2, 'd': 0})
#Get count of individual element
print(c['a'])



#Set count of individual element
c['c'] = -3
print(c)

#Get total number of elements in counter
#print(sum(c.items()))

#Get elements (only those with positive counter are kept)
print(list(c.elements()))

#Remove keys with 0 or negative value
print(c - collections.Counter())

#Remove everything
c.clear()
print(c)

#Add remove individual elements
c.update({'a': 3, 'b':3})
c.update({'a': 2, 'c':2}) # adds to existing, sets if they don't exist
c.subtract({'a': 3, 'b': 3, 'c': 3}) # subtracts (negative values are allowed)


#Section 47.2: collections.OrderedDict
print("------Section 47.2: collections.OrderedDict-----------")
d = OrderedDict([('foo', 5), ('bar', 6)])
print(d)

#we can create an empty OrderedDict and then add items:
o = OrderedDict()
o['key1'] = "value1"
o['key2'] = "value2"
print(o)

#Section 47.3: collections.defaultdict
print("------Section 47.3: collections.defaultdict-------------")
state_capitals = collections.defaultdict(str)
print(state_capitals)

state_capitals['Alaska']
state_capitals['Alabama'] = 'Montgomery'
print(state_capitals)

#Using int as the default_factory will create a list for each new key
fruit_counts = collections.defaultdict(int)
fruit_counts['apple'] += 2 # No errors should occur
fruit_counts['banana'] # No errors should occur
print(fruit_counts)

#Using list as the default_factory will create a list for each new key
s = [('NC', 'Raleigh'), ('VA', 'Richmond'), ('WA', 'Seattle'), ('NC', 'Asheville')]
dd = collections.defaultdict(list)
for k, v in s:
    dd[k].append(v)
print(dd)

#Section 47.4: collections.namedtuple
print("--------Section 47.4: collections.namedtuple-----------")

Person = collections.namedtuple('Person', ['age', 'height', 'name'])
# or
Person = collections.namedtuple('Person', 'age, height, name')

# or
Person = collections.namedtuple('Person', 'age height name')

dave = Person(30, 178, 'Dave')
#  or
jack = Person(age=30, height=178, name='Jack S.')

print(jack.age)

Human = collections.namedtuple('Person', 'age, height, name')
dave = Human(30, 178, 'Dave')
print(dave)

#Section 47.5: collections.deque
print("-----Section 47.5: collections.deque----------")

d = deque('ghi')
for elem in d: # iterate over the deque's elements
    print(elem.upper())


d.append('j')               # add a new entry to the right side
d.appendleft('f')           # add a new entry to the left side
d.pop()                     # return and remove the rightmost item
d.popleft()                 # return and remove the leftmost item
list(d)                     # list the contents of the deque
d[0]                        # peek at leftmost item
d[-1]                       # peek at rightmost item
list(reversed(d))           # list the contents of a deque in reverse
'h' in d                    # search the deque
d.extend('jkl')             # add multiple elements at once
d.rotate(1)                 # right rotation
d.rotate(-1)                #  left rotation
deque(reversed(d))          # make a new deque in reverse order
d.clear()                   # empty the deque
#d.pop()                     # cannot pop from an empty deque
d.extendleft('abc')         # extendleft() reverses the input order

#Section 47.6: collections.ChainMap
print("---------Section 47.6: collections.ChainMap----------")
# define two dictionaries with at least some keys overlapping.
dict1 = {'apple': 1, 'banana': 2}
dict2 = {'coconut': 1, 'date': 1, 'apple': 3}
# create two ChainMaps with different ordering of those dicts.
combined_dict = collections.ChainMap(dict1, dict2)
reverse_ordered_dict = collections.ChainMap(dict2, dict1)
for k, v in combined_dict.items():
    print(k, v)
for k, v in reverse_ordered_dict.items():
    print(k, v)
