'''
Parameter   Details
f           The function to be decorated (wrapped)
Decorator functions are software design patterns. They dynamically alter the functionality of a function, method, or
class without having to directly use subclasses or change the source code of the decorated function.

Section 37.1: Decorator function
Decorators augment the behavior of other functions or methods. Any function that takes a function as a parameter
and returns an augmented function can be used as a decorator.

Decorator function takes function as arguments and should return the function. It will give error if the return is not a
 function.

This is also called metaprogramming as a part of the program tries to modify another part of the program at compile time.

Any object which implements the specuial method __call__() is termed callable

Section 37.2: Decorator class
The syntax would still work, except that now my_func gets replaced with an instance
of the decorator class. If this class implements the __call__() magic method, then it would still be possible to use
my_func as if it was a function:

Note that a function decorated with a class decorator will no longer be considered a "function" from type-checking
perspective:

Decorating Methods
For decorating methods you need to define an additional __get__-method:

Class Decorators only produce one instance for a specific function so decorating a method with a class decorator
will share the same decorator between all instances of that class:

Section 37.3: Decorator with arguments (decorator factory)
A decorator takes just one argument: the function to be decorated. There is no way to pass other arguments.
But additional arguments are often desired. The trick is then to make a function which takes arbitrary arguments
and returns a decorator.

Section 37.4: Making a decorator look like the decorated function
Decorators normally strip function metadata as they aren't the same. This can cause problems when using metaprogramming
to dynamically access function metadata. Metadata also includes function's docstrings and its name.
functools.wraps makes the decorated function look like the original function by copying several attributes to the
wrapper function.


Section 37.5: Using a decorator to time a function

Section 37.6: Create singleton class with a decorator
A singleton is a pattern that restricts the instantiation of a class to one instance/object. Using a decorator, we can
define a class as a singleton by forcing the class to either return an existing instance of the class or create a new
instance (if it doesn't exist).

'''

import types
from types import MethodType
from functools import wraps

#This is the decorator
def print_args(func):
    def inner_func(*args, **kwargs):
        print(args)
        print(kwargs)
        return func(*args, **kwargs) #Call the original function with its arguments.
    return inner_func

@print_args
def multiply(num_a, num_b):
    return num_a * num_b

print(multiply(3, 5))

# Class Decorator , Class should ahve __call__ function
class Decorator(object):
    """Simple decorator class."""
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print('Before the function call.')
        res = self.func(*args, **kwargs)
        print('After the function call.')
        return res
    def __get__(self, instance, cls):
        # Return a Method if it is called on an instance
        return self if instance is None else MethodType(self, instance)

@Decorator
def testfunc():
    print('Inside the function.')

testfunc()

isinstance(testfunc, types.FunctionType)
type(testfunc)

#Decorating Methods
#For decorating methods you need to define an additional __get__-method:

class Test(object):
    @Decorator
    def __init__(self):
        print("method decorator")
        pass
a = Test()

#Class Decorators only produce one instance for a specific function so decorating a method with a class decorator
#will share the same decorator between all instances of that class:

class CountCallsDecorator(object):
    def __init__(self, func):
        self.func = func
        self.ncalls = 0 # Number of calls of this method
    def __call__(self, *args, **kwargs):
        self.ncalls += 1 # Increment the calls counter
        return self.func(*args, **kwargs)
    def __get__(self, instance, cls):
        return self if instance is None else MethodType(self, instance)

class Test(object):
    def __init__(self):
        pass
    @CountCallsDecorator
    def do_something(self):
        return 'something was done'

a = Test()
a.do_something()
a.do_something.ncalls # 1
b = Test()
b.do_something()
b.do_something.ncalls # 2

# Decorator with argument for methods
def decoratorfactory(message):
    def decorator(func):
        def wrapped_func(*args, **kwargs):
            print('The decorator wants to tell you: {}'.format(message))
            return func(*args, **kwargs)
        return wrapped_func
    return decorator

@decoratorfactory('Hello World')
def test():
    pass
test()

#Decorator classes with arguments
def decoratorfactory(*decorator_args, **decorator_kwargs):
    class Decorator(object):
        def __init__(self, func):
            self.func = func
        def __call__(self, *args, **kwargs):
                print('Inside the decorator with arguments {}'.format(decorator_args))
                return self.func(*args, **kwargs)
    return Decorator

@decoratorfactory(10)
def test():
    pass
test()

#37.4
#The two methods of wrapping a decorator are achieving the same thing in hiding that the original function has
#been decorated. There is no reason to prefer the function version to the class version unless you're already using
#one over the other.

#As a function
def decorator(func):
    # Copies the docstring, name, annotations and module to the decorator
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapped_func

@decorator
def test():
    pass

test.__name__

#As a class
class Decorator(object):
    def __init__(self, func):
        # Copies name, module, annotations and docstring to the instance.
        self._wrapped = wraps(func)(self)
    def __call__(self, *args, **kwargs):
        return self._wrapped(*args, **kwargs)

@Decorator
def test():
    """Docstring of test."""
    pass

test.__doc__

#Section 37.5: Using a decorator to time a function
import time
def timer(func):
    def inner(*args, **kwargs):
        t1 = time.time()
        f = func(*args, **kwargs)
        t2 = time.time()
        print ('Runtime took {0} seconds'.format(t2-t1))
        return f
    return inner

@timer
def example_function():
    #do stuff
    pass

example_function()

#Section 37.6: Create singleton class with a decorator
#So it doesn't matter whether you refer to the class instance via your local variable or whether you create another
#"instance", you always get the same object
def singleton(cls):
    instance = [None]
    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]
    return wrapper

@singleton
class SomeSingletonClass:
    x = 2
    def __init__(self):
        print("Created!")

instance = SomeSingletonClass() # prints: Created!
instance1 = SomeSingletonClass() # doesn't print anything
print(instance.x) # 2
instance.x = 3
print(SomeSingletonClass().x) # 3
