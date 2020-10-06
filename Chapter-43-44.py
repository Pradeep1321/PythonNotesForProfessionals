"""
Chapter 43: Importing modules

Section 43.1: Importing a module

Use the import statement:
import random
print(random.randint(1, 10))

import module will import a module and then allow you to reference its objects -- values, functions and classes, for
example -- using the module.name syntax. In the above example, the random module is imported, which contains the
randint function. So by importing random you can call randint with random.randint.

You can import a module and assign it to a different name

import random as rn

print(rn.randint(1, 10))

If your python file main.py is in the same folder as custom.py. You can import it like this:
import custom

It is also possible to import a function from a module:

from math import sin
sin(1)

To import specific functions deeper down into a module, the dot operator may be used only on the left side of the
import keyword:

from urllib.request import urlopen

In python, we have two ways to call function from top level. One is import and another is from. We should use
import when we have a possibility of name collision. Suppose we have hello.py file and world.py files having same
function named function. Then import statement will work good

Multiple imports can be made on the same line:
>>> # Multiple modules
>>> import time, sockets, random
>>> # Multiple functions
>>> from math import sin, cos, tan
>>> # Multiple constants
>>> from math import pi, e

>>> from urllib.request import urlopen as geturl, pathname2url as path2url, getproxies
>>> from math import factorial as fact, gamma, atan as arctan
>>> import random.randint, time, sys

Section 43.2: The __all__ special variable
Modules can have a special variable named __all__ to restrict what variables are imported when using from
mymodule import *.

Given the following module:
# mymodule.py
__all__ = ['imported_by_star']

imported_by_star = 42
not_imported_by_star = 21

Only imported_by_star is imported when using from mymodule import *:
>>> from mymodule import *
>>> imported_by_star
42
>>> not_imported_by_star
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'not_imported_by_star' is not defined

However, not_imported_by_star can be imported explicitly:
>>> from mymodule import not_imported_by_star
>>> not_imported_by_star
21

Section 43.3: Import modules from an arbitrary filesystem location
If you want to import a module that doesn't already exist as a built-in module in the Python Standard Library nor as
a side-package, you can do this by adding the path to the directory where your module is found to sys.path. This
may be useful where multiple python environments exist on a host

import sys
sys.path.append("/path/to/directory/containing/your/module")
import mymodule

It is important that you append the path to the directory in which mymodule is found, not the path to the module
itself.

Section 43.4: Importing all names from a module
from module_name import *
from math import *
sqrt(2) # instead of math.sqrt(2)
ceil(2.7) # instead of math.ceil(2.7)

This will import all names defined in the math module into the global namespace, other than names that begin with
an underscore (which indicates that the writer feels that it is for internal use only).

Warning: If a function with the same name was already defined or imported, it will be overwritten. Almost always
importing only specific names from math import sqrt, ceil is the recommended way:

Starred imports are only allowed at the module level. Attempts to perform them in class or function definitions
result in a SyntaxError.

Section 43.5: Programmatic importing
Python 2.x Version ≥ 2.7
To import a module through a function call, use the importlib module (included in Python starting in version 2.7):

import importlib
random = importlib.import_module("random")

The importlib.import_module() function will also import the submodule of a package directly:

collections_abc = importlib.import_module("collections.abc")

For older versions of Python, use the imp module.
Python 2.x Version ≤ 2.7
Use the functions imp.find_module and imp.load_module to perform a programmatic import.

Do NOT use __import__() to programmatically import modules! There are subtle details involving sys.modules,
the fromlist argument, etc. that are easy to overlook which importlib.import_module() handles for you.

Section 43.6: PEP8 rules for Imports

1. Imports should be on separate lines:
        from math import sqrt, ceil     # Not recommended
        from math import sqrt           # Recommended
        from math import ceil


2. Order imports as follows at the top of the module:
        Standard library imports
        Related third party imports
        Local application/library specific imports

3. Wildcard imports should be avoided as it leads to confusion in names in the current namespace. If you do
from module import *, it can be unclear if a specific name in your code comes from module or not. This is
doubly true if you have multiple from module import *-type statements

4. Avoid using relative imports; use explicit imports instead


Section 43.7: Importing specific names from a module
Instead of importing the complete module you can import only specified names

from random import randint # Syntax "from MODULENAME import NAME1[, NAME2[, ...]]"

from random is needed, because the python interpreter has to know from which resource it should import a
function or class and import randint specifies the function or class itself.


The following example will raise an error, because we haven't imported a module:
random.randrange(1, 10) # works only if "import random" has been run before

The python interpreter does not understand what you mean with random. It needs to be declared by adding import
random to the example:
import random
random.randrange(1, 10)

Section 43.8: Importing submodules

from module.submodule import function   #This imports function from module.submodule.

Section 43.9: Re-importing a module
the interpreter registers every module you import. And when you try to reimport a module, the
interpreter sees it in the register and does nothing. So the hard way to reimport is to use import after removing the
corresponding item from the register:

Python 2
        Use the reload function:

Python 3
The reload function has moved to importlib
from importlib import reload

Section 43.10: __import__() function

The __import__() function can be used to import modules where the name is only known at runtime
if user_input == "os":
    os = __import__("os") # equivalent to import os

This function can also be used to specify the file path to a module
mod = __import__(r"C:/path/to/file/anywhere/on/computer/module.py")

Chapter 44: Dierence between Module and Package

Section 44.1: Modules

A module is a single Python file that can be imported.

Section 44.2: Packages
A package is made up of multiple Python files (or modules), and can even include libraries written in C or C++.
Instead of being a single file, it is an entire folder structure which might look like this:

All Python packages must contain an __init__.py file. When you import a package in your script (import package),
the __init__.py script will be run, giving you access to the all of the functions in the package





"""