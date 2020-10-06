"""
Chapter 7: Enum
Section 7.1: Creating an enum (Python 2.4 through 3.3)
Enums have been backported from Python 3.4 to Python 2.4 through Python 3.3. You can get this the enum34
backport from PyPI.


Section 7.2: Iteration

Chapter 8: Set
Section 8.1: Operations on sets
with other sets
# Intersection
# Union
# Difference
# Symmetric difference with
# Superset check
# Subset check
# Disjoint check

with single elements
# Existence check
# Add and Remove

Set operations return new sets, but have the corresponding in-place versions:
method      in-place operation      in-place method
union           s |= t                  update
intersection    s &= t                  intersection_update
difference      s -= t                  difference_update
symmetric_difference s ^= t             symmetric_difference_update

Section 8.2: Get the unique elements of a list
The best way to get the unique elements from a list is to turn it into a set:
Note that the set is not in the same order as the original list; that is because sets are unordered, just like dicts.

Section 8.3: Set of Sets
{{1,2}, {3,4}}
leads to:
TypeError: unhashable type: 'set'
Instead, use frozenset:
{frozenset({1, 2}), frozenset({3, 4})}

Section 8.4: Set Operations using Methods and Builtins
NOTE: {1} creates a set of one element, but {} creates an empty dict. The correct way to create an
empty set is set().

Intersection
Union
Difference
Symmetric Difference
NOTE: a.symmetric_difference(b) == b.symmetric_difference(a)
Subset and superset
Disjoint sets

Method                      Operator
a.intersection(b)               a & b
a.union(b)                      a|b
a.difference(b)                 a - b
a.symmetric_difference(b)       a ^ b
a.issubset(b)                   a <= b
a.issuperset(b)                 a >= b


Section 8.5: Sets versus multisets
Sets are unordered collections of distinct elements.
For implementing multisets Python provides the Counter class from the collections module (starting from version
2.7):
Counter is a dictionary where where elements are stored as dictionary keys and their counts are stored as
dictionary values. And as all dictionaries, it is an unordered collection.


"""

from enum import Enum
class Color(Enum):
    red = 1
    green = 2
    blue = 3
print(Color.red) # Color.red
print(Color(1)) # Color.red
print(Color['red']) # Color.red