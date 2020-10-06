"""
Chapter 86: Recursion
Section 86.1: The What, How, and When of Recursion


A tail call is simply a recursive function call which is the last operation to be performed before returning a
value. To be clear, return foo(n - 1) is a tail call, but return foo(n - 1) + 1 is not (since the addition is
the last operation).
Tail call optimization (TCO) is a way to automatically reduce recursion in recursive functions.
Tail call elimination (TCE) is the reduction of a tail call to an expression that can be evaluated without
recursion. TCE is a type of TCO.


Tail call optimization is helpful for a number of reasons:
    The interpreter can minimize the amount of memory occupied by environments. Since no computer has
    unlimited memory, excessive recursive function calls would lead to a stack overflow.
    The interpreter can reduce the number of stack frame switches.

Python has no form of TCO implemented for a number of a reasons.

This is usually the most efficient way to manually eliminate recursion, but it can become rather difficult for more
complex functions.

Another useful tool is Python's lru_cache decorator which can be used to reduce the number of redundant
calculations.

Section 86.4: Increasing the Maximum Recursion Depth
There is a limit to the depth of possible recursion, which depends on the Python implementation. When the limit is
reached, a RuntimeError exception is raised:

It is possible to change the recursion depth limit by using
sys.setrecursionlimit(limit)

You can check what the current parameters of the limit are by running:
sys.getrecursionlimit()

From Python 3.5, the exception is a RecursionError, which is derived from RuntimeError

Section 86.5: Tail Recursion - Bad Practice
When the only thing returned from a function is a recursive call, it is referred to as tail recursion.

Tail recursion is considered a bad practice in Python, since the Python compiler does not handle optimization for
tail recursive calls. The recursive solution in cases like this use more system resources than the equivalent iterative
solution.

Section 86.6: Tail Recursion Optimization Through Stack Introspection
Instead, we can also solve the Tail Recursion problem using stack introspection.
#!/usr/bin/env python2.4
# This program shows off a python decorator which implements tail call optimization. It
# does this by throwing an exception if it is its own grandparent, and catching such
# exceptions to recall the stack.
import sys
class TailRecurseException:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs

def tail_call_optimized(g):
    \"""
    This function decorates a function with tail call
    optimization. It does this by throwing an exception
    if it is its own grandparent, and catching such
    exceptions to fake the tail call optimization.
    This function fails if the decorated function recurses in a non-tail context.
    \"""
    def func(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:
            raise TailRecurseException(args, kwargs)
        else:
            while 1:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException, e:
                    args = e.args
                    kwargs = e.kwargs
        func.__doc__ = g.__doc__
        return func

To optimize the recursive functions, we can use the @tail_call_optimized decorator to call our function. Here's a
few of the common recursion examples using the decorator described above:

@tail_call_optimized
def factorial(n, acc=1):
    "calculate a factorial"
    if n == 0:
        return acc
    return factorial(n-1, n*acc)
print factorial(10000)
# prints a big, big number,
# but doesn't hit the recursion limit


"""