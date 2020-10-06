''''
Chapter 33: Functions
Parameter               Details
arg1, ..., argN         Regular arguments
*args                   Unnamed positional arguments
kw1, ..., kwN           Keyword-only arguments
**kwargs                The rest of keyword arguments

Section 33.1: Defining and calling simple functions
Using the def statement is the most common way to define a function in python. This statement is a so called single
clause compound statement with the following syntax:
def function_name(parameters):
    statement(s)

function_name is known as the identifier of the function. Since a function definition is an executable statement its
execution binds the function name to the function object which can be called later on using the identifier.
parameters is an optional list of identifiers that get bound to the values supplied as arguments when the function is
called. A function may have an arbitrary number of arguments which are separated by commas.
statement(s) – also known as the function body – are a nonempty sequence of statements executed each time the
function is called. This means a function body cannot be empty, just like any indented block.

Python functions can return values of any type via the return keyword.
A function that reaches the end of execution without a return statement will always return None:


Section 33.2: Defining a function with an arbitrary number of arguments
Defining a function capable of taking an arbitrary number of arguments can be done by prefixing one of the
arguments with a *

You can't provide a default for args, for example func(*args=[1, 2, 3]) will raise a syntax error (won't even
compile).
You can't provide these by name when calling the function, for example func(*args=[1, 2, 3]) will raise a
TypeError.

These arguments (*args) can be accessed by index, for example args[0] will return the first argument

Arbitrary number of keyword arguments
You can take an arbitrary number of arguments with a name by defining an argument in the definition with  ** in front of it:
kwargs is a plain native python dictionary. For example, args['value1'] will give the value for argument value1.

Warning
You can mix these with other optional and required arguments but the order inside the definition matters.
The positional/keyword arguments come first. (Required arguments).
Then comes the arbitrary *arg arguments. (Optional).
GoalKicker.com – Python® Notes for Professionals 180
Then keyword-only arguments come next. (Required).
Finally the arbitrary keyword **kwargs come. (Optional).

# |-positional-|-optional-|---keyword-only--|-optional-|
def func(arg1, arg2=10 , *args, kwarg1, kwarg2=2, **kwargs):
    pass
arg1 must be given, otherwise a TypeError is raised. It can be given as positional (func(10)) or keyword
argument (func(arg1=10)).
kwarg1 must also be given, but it can only be provided as keyword-argument: func(kwarg1=10).
arg2 and kwarg2 are optional. If the value is to be changed the same rules as for arg1 (either positional or
keyword) and kwarg1 (only keyword) apply.
*args catches additional positional parameters. But note, that arg1 and arg2 must be provided as positional
arguments to pass arguments to *args: func(1, 1, 1, 1).
**kwargs catches all additional keyword parameters. In this case any parameter that is not arg1, arg2,
kwarg1 or kwarg2. For example: func(kwarg3=10).
In Python 3, you can use * alone to indicate that all subsequent arguments must be specified as keywords.
For instance the math.isclose function in Python 3.5 and higher is defined using def math.isclose (a, b,
*, rel_tol=1e-09, abs_tol=0.0), which means the first two arguments can be supplied positionally but the
optional third and fourth parameters can only be supplied as keyword arguments.

Note on Uniqueness
Any function can be defined with none or one *args and none or one **kwargs but not with more than one of
each. Also *args must be the last positional argument and **kwargs must be the last parameter. Attempting to use
more than one of either will result in a Syntax Error exception


Section 33.3: Lambda (Inline/Anonymous) Functions
The lambda keyword creates an inline function that contains a single expression. The value of this expression is
what the function returns when invoked.
lambdas are commonly used for short functions that are convenient to define at the point where they are called
(typically with sorted, filter and map).

They can also take arbitrary number of arguments / keyword arguments, like normal functions.
greeting = lambda x, *args, **kwargs: print(x, args, kwargs)
greeting('hello', 'world', world='world')


Always use a def statement instead of an assignment statement that binds a lambda expression directly
to an identifier.
Yes:
    def f(x): return 2*x
No:
    f = lambda x: 2*x

The use of the assignment statement eliminates the sole benefit a lambda expression can offer over an explicit def
statement (i.e. that it can be embedded inside a larger expression).

Section 33.4: Defining a function with optional arguments
Optional arguments can be defined by assigning (using =) a default value to the argument-name:

Mutable types (list, dict, set, etc.) should be treated with care when given as default attribute. Any
mutation of the default argument will change it permanently. See Defining a function with optional
mutable arguments

Section 33.5: Defining a function with optional mutable arguments
There is a problem when using optional arguments with a mutable default type (described in Defining a function
with optional arguments), which can potentially lead to unexpected behaviour.

However, for a mutable type, the original value can mutate, by making
calls to its various member functions. Therefore, successive calls to the function are not guaranteed to have the
initial default value.

Solution
If you want to ensure that the default argument is always the one you specify in the function definition, then the
solution is to always use an immutable type as your default argument.
def append(elem, to=None):
    if to is None:
        to = []

Section 33.6: Argument passing and mutability
First, some terminology:
argument (actual parameter): the actual variable being passed to a function;
parameter (formal parameter): the receiving variable that is used in a function.

In Python, we don’t really assign values to variables, instead we bind (i.e. assign, attach) variables
(considered as names) to objects.
Immutable: Integers, strings, tuples, and so on. All operations make copies.
Mutable: Lists, dictionaries, sets, and so on. Operations may or may not mutate.


Section 33.7: Returning values from functions
If return is encountered in the function the function will be exited immediately and subsequent operations will not
be evaluated:

You can also return multiple values (in the form of a tuple):

A function with no return statement implicitly returns None. Similarly a function with a return statement, but no
return value or variable returns None.

Section 33.8: Closure
A Closure is an inner function that remembers the instance of the function and hence the outer function retun statement
is the inner function instance and not any value

There must be a nested function ( a function inside another function)
This nested function has to refer toa variable  defined inside the enclosing function
The enclosing function must return the nested function
All function objects have a __closure__ attribute that returns a tuple of cell objects if it is a closure function

Closure provide some sort of data hiding as they are used a call back functions. This helps us to reduce the iuse of
global variables
Useful for replacing hard coded constants



Section 33.9: Forcing the use of named parameters
All parameters specified after the first asterisk in the function signature are keyword-only
def f(*a, b):
    pass
f(1, 2, 3)
# TypeError: f() missing 1 required keyword-only argument: 'b'

def f(a, b, *, c):
    pass
f(1, 2, 3) # TypeError: f() takes 2 positional arguments but 3 were given
f(1, 2, c=3) # No error

Section 33.10: Nested functions
Functions in python are first-class objects. They can be defined in any scope

Section 33.11: Recursion limit
There is a limit to the depth of possible recursion, which depends on the Python implementation. When the limit is
reached, a RuntimeError exception is raised:

It is possible to change the recursion depth limit by using sys.setrecursionlimit(limit) and check this limit by
sys.getrecursionlimit().

From Python 3.5, the exception is a RecursionError, which is derived from RuntimeError.

Section 33.12: Recursive Lambda using assigned variable

Section 33.13: Recursive functions

Section 33.14: Defining a function with arguments

Section 33.15: Iterable and dictionary unpacking
Functions allow you to specify these types of parameters: positional, named, variable positional, Keyword args
(kwargs). Here is a clear and concise use of each type.

Section 33.16: Defining a function with multiple arguments
One can give a function as many arguments as one wants, the only fixed rules are that each argument name must
be unique and that optional arguments must be after the not-optional ones:
combine giving the arguments with name and without. Then the ones with name must follow those without but
the order of the ones with name doesn't matter:

Chapter 34: Defining functions with list arguments:

Section 34.1: Function and Call

Chapter 35: Functional Programming in Python:
An anonymous, inlined function defined with lambda. The parameters of the lambda are defined to the left of the
colon. The function body is defined to the right of the colon. The result of running the function body is (implicitly)
returned.
s=lambda x:x*x
s(2) =>4

Section 35.2: Map Function
Map takes a function and a collection of items. It makes a new, empty collection, runs the function on each item in
the original collection and inserts each return value into the new collection. It returns the new collection.

name_lengths = map(len, ["Mary", "Isla", "Sam"])
print(name_lengths) =>[4, 4, 3]

Section 35.3: Reduce Function
Reduce takes a function and a collection of items. It returns a value that is created by combining the items.

total = reduce(lambda a, x: a + x, [0, 1, 2, 3, 4])
print(total) =>10

Section 35.4: Filter Function:
Filter takes a function and a collection. It returns a collection of every item for which the function returned True.

arr=[1,2,3,4,5,6]
[i for i in filter(lambda x:x>4,arr)] # outputs[5,6]

Chapter 36: Partial functions
This is used when an operation needs to be done on two variables like multiply, exponentional, etc and i think its like
closure.

Param details
x the number to be raised
y the exponent
raise the function to be specialized

Section 36.1: Raise the power

from functors import partial
def multiply(x,y)
    return x*y
mul = partial(multiply,y=5)
print(mul(3))





'''

