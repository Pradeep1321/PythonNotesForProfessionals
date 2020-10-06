import keyword
"""

Python can be passed arbitrary code as a string in the shell:
$ python -c 'print("Hello, World")'
Hello, World
This can be useful when concatenating the results of scripts together in the shell.


Shells and Beyond:
GUI, IPython - known for extending the interactive experience, etc.
Programs - shell, IDEs (such as PyCharm), Jupyter notebooks, etc
Python tutor allows you to step through Python code so you can visualize how the program will flow, and helps you
to understand where your program went wrong.
PEP8 defines guidelines for formatting Python code. Formatting code well is important so you can quickly read what
the code does.

Section 1.2: Creating variables and assigning value
You can not use python's keywords as a valid variable name. You can see the list of keyword by:

Rules for variable naming:
    1. Variables names must start with a letter or an underscore.
    2. The remainder of your variable name may consist of letters, numbers and underscores.
    3. Names are case sensitive.

Even though there's no need to specify a data type when declaring a variable in Python, while allocating the
necessary area in memory for the variable, the Python interpreter automatically picks the most suitable built-in
type for it:

When you use = to do an assignment operation, what's on the left of = is a name for the object on the right. Finally,
what = does is assign the reference of the object on the right to the name on the left.
That is:
a_name = an_object # "a_name" is now a name for the reference to the object "an_object"

You can assign multiple values to multiple variables in one line. Note that there must be the same number of
arguments on the right and left sides of the = operator:
a, b, c = 1, 2, 3
it is conventional to use the underscore (_) for assigning unwanted
values:
Note that the number of _ and number of remaining values must be equal.
a, b, _ = 1, 2, 3
print(a, b)

You can also assign a single value to several variables simultaneously.
When using such cascading assignment, it is important to note that all three variables a, b and c refer to the same
object in memory. This is also true for mutable types (like list, dict, etc.) just as it is true for immutable types (like int, string,
tuple, etc.):
a = b = c = 1

Section 1.3: Block Indentation
All blocks start with a colon and then contain the indented lines

Spaces vs. Tabs
In short: always use 4 spaces for indentation.

Using tabs exclusively is possible but PEP 8, the style guide for Python code, states that spaces are preferred.
Python 3.x Version ≥ 3.0
Python 3 disallows mixing the use of tabs and spaces for indentation. In such case a compile-time error is
generated: Inconsistent use of tabs and spaces in indentation and the program will not run.
Python 2.x Version ≤ 2.7
GoalKicker.com – Python® Notes for Professionals 11
Python 2 allows mixing tabs and spaces in indentation; this is strongly discouraged. The tab character completes
the previous indentation to be a multiple of 8 spaces. Since it is common that editors are configured to show tabs
as multiple of 4 spaces, this can cause subtle bugs.

Citing PEP 8:
    When invoking the Python 2 command line interpreter with the -t option, it issues warnings about code
that illegally mixes tabs and spaces. When using -tt these warnings become errors. These options are
highly recommended!

Python source code written with a mix of tabs and spaces, or with non-standard number of indentation spaces can
be made pep8-conformant using autopep8. (A less powerful alternative comes with most Python installations:
reindent.py)

Section 1.4: Datatypes

Built-in Types
Booleans
bool: A boolean value of either True or False. Logical operations like and, or, not can be performed on booleans
In Python 2.x and in Python 3.x, a boolean is also an int. The bool type is a subclass of the int type and True and
False are its only instances:
If boolean values are used in arithmetic operations, their integer values (1 and 0 for True and False) will be used to
return an integer result:

Numbers
int: Integer number
Integers in Python are of arbitrary sizes.
Note: in older versions of Python, a long type was available and this was distinct from int. The two have
been unified.

float: Floating point number; precision depends on the implementation and system architecture, for
CPython the float datatype corresponds to a C double.

complex: Complex numbers
The <, <=, > and >= operators will raise a TypeError exception when any operand is a complex number

Strings
Python 3.x Version ≥ 3.0
    str: a unicode string. The type of 'hello'
    bytes: a byte string. The type of b'hello'
Python 2.x Version ≤ 2.7
    str: a byte string. The type of 'hello'
    bytes: synonym for str
    unicode: a unicode string. The type of u'hello'
    
Sequences and collections
Python differentiates between ordered sequences and unordered collections (such as set and dict).
    strings (str, bytes, unicode) are sequences
    reversed: A reversed order of str with reversed function
        a = reversed('hello')
    tuple: An ordered collection of n values of any type (n >= 0).
        Supports indexing; immutable; hashable if all its members are hashable
    list: An ordered collection of n values (n >= 0)
        Not hashable; mutable.
    set: An unordered collection of unique values. Items must be hashable.
        a = {1, 2, 'a'}
    dict: An unordered collection of unique key-value pairs; keys must be hashable.

An object is hashable if it has a hash value which never changes during its lifetime (it needs a __hash__()
method), and can be compared to other objects (it needs an __eq__() method). Hashable objects which
compare equality must have the same hash value.

Built-in constants

In conjunction with the built-in datatypes there are a small number of built-in constants in the built-in namespace:
True: The true value of the built-in type bool
False: The false value of the built-in type bool
None: A singleton object used to signal that a value is absent.
Ellipsis or ...: used in core Python3+ anywhere and limited usage in Python2.7+ as part of array notation.
numpy and related packages use this as a 'include everything' reference in arrays.
NotImplemented: a singleton used to indicate to Python that a special method doesn't support the specific
arguments, and Python will try alternatives if available.
a = None # No value will be assigned. Any valid datatype can be assigned later
Python 3.x Version ≥ 3.0
None doesn't have any natural ordering. Using ordering comparison operators (<, <=, >=, >) isn't supported anymore
and will raise a TypeError.
Python 2.x Version ≤ 2.7
None is always less than any number (None < -32 evaluates to True).

Converting between datatypes
Explicit string type at definition of literals

With one letter labels just in front of the quotes you can tell what type of string you want to define.
b'foo bar': results bytes in Python 3, str in Python 2
u'foo bar': results str in Python 3, unicode in Python 2
'foo bar': results str
r'foo bar': results so called raw string, where escaping special characters is not necessary, everything is
taken verbatim as you typed


Mutable and Immutable Data Types

An object is called mutable if it can be changed.
An object is called immutable if it cannot be changed in any way.
Note that variables themselves are mutable, so we can reassign the variable x, but this does not change the object
that x had previously pointed to. It only made x point to a new object.
Data types whose instances are mutable are called mutable data types, and similarly for immutable objects and datatypes.

Examples of immutable Data Types:
    int, long, float, complex
    str
    bytes
    tuple
    frozenset
Examples of mutable Data Types:
    bytearray
    list
    set
    dict

Section 1.5: Collection Types:
There are a number of collection types in Python. While types such as int and str hold a single value, collection
types hold multiple values.

Lists:
The list type is probably the most commonly used collection type in Python. a list is merely an ordered collection of valid Python values.
The elements of a list are not restricted to a single data type, which makes sense given that Python is a dynamic
language.
Append object to end of list with L.append(object), returns None.

Tuples:
A tuple is similar to a list except that it is fixed-length and immutable. So the values in the tuple cannot be changed
nor the values be added to or removed from the tuple. Tuples are commonly used for small collections of values
that will not need to change, such as an IP address and port.
one_member_tuple = ('Only member',)
    or 
one_member_tuple = 'Only member', --> is considered as tuple

Dictionaries:
A dictionary in Python is a collection of key-value pairs.
Dictionaries strongly resemble JSON syntax. The native json module in the Python standard library can be used to
convert between JSON and dictionaries.

set:
A set is a collection of elements with no repeats and without insertion order but sorted order. They are used in
situations where it is only important that some things are grouped together, and not what order they were
included. For large groups of data, it is much faster to check whether or not an element is in a set than it is to do
the same for a list.

first_names = {'Adam', 'Beth', 'Charlie'}

defaultdict:
A defaultdict is a dictionary with a default value for keys, so that keys for which no value has been explicitly
defined can be accessed without errors. defaultdict is especially useful when the values in the dictionary are
collections (lists, dicts, etc) in the sense that it does not need to be initialized every time when a new key is used.
A defaultdict will never raise a KeyError. Any key that does not exist gets the default value returned.

>>> from collections import defaultdict
>>> state_capitals = defaultdict(lambda: 'Boston')


Section 1.6: IDLE - Python GUI:

Section 1.7: User Input
To get input from the user, use the input function (note: in Python 2.x, the function is called raw_input instead

Python 2.x Version ≥ 2.3
name = raw_input("What is your name? ")
# Out: What is your name? _
Security Remark Do not use input() in Python2 - the entered text will be evaluated as if it were a
Python expression (equivalent to eval(input()) in Python3), which might easily become a vulnerability.
See this article for further information on the risks of using this function.
Python 3.x Version ≥ 3.0
name = input("What is your name? ")

Note that the input is always of type str,

Section 1.8: Built in Modules and Functions
To check the built in function in python we can use dir().If called without an argument, return the names in the
current scope. Else, return an alphabetized list of names comprising (some of) the attribute of the given object, and
of attributes reachable from it.
>>> dir(__builtins__)
[
'ArithmeticError',
'AssertionError',
To know the functionality of any function, we can use built in function help .
>>> help(max)

To know all the functions in a module we can assign the functions list to a variable, and then print the variable.
>>> import math
>>> dir(math)

it seems __doc__ is useful to provide some documentation in, say, functions
GoalKicker.com – Python® Notes for Professionals 25
>>> math.__doc__
For any user defined type, its attributes, its class's attributes, and recursively the attributes of its class's base
classes can be retrieved using dir()

Section 1.9: Creating a module
A module is an importable file containing definitions and statements.
A module can be created by creating a .py file.

Functions in a module can be used by importing the module.
For modules that you have made, they will need to be in the same directory as the file that you are importing them
into. (However, you can also put them into the Python lib directory with the pre-included modules, but should be
avoided if possible.)

Modules can be aliased.
# greet.py
import hello as ai
ai.say_hello()

A module can be stand-alone runnable script.
# run_hello.py
if __name__ == '__main__':
    from hello import say_hello
    say_hello()

If the module is inside a directory and needs to be detected by python, the directory should contain a file named
__init__.py.

Section 1.10: Installation of Python 2.7.x and 3.x
Python 3 will install the Python launcher which can be used to launch Python 2.x and Python 3.x interchangeably
from the command-line:
P:\>py -3
C:\>py -2

To use the corresponding version of pip for a specific Python version, use:
C:\>py -3 -m pip -V
C:\>py -2 -m pip -V

Section 1.11: String function - str() and repr()
There are two functions that can be used to obtain a readable representation of an object.
repr(x) calls x.__repr__(): a representation of x. eval will usually convert the result of this function back to the
original object.
str(x) calls x.__str__(): a human-readable string that describes the object. This may elide some technical detail.
When writing a class, you can override these methods to do whatever you want:

Section 1.12: Installing external modules using pip
Using pip will only install packages for Python 2 and pip3 will only install packages for Python 3.

Finding / installing a package
Searching for a package is as simple as typing
$ pip search <query>
# Searches for packages whose name or summary contains <query>

When your server is behind proxy, you can install package by using below command:
$ pip --proxy http://<server address>:<port> install


Upgrading installed packages
$ pip list --outdated
$ pip install [package_name] --upgrade

Upgrading pip
py -m pip install -U pip
or
python -m pip install -U pip

Section 1.13: Help Utility
>>> help()
>>> help(help)
You can also request subclasses of modules:
help(pymysql.connections)

Close the helper with quit



"""


print(keyword.kwlist)
"""
Things are a bit different when it comes to modifying the object (in contrast to assigning the name to
a different object, which we did above) when the cascading assignment is used for mutable types. Take a look
below, and you will see it first hand
"""
x = y = [7, 8, 9]
x[0] = 13
print(y)

"""
Blocks that contain exactly one single-line statement may be put on the same line, though this form is generally not
considered good style:
"""
a = 10
b= 8
if a > b: print(a)
else: print(b)

"""
Attempting to do this with more than a single statement will not work:
if x > y: y = x
print(y) # IndentationError: unexpected indent
if x > y: while y != z: y -= 1 # SyntaxError: invalid synta

"""

"""
An empty block causes an IndentationError. Use pass (a command that does nothing) when you have a block with
no content:
"""
def will_be_implemented_later():
    pass

