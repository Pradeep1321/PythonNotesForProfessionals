"""
Chapter 2: Python Data Types

Section 2.1: String Data Type
Python allows for either pairs of single or double quotes. Strings are immutable sequence data type, i.e each time one
makes any changes to a string, completely new string object is created.

Section 2.2: Set Data Types
Sets are unordered collections of unique objects, there are two types of set:
1. Sets - They are mutable and new elements can be added once sets are defined
2. Frozen Sets - They are immutable and new elements cannot added after its defined.

Section 2.3: Numbers data type
Numbers have four types in Python. Int, float, complex, and long.
int_num = 10 #int value
float_num = 10.2 #float value
complex_num = 3.14j #complex value
long_num = 1234567L #long value

Section 2.4: List Data Type
lists are almost similar to arrays in C. One difference is that all the items belonging to a list can be of different
 data type.

Section 2.5: Dictionary Data Type
Dictionary consists of key-value pairs. It is enclosed by curly braces {} and values can be assigned and accessed
using square brackets[].

Section 2.6: Tuple Data Type
Lists are enclosed in brackets [ ] and their elements and size can be changed, while tuples are enclosed in
parentheses ( ) and cannot be updated. Tuples are immutable.

Chapter 3: Indentation
Section 3.1: Simple example
#If a function is not indented to the same level it will not be considers as part of the parent class

Spaces or Tabs?
The recommended indentation is 4 spaces but tabs or spaces can be used so long as they are consistent. Do not
mix tabs and spaces in Python as this will cause an error in Python 3 and can causes errors in Python 2.

Section 3.2: How Indentation is Parsed
Whitespace is handled by the lexical analyzer before being parsed.

Section 3.3: Indentation Errors
The spacing should be even and uniform throughout. Improper indentation can cause an IndentationError or
cause the program to do something unexpected

Chapter 4: Comments and Documentation
Section 4.1: Single line, inline and multiline comments

Single-line comments begin with the hash character (#) and are terminated by the end of line.
Single line comment:
# This is a single line comment in Python
Inline comment:
print("Hello World") # This line prints "Hello World"
Comments spanning multiple lines have \""" or ''' on either end. This is the same as a multiline string, but
they can be used as comments:

Section 4.2: Programmatically accessing docstrings

Docstrings are - unlike regular comments - stored as an attribute of the function they document, meaning that you
can access them programmatically.
An example function
def func():
    """This is a function that does nothing at all"""
    return
The docstring can be accessed using the __doc__ attribute:
print(func.__doc__)


Advantages of docstrings over regular comments
Just putting no docstring or a regular comment in a function makes it a lot less helpful.
def greet(name, greeting="Hello"):
    # Print a greeting to the user `name`
    # Optional parameter `greeting` can change what they're greeted with.
    print("{} {}".format(greeting, name))
print(greet.__doc__)
    None

Section 4.3: Write documentation using docstrings
A docstring is a multi-line comment used to document modules, classes, functions and methods. It has to be the
first statement of the component it describes.

Syntax conventions:
PEP 257:
PEP 257 defines a syntax standard for docstring comments

Sphinx:
Sphinx is a tool to generate HTML based documentation for Python projects based on docstrings. Its markup
language used is reStructuredText. They define their own standards for documentation, pythonhosted.org hosts a
very good description of them. The Sphinx format is for example used by the pyCharm IDE.

Google Python Style Guide:
Google has published Google Python Style Guide which defines coding conventions for Python, including
documentation comments.    

Using the Napoleon plugin, Sphinx can also parse documentation in the Google Style Guide-compliant format.


"""