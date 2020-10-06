"""
Chapter 48: Operator module
Section 48.1: Itemgetter
Grouping the key-value pairs of a dictionary by the value with itemgetter

Section 48.2: Operators as alternative to an infix operator

Section 48.3: Methodcaller




"""
from itertools import groupby
from operator import itemgetter
from operator import add
from operator import mul
from operator import methodcaller


#Section 48.1: Itemgetter
print("-----Section 48.1: Itemgetter--------")

adict = {'a': 1, 'b': 5, 'c': 1}
dict((i, dict(v)) for i, v in groupby(adict.items(), itemgetter(1)))
# Output: {1: {'a': 1, 'c': 1}, 5: {'b': 5}}

#which is equivalent (but faster) to a lambda function like this:

dict((i, dict(v)) for i, v in groupby(adict.items(), lambda x: x[1]))

#Or sorting a list of tuples by the second element first the first element as secondary
alist_of_tuples = [(5,2), (1,3), (2,2)]
sorted(alist_of_tuples, key=itemgetter(1,0))

#Section 48.2: Operators as alternative to an infix operator
print("-----Section 48.2: Operators as alternative to an infix operator---------")
print(add(1, 1))
print(mul('a', 10))
print(mul([3], 3))

#Section 48.3: Methodcaller
print("-------Section 48.3: Methodcaller---------")
alist = ['wolf', 'sheep', 'duck']
list(filter(lambda x: x.startswith('d'), alist)) # Keep only elements that start with 'd'
# Output: ['duck']

# or

list(filter(methodcaller('startswith', 'd'), alist)) # Does the same but is faster