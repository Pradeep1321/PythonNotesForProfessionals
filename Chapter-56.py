"""
Chapter 56: Functools Module

Section 56.1: partial

The partial function creates partial function application from another function. It is used to bind values to some of
the function's arguments (or keyword arguments) and produce a callable without the already defined arguments.

One way to think of partial is a shift register; pushing in one argument at the time into some function. partial
comes handy for cases where data is coming in as stream and we cannot pass more than one argument.

Section 56.2: cmp_to_key
Python changed its sorting methods to accept a key function. Those functions take a value and return a key which is
used to sort the arrays.
Old comparison functions used to take two values and return -1, 0 or +1 if the first argument is small, equal or
greater than the second argument respectively. This is incompatible to the new key-function.
That's where functools.cmp_to_key comes in:

Section 56.3: lru_cache
The @lru_cache decorator can be used wrap an expensive, computationally-intensive function with a Least Recently
Used cache. This allows function calls to be memoized, so that future calls with the same parameters can return
instantly instead of having to be recomputed.

the value of fibonacci(3) is only calculated once, whereas if fibonacci didn't have an LRU
cache, fibonacci(3) would have been computed upwards of 230 times. Hence, @lru_cache is especially great for
recursive functions or dynamic programming, where an expensive function could be called multiple times with the
same exact parameters.

@lru_cache has two arguments
    maxsize: Number of calls to save. When the number of unique calls exceeds maxsize, the LRU cache will
            remove the least recently used calls.
    typed (added in 3.3): Flag for determining if equivalent arguments of different types belong to different cache
            records (i.e. if 3.0 and 3 count as different arguments)

NOTE: Since @lru_cache uses dictionaries to cache results, all parameters for the function must be hashable for the
cache to work.
Official Python docs for @lru_cache. @lru_cache was added in 3.2.


Section 56.4: total_ordering
This is expensive and slow and difficult to trace the actual problem

When we want to create an orderable class, normally we need to define the methods __eq()__, __lt__(),
__le__(), __gt__() and __ge__().
The total_ordering decorator, applied to a class, permits the definition of __eq__() and only one between
__lt__(), __le__(), __gt__() and __ge__(), and still allow all the ordering operations on the class.

Note: The total_ordering function is only available since Python 2.7.

Section 56.5: reduce

In Python 3.x, the reduce function already explained here has been removed from the built-ins and must now be
imported from functools.

"""
from functools import partial
from functools import lru_cache
from functools import total_ordering
import functools
import locale
from functools import reduce

#Section 56.1: partial
print("------Section 56.1: partial-----")
unhex = partial(int, base=16)
unhex.__doc__ = 'Convert base16 string to int'
print(unhex('ca11ab1e'))

def f(a, b, c, x):
    return 1000 * a + 100 * b + 10 * c + x

g = partial(f, 5, 1, 1)
print(g(8))

#Section 56.2: cmp_to_key
print("------Section 56.2: cmp_to_key------")
print(sorted(["A", "S", "F", "D"], key=functools.cmp_to_key(locale.strcoll)))

@lru_cache(maxsize=None) # Boundless cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(15))

#We can see cache stats too:
print(fibonacci.cache_info())

#Section 56.4: total_ordering
print("------Section 56.4: total_ordering-----------")

@total_ordering
class Employee:
    def __eq__(self, other):
        return ((self.surname, self.name) == (other.surname, other.name))

    def __lt__(self, other):
        return ((self.surname, self.name) < (other.surname, other.name))


#Section 56.5: reduce
print("-------Section 56.5: reduce-----------")
def factorial(n):
    return reduce(lambda a, b: (a*b), range(1, n+1))
print(factorial(5))