#Section 33.2: Defining a function with an arbitrary number of arguments
def func(*args):
    # args will be a tuple containing all values that are passed in
    for i in args:
        print(i)

#Arbitrary number of keyword arguments
def func(**kwargs):
    # kwargs will be a dictionary containing the names as keys and the values as values
    for name, value in kwargs.items():
        print(name, value)

def fn(**kwargs):
    print(kwargs)
    f1(**kwargs)

def f1(**kwargs):
    print(len(kwargs))
    print(kwargs)

fn(a=1, b=2)

#Section 33.3: Lambda (Inline/Anonymous) Functions
greet_me = lambda: "Hello"

print(greet_me())

#This creates an inline function with the name greet_me that returns Hello. Note that you don't write return when
#creating a function with lambda. The value after : is automatically returned.

#lambdas can take arguments, too:
#They can also take arbitrary number of arguments / keyword arguments, like normal functions.
greeting = lambda x, *args, **kwargs: print(x, args, kwargs)

(greeting('hello', 'world', world='world'))

#Reassigning the parameter won’t reassign the argument.
def foo(x): # here x is the parameter, when we call foo(y) we assign y to x
    x[0] = 9 # This mutates the list labelled by both x and y
    x = [1, 2, 3] # x is now labeling a different list (y is unaffected)
    x[2] = 8 # This mutates x's list, not y's list
y = [4, 5, 6] # y is the argument, x is the parameter
foo(y) # Pretend that we wrote "x = y", then go to line 1
print(y)
# Out: [9, 5, 6]
print("---------")
x = [3, 1, 9]
y = x
x.append(5) # Mutates the list labelled by x and y, both x and y are bound to [3, 1, 9]
x.sort() # Mutates the list labelled by x and y (in-place sorting)
print(x,y)
x = x + [4] # Does not mutate the list (makes a copy for x only, not y)
print(x,y)
z = x # z is x ([1, 3, 9, 4])
print(x,z)
x += [6] # Mutates the list labelled by both x and z (uses the extend function).
x = sorted(x) # Does not mutate the list (makes a copy for x only).
print(x)
# Out: [1, 3, 4, 5, 6, 9]
print(y)
# Out: [1, 3, 5, 9]
print(z)
# Out: [1, 3, 5, 9, 4, 6]

#Closure
def makeInc(x):
    def inc(y):
        # x is "attached" in the definition of inc
        return y + x

    return inc # See here the return is inc instance

incOne = makeInc(1)
incFive = makeInc(5)

print(incOne(5)) # returns 6
print(incFive(5)) # returns 10

# As x is attached to Inc instance you can not modify x
def makeInc(x):
    def inc(y):
        # incrementing x is not allowed
        x += y
        return x
    return inc

incOne = makeInc(1)
#incOne(5) # UnboundLocalError: local variable 'x' referenced before assignment

#Python 3 offers the nonlocal statement (Nonlocal Variables ) for realizing a full closure with nested functions.
def makeInc(x):
    def inc(y):
        nonlocal x
        # now assigning a value to x is allowed
        x += y
        return x
    return inc
incOne = makeInc(1)
print(incOne(5)) # returns 6

#33.10 Functions

def fibonacci(n):
    def step(a,b):
        return b, a+b
    a, b = 0, 1
    for i in range(n):
        a, b = step(a, b)
    return a

print(fibonacci(4))

def make_adder(n):
    def adder(x):
        return n + x
    return adder

add5 = make_adder(5)
def repeatedly_apply(func, n, x):
    for i in range(n):
        x = func(x)
    return x
print(repeatedly_apply(add5, 5, 1)) #Out: 26

#Section 33.12: Recursive Lambda using assigned variable
lambda_factorial = lambda i:1 if i==0 else i*lambda_factorial(i-1)
print(lambda_factorial(4)) # 4 * 3 * 2 * 1 = 12 * 2 = 24

#Section 33.13: Recursive functions
def factorial(n):
    #n here should be an integer
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

factorial = lambda n: 1 if n == 0 else n*factorial(n-1)

# Partial functions
print("PArtial Fucntion")
from functools import partial
def multiply(x,y):
    return x*y
mul = partial(multiply,y=5)
print(mul(3))
