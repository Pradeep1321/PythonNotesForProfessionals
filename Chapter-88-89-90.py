"""
Chapter 88: Exceptions
exceptions have a rich type hierarchy, all inheriting from the BaseException type.

Section 88.1: Catching Exceptions
Use try...except: to catch exceptions.
try:
    x = 5 / 0
except ZeroDivisionError as e:
    # `e` is the exception object
    print("Got a divide by zero! The exception was:", e)
    # handle exceptional case
    x = 0
finally:
    print "The END"
    # it runs no matter what execute


For example, ZeroDivisionError is a subclass of ArithmeticError:
>> ZeroDivisionError.__bases__
(<class 'ArithmeticError'>,)

Section 88.2: Do not catch everything!
    except Exception:

    Or even everything (that includes BaseException and all its children including Exception):
    except:

If you're catching every error, you won't know what error occurred or how to fix it.
This is more commonly referred to as 'bug masking' and should be avoided

Section 88.3: Re-raising exceptions
simply use the raise statement with no parameters to catch an exception just to inspect it, e.g. for logging purposes
try:
    5 / 0
except ZeroDivisionError:
    print("Got an error")
    raise

#better
try:
    5 / 0
except ZeroDivisionError as e:
    raise ZeroDivisionError("Got an error", e)

But this has the drawback of reducing the exception trace to exactly this raise while the raise without argument
retains the original exception trace.

In Python 3 you can keep the original stack by using the raise-from syntax:

raise ZeroDivisionError("Got an error") from e


Section 88.4: Catching multiple exceptions

try:
   #code
except (KeyError, AttributeError) as e:
    print("A KeyError or an AttributeError exception has been caught.")
or
try:
    Code
except KeyError as e:
    print("A KeyError has occurred. Exception message:", e)
except AttributeError as e:
    print("An AttributeError has occurred. Exception message:", e)


Section 88.5: Exception Hierarchy
Exception handling occurs based on an exception hierarchy, determined by the inheritance structure of the
exception classes.

For example, IOError and OSError are both subclasses of EnvironmentError. Code that catches an IOError will not
catch an OSError. However, code that catches an EnvironmentError will catch both IOErrors and OSErrors.

The hierarchy of built-in exceptions:
Python 2.x Version ≥ 2.3
BaseException
+-- SystemExit
+-- KeyboardInterrupt
+-- GeneratorExit
+-- Exception
+-- StopIteration
+-- StandardError
| +-- BufferError
| +-- ArithmeticError
| | +-- FloatingPointError
| | +-- OverflowError
| | +-- ZeroDivisionError
| +-- AssertionError
| +-- AttributeError
| +-- EnvironmentError
| | +-- IOError
| | +-- OSError
| | +-- WindowsError (Windows)
| | +-- VMSError (VMS)
| +-- EOFError
| +-- ImportError
| +-- LookupError
| | +-- IndexError
| | +-- KeyError
| +-- MemoryError
| +-- NameError
| | +-- UnboundLocalError
| +-- ReferenceError
| +-- RuntimeError
| | +-- NotImplementedError
| +-- SyntaxError
| | +-- IndentationError
| | +-- TabError
| +-- SystemError
| +-- TypeError
| +-- ValueError
| +-- UnicodeError
| +-- UnicodeDecodeError
| +-- UnicodeEncodeError
| +-- UnicodeTranslateError
+-- Warning
+-- DeprecationWarning
+-- PendingDeprecationWarning
+-- RuntimeWarning
+-- SyntaxWarning
+-- UserWarning
+-- FutureWarning
+-- ImportWarning
+-- UnicodeWarning
+-- BytesWarning

Python 3.x Version ≥ 3.0
BaseException
+-- SystemExit
+-- KeyboardInterrupt
+-- GeneratorExit
+-- Exception
+-- StopIteration
+-- StopAsyncIteration
+-- ArithmeticError
| +-- FloatingPointError
| +-- OverflowError
| +-- ZeroDivisionError
+-- AssertionError
+-- AttributeError
+-- BufferError
+-- EOFError
+-- ImportError
+-- LookupError
| +-- IndexError
| +-- KeyError
+-- MemoryError
+-- NameError
| +-- UnboundLocalError
+-- OSError
| +-- BlockingIOError
| +-- ChildProcessError
| +-- ConnectionError
| | +-- BrokenPipeError
| | +-- ConnectionAbortedError
| | +-- ConnectionRefusedError
| | +-- ConnectionResetError
| +-- FileExistsError
| +-- FileNotFoundError
| +-- InterruptedError
| +-- IsADirectoryError
| +-- NotADirectoryError
| +-- PermissionError
| +-- ProcessLookupError
| +-- TimeoutError
+-- ReferenceError
+-- RuntimeError
| +-- NotImplementedError
| +-- RecursionError
+-- SyntaxError
| +-- IndentationError
| +-- TabError
+-- SystemError
+-- TypeError
+-- ValueError
| +-- UnicodeError
| +-- UnicodeDecodeError
| +-- UnicodeEncodeError
| +-- UnicodeTranslateError
+-- Warning
+-- DeprecationWarning
+-- PendingDeprecationWarning
+-- RuntimeWarning
+-- SyntaxWarning
+-- UserWarning
+-- FutureWarning
+-- ImportWarning
+-- UnicodeWarning
+-- BytesWarning
+-- ResourceWarning


Section 88.6: Else
Code in an else block will only be run if no exceptions were raised by the code in the try block. This is useful if you
have some code you don’t want to run if an exception is thrown, but you don’t want exceptions thrown by that
code to be caught.

Note that this kind of else: cannot be combined with an if starting the else-clause to an elif. If you have a
following if it needs to stay indented below that else::

try:
    ...
except ...:
    ...
else:
    if ...:
        ...
    elif ...:
        ...
    else:
        ...

Section 88.7: Raising Exceptions
If your code encounters a condition it doesn't know how to handle, such as an incorrect parameter, it should raise
the appropriate exception.

def even_the_odds(odds):
    if odds % 2 != 1:
        raise ValueError("Did not get an odd number")
    return odds + 1


Section 88.8: Creating custom exception types
Create a class inheriting from Exception:

Section 88.9: Practical examples of exception handling
d = [{7: 3}, {25: 9}, {38: 5}]
for i in range(len(d)):
    do_stuff(i)
    try:
       dic = d[i]
      i += dic[i]
    except KeyError:
      i += 1

A KeyError will be raised when you try to get a value from a dictionary for a key that doesn’t exist.

Section 88.10: Exceptions are Objects too
A Python script can use the raise statement to interrupt execution, causing Python to print a stack trace of the call
stack at that point and a representation of the exception instance.

You can get hold of the exception objects by assigning them in the except... part of the exception handling code:

Section 88.11: Running clean-up code with finally
The finally block of a try clause will happen regardless of whether any exceptions were raised.
resource = allocate_some_expensive_resource()
try:
    do_stuff(resource)
except SomeException as e:
    log_error(e)
    raise # re-raise the error
finally:
    free_expensive_resource(resource)

This pattern is often better handled with context managers (using the with statement).

Section 88.12: Chain exceptions with raise from
In the process of handling an exception, you may want to raise another exception.

Python 3.x Version ≥ 3.0
You can chain exceptions to show how the handling of exceptions proceeded:
try:
    5 / 0
except ZeroDivisionError as e:
    raise ValueError("Division failed") from e

Chapter 89: Raise Custom Errors / Exceptions
This exception class has to be derived, either
directly or indirectly, from Exception class. Most of the built-in exceptions are also derived from this class.

Section 89.1: Custom Exception

class CustomError(Exception):
    pass

x = 1
if x == 1:
    raise CustomError('This is custom error')

Section 89.2: Catch custom Exception
try:
    raise CustomError('Can you catch me ?')
except CustomError as e:
    print ('Catched CustomError :{}'.format(e))
except Exception as e:
    print ('Generic exception: {}'.format(e))

Chapter 90: Commonwealth Exceptions
Section 90.1: Other Errors
AssertError
The assert statement exists in almost every programming language. When you do:

assert condition
or:
assert condition, message
It's equivalent to this:
if __debug__:
    if not condition: raise AssertionError(message)

Note: the built-in variable debug is True under normal circumstances, False when optimization is requested
(command line option -O). Assignments to debug are illegal. The value for the built-in variable is determined when
the interpreter starts.

KeyboardInterrupt
Error raised when the user presses the interrupt key, normally Ctrl + C or del .

ZeroDivisionError
You tried to calculate 1/0 which is undefined.

Section 90.2: NameError: name '???' is not defined
Is raised when you tried to use a variable, method or function that is not initialized (at least not before).

Python scopes and the LEGB Rule:
The so-called LEGB Rule talks about the Python scopes. Its name is based on the different scopes, ordered by the
correspondent priorities:
Local → Enclosed → Global → Built-in.

Local: Variables not declared global or assigned in a function.
Enclosing: Variables defined in a function that is wrapped inside another function.
Global: Variables declared global, or assigned at the top-level of a file.
Built-in: Variables preassigned in the built-in names module.


Section 90.3: TypeErrors

These exceptions are caused when the type of some object should be different
TypeError: [definition/method] takes ? positional arguments but ? was given

Section 90.4: Syntax Error on good code

The gross majority of the time a SyntaxError which points to an uninteresting line means there is an issue on the
line before it

Section 90.5: IndentationErrors (or indentation SyntaxErrors)
IndentationError/SyntaxError: unexpected indent
This exception is raised when the indentation level increases with no reason.

IndentationError/SyntaxError: unindent does not match any outer indentation level

IndentationError: expected an indented block

IndentationError: expected an indented block

IndentationError: inconsistent use of tabs and spaces in indentation
How to avoid this error
Don't use tabs. It is discouraged by PEP8, the style guide for Python.
1. Set your editor to use 4 spaces for indentation.
2. Make a search and replace to replace all tabs with 4 spaces.
3. Make sure your editor is set to display tabs as 8 spaces, so that you can realize easily that error and fix it.


"""

#Section 88.6: Else
print("---Section 88.6: Else------")
try:
    data = {1: 'one', 2: 'two'}
    print(data[1])
except KeyError as e:
    print('key not found')
else:
    print("ValuError is printed and gives error")
    #raise ValueError()

#Section 88.8: Creating custom exception types
print("-----Section 88.8: Creating custom exception types-------")

class FooException(Exception):
    pass
try:
    raise FooException("insert description here")
except FooException:
    print("A FooException was raised.")

class NegativeError(ValueError):
    pass

def foo(x):
    # function that only accepts positive values of x
    if x < 0:
        raise NegativeError("Cannot process negative numbers") # rest of function body
try:
    result = foo(int(input("Enter a positive integer: "))) # raw_input in Python 2.x
except NegativeError:
    print("You entered a negative number!")
else:
    print("The result was " + str(result))
