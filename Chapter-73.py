"""
Chapter 73: Counting
Section 73.1: Counting all occurrence of all items in an iterable: collections.Counter

The collections.Counter can be used for any iterable and counts every occurrence for every element.
Note: One exception is if a dict or another collections.Mapping-like class is given, then it will not count them,
rather it creates a Counter with these values:

Counter({"e": 2})
# Out: Counter({"e": 2})
Counter({"e": "e"}) # warning Counter does not verify the values are int
# Out: Counter({"e": "e"})


Section 73.2: Getting the most common value(-s): collections.Counter.most_common()
Counting the keys of a Mapping isn't possible with collections.Counter but we can count the values:


Section 73.3: Counting the occurrences of one item in a sequence: list.count() and tuple.count()

Section 73.4: Counting the occurrences of a substring in a string: str.count()

Section 73.5: Counting occurrences in numpy array
There are two methods I use to count occurrences of all unique values in numpy. Unique and bincount. Unique
automatically flattens multidimensional arrays, while bincount only works with 1d arrays only containing positive
integers.

If your data are numpy arrays it is generally much faster to use numpy methods then to convert your data to
generic methods.

"""

from collections import Counter
import numpy as np


#Section 73.1: Counting all occurrence of all items in an iterable: collections.Counter
print("------Section 73.1: Counting all occurrence of all items in an iterable: collections.Counter-------")

c = Counter(["a", "b", "c", "d", "a", "b", "a", "c", "d"])
print(c)

#Section 73.2: Getting the most common value(-s): collections.Counter.most_common()
print("------Section 73.2: Getting the most common value(-s): collections.Counter.most_common()--------")

adict = {'a': 5, 'b': 3, 'c': 5, 'd': 2, 'e':2, 'q': 5}
print(Counter(adict.values()))

#The most common elements are available by the most_common-method:

## Sorting them from most-common to least-common value:
print(Counter(adict.values()).most_common())
# Out: [(5, 3), (2, 2), (3, 1)]

# Getting the most common value
print(Counter(adict.values()).most_common(1))
# Out: [(5, 3)]

# Getting the two most common values
print(Counter(adict.values()).most_common(2))
# Out: [(5, 3), (2, 2)]

#Section 73.3: Counting the occurrences of one item in a sequence: list.count() and tuple.count()
print("-------Section 73.3: Counting the occurrences of one item in a sequence: list.count() and tuple.count()-------")

alist = [1, 2, 3, 4, 1, 2, 1, 3, 4]
print(alist.count(1))

atuple = ('bear', 'weasel', 'bear', 'frog')
print(atuple.count('bear'))

#Section 73.4: Counting the occurrences of a substring in a string: str.count()
print("---------Section 73.4: Counting the occurrences of a substring in a string: str.count()-----")

astring = 'thisisashorttext'
print(astring.count('t'))

#This works even for substrings longer than one character:
print(astring.count('th'))

#which would not be possible with collections.Counter which only counts single characters:

print(Counter(astring))
# Out: Counter({'a': 1, 'e': 1, 'h': 2, 'i': 2, 'o': 1, 'r': 1, 's': 3, 't': 4, 'x': 1})

#Section 73.5: Counting occurrences in numpy array
print("------Section 73.5: Counting occurrences in numpy array----")

#To count the occurrences of a value in a numpy array. This will work:

a=np.array([0,3,4,3,5,4,7])
print(np.sum(a==3))
#The logic is that the boolean statement produces a array where all occurrences of the requested values are 1 and
#all others are zero. So summing these gives the number of occurencies. This works for arrays of any shape or dtype.

unique,counts=np.unique(a,return_counts=True)
print(unique,counts) # counts[i] is equal to occurrences of unique[i] in a

bin_count=np.bincount(a)
print(bin_count) # bin_count[i] is equal to occurrences of i in a




