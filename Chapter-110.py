"""
Chapter 110: *args and **kwargs
Section 110.1: Using **kwargs when writing functions
You can define a function that takes an arbitrary number of keyword (named) arguments by using the double star
** before a parameter name:

def print_kwargs(**kwargs):
    print(kwargs)

When calling the method, Python will construct a dictionary of all keyword arguments and make it available in the
function body:
print_kwargs(a="two", b=3)
# prints: "{a: "two", b=3}"

Note that the **kwargs parameter in the function definition must always be the last parameter, and it will only
match the arguments that were passed in after the previous ones.

def example(a, **kw):
    print kw

example(a=2, b=3, c=4) # => {'b': 3, 'c': 4}

Section 110.2: Using *args when writing functions
You can use the star * when writing a function to collect all positional (ie. unnamed) arguments in a tuple:
def print_args(farg, *args):
    print("formal arg: %s" % farg)
    for arg in args:
        print("another positional arg: %s" % arg)

Calling method:
print_args(1, "two", 3)

In that call, farg will be assigned as always, and the two others will be fed into the args tuple, in the order they were
received.

Section 110.3: Populating kwarg values with a dictionary
def foobar(foo=None, bar=None):
    return "{}{}".format(foo, bar)

values = {"foo": "foo", "bar": "bar"}

foobar(**values) # "foobar"

Section 110.4: Keyword-only and Keyword-required arguments
Python 3 allows you to define function arguments which can only be assigned by keyword, even without default
values. This is done by using star * to consume additional positional parameters without setting the keyword
parameters. All arguments after the * are keyword-only (i.e. non-positional) arguments. Note that if keyword-only
arguments aren't given a default, they are still required when calling the function.

def print_args(arg1, *args, keyword_required, keyword_only=True):
    print("first positional arg: {}".format(arg1))
    for arg in args:
        print("another positional arg: {}".format(arg))
    print("keyword_required value: {}".format(keyword_required))
    print("keyword_only value: {}".format(keyword_only))
print(1, 2, 3, 4) # TypeError: print_args() missing 1 required keyword-only argument:
    'keyword_required'
print(1, 2, 3, keyword_required=4)
# first positional arg: 1
# another positional arg: 2
# another positional arg: 3
# keyword_required value: 4
# keyword_only value: True

Section 110.5: Using **kwargs when calling functions
You can use a dictionary to assign values to the function's parameters; using parameters name as keys in the
dictionary and the value of these arguments bound to each key:

def test_func(arg1, arg2, arg3): # Usual function with three arguments
    print("arg1: %s" % arg1)
    print("arg2: %s" % arg2)
    print("arg3: %s" % arg3)

# Note that dictionaries are unordered, so we can switch arg2 and arg3. Only the names matter.
kwargs = {"arg3": 3, "arg2": "two"}
# Bind the first argument (ie. arg1) to 1, and use the kwargs dictionary to bind the others
test_var_args_call(1, **kwargs)


Section 110.6: **kwargs and default values
To use default values with **kwargs
def fun(**kwargs):
    print kwargs.get('value', 0)

fun()
# print 0
fun(value=1)
# print 1

Section 110.7: Using *args when calling functions
The effect of using the * operator on an argument when calling a function is that of unpacking the list or a tuple
argument

def print_args(arg1, arg2):
    print(str(arg1) + str(arg2))

a = [1,2]
b = tuple([3,4])
print_args(*a)
# 12
print_args(*b)
# 34

Note that the length of the starred argument need to be equal to the number of the function's arguments.
A common python idiom is to use the unpacking operator * with the zip function to reverse its effects:
a = [1,3,5,7,9]
b = [2,4,6,8,10]
zipped = zip(a,b)
# [(1,2), (3,4), (5,6), (7,8), (9,10)]
zip(*zipped)
# (1,3,5,7,9), (2,4,6,8,10)



"""