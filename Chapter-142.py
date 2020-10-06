"""
Chapter 142: Accessing Python source code and bytecode
Section 142.1: Display the bytecode of a function
The Python interpreter compiles code to bytecode before executing it on the Python's virtual machine
import dis
def fib(n):
    if n <= 2: return 1
        return fib(n-1) + fib(n-2)
# Display the disassembled bytecode of the function.
dis.dis(fib)

The function dis.dis in the dis module will return a decompiled bytecode of the function passed to it.

Section 142.2: Display the source code of an object
To print the source code of a Python object use inspect. Note that this won't work for built-in objects nor for
objects defined interactively.

import random
import inspect
print(inspect.getsource(random.randint))

To just print the documentation string
print(inspect.getdoc(random.randint))

Print full path of the file where the method random.randint is defined:
print(inspect.getfile(random.randint))

print(random.randint.__code__.co_filename) # equivalent to the above

Objects defined interactively
If an object is defined interactively inspect cannot provide the source code but you can use
dill.source.getsource instead

# define a new function in the interactive shell
def add(a, b):
    return a + b
print(add.__code__.co_filename) # Output: <stdin>

import dill
print dill.source.getsource(add)
# def add(a, b):
    return a + b


Built-in objects

The source code for Python's built-in functions is written in c and can only be accessed by looking at the Python's
source code (hosted on Mercurial or downloadable from https://www.python.org/downloads/source/).

print(inspect.getsource(sorted)) # raises a TypeError
type(sorted) # <class 'builtin_function_or_method'>

Section 142.3: Exploring the code object of a function

CPython allows access to the code object for a function object

The __code__object contains the raw bytecode (co_code) of the function as well as other information such as
constants and variable names.



"""