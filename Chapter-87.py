"""
Chapter 87: Type Hints
Section 87.1: Adding types to a function

To indicate that we only want to allow int types we can change our function definition to look like:

def two_sum(a: int, b: int):
    return a + b

Apart from specifying the type of the arguments, one could also indicate the return value of a function call. This is
done by adding the -> character followed by the type after the closing parenthesis in the argument list but before
the : at the end of the function declaration:

def two_sum(a: int, b: int) -> int:
    return a + b

Now we've indicated that the return value when calling two_sum should be of type int. Similarly we can define
appropriate values for str, float, list, set and others.

Although type hints are mostly used by type checkers and IDEs, sometimes you may need to retrieve them. This can
be done using the __annotations__ special attribute:

two_sum.__annotations__
# {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}


Section 87.2: NamedTuple
Creating a namedtuple with type hints is done using the function NamedTuple from the typing module:

import typing
Point = typing.NamedTuple('Point', [('x', int), ('y', int)])

Note that the name of the resulting type is the first argument to the function, but it should be assigned to a variable
with the same name to ease the work of type checkers.

Section 87.3: Generic Types
The typing.TypeVar is a generic type factory. It's primary goal is to serve as a parameter/placeholder for generic
function/class/method annotations:

T = typing.TypeVar("T")
def get_first_element(l: typing.Sequence[T]) -> T:
    \"""Gets the first element of a sequence.\"""
    return l[0]

Section 87.4: Variables and Attributes

x = 3 # type: int
x = negate(x)
x = 'a type-checker might catch this error'
Python 3.x Version ≥ 3.6
Starting from Python 3.6, there is also new syntax for variable annotations. The code above might use the form
x: int = 3

Additionally if these are used in the module or the class level, the type hints can be retrieved using
typing.get_type_hints(class_or_module):

class Foo:
    x: int
    y: str = 'abc'
print(typing.get_type_hints(Foo))
# ChainMap({'x': <class 'int'>, 'y': <class 'str'>}, {})

Alternatively, they can be accessed by using the __annotations__ special variable or attribute:
x: int
print(__annotations__)
# {'x': <class 'int'>}

Section 87.5: Class Members and Methods
class A:
    x = None # type: float
    def __init__(self, x: float) -> None:
        \"""
        self should not be annotated
        init should be annotated to return None
        \"""
        self.x = x

    @classmethod
    def from_int(cls, x: int) -> 'A':
        \"""
        cls should not be annotated
        Use forward reference to refer to current class with string literal 'A'
        \"""
        return cls(float(x))


Section 87.6: Type hints for keyword arguments
def hello_world(greeting: str = 'Hello'):
    print(greeting + ' world!')
Note the spaces around the equal sign as opposed to how keyword arguments are usually styled.

"""