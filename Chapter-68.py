"""
Chapter 68: Reduce
Parameter               Details
function                function that is used for reducing the iterable (must take two arguments). (positional-only)
iterable                iterable that's going to be reduced. (positional-only)
initializer             start-value of the reduction. (optional, positional-only)

Section 68.1: Overview
reduce reduces an iterable by applying a function repeatedly on the next element of an iterable and the
cumulative result so far.

Section 68.2: Using reduce

Section 68.4: Non short-circuit variant of any/all
reduce will not terminate the iteration before the iterable has been completely iterated over so it can be used to
create a non short-circuit any() or all() function:


"""
from functools import reduce # mandatory
import operator


def add(s1, s2):
    return s1 + s2
asequence = [1, 2, 3]

print(reduce(add, asequence)) # equivalent to: add(add(1,2),3)

print(reduce(operator.add, asequence))

#reduce can also be passed a starting value:
print(reduce(add, asequence, 10))


#Section 68.2: Using reduce
print("-----Section 68.2: Using reduce-------")
#Section 68.3: Cumulative product
print("-----Section 68.3: Cumulative product-----")

reduce(operator.mul, [10, 5, -3])

#Section 68.4: Non short-circuit variant of any/all
print("------Section 68.4: Non short-circuit variant of any/all---------")

#Section 68.4: Non short-circuit variant of any/all
print("-------Section 68.4: Non short-circuit variant of any/all=-------")
# non short-circuit "all"
reduce(operator.and_, [False, True, True, True]) # = False
# non short-circuit "any"
reduce(operator.or_, [True, False, False, False]) # = True
