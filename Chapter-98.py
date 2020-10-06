"""
Chapter 98: Overloading
Section 98.1: Operator overloading
Each of the methods corresponding to a binary operator has a corresponding "right" method which start with __r,
for example __radd__:

Section 98.2: Magic/Dunder Methods
Magic (also called dunder as an abbreviation for double-underscore) methods in Python serve a similar purpose to
operator overloading in other languages. They allow a class to define its behavior when it is used as an operand in
unary or binary operator expressions. They also serve as implementations called by some built-in functions


Section 98.3: Container and sequence types
It is possible to emulate container types, which support accessing values by key or index.

Section 98.4: Callable types
class adder(object):
    def __init__(self, first):
        self.first = first
    # a(...)
    def __call__(self, second):
        return self.first + second

add2 = adder(2)
add2(1) # 3
add2(2) # 4

Section 98.5: Handling unimplemented behaviour
If your class doesn't implement a specific overloaded operator for the argument types provided, it should return
NotImplemented (note that this is a special constant, not the same as NotImplementedError). This will allow Python
to fall back to trying other methods to make the operation work:

When NotImplemented is returned, the interpreter will then try the reflected operation on the other type,
or some other fallback, depending on the operator. If all attempted operations return NotImplemented,
the interpreter will raise an appropriate exception.





"""