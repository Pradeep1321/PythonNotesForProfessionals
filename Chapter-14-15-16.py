''''
Chapter 14: Conditionals
Section 14.1: Conditional Expression (or "The Ternary Operator")

The ternary operator is used for inline conditional expressions. It is best used in simple, concise operations that are
easily read.
if the conditional expression is True, then it will evaluate  to the expression on the left side, otherwise, the right side.
n = 5
"Hello" if n > 10 else "Goodbye" if n > 5 else "Good day"

Section 14.3: Truth Values
The following values are considered falsey, in that they evaluate to False when applied to a boolean operator.
None
False
0, or any numerical value equivalent to zero, for example 0L, 0.0, 0j
Empty sequences: '', "", (), []
Empty mappings: {}
User-defined types where the __bool__ or __len__ methods return 0 or False

All other values in Python evaluate to True.

Section 14.4: Boolean Logic Expressions

And operator
The and operator evaluates all expressions and returns the last expression if all expressions evaluate to True.
Otherwise it returns the first value that evaluates to False:
>>> 1 and 2
2
>>> 1 and 0
0
>>> 1 and "Hello World"
"Hello World"
>>> "" and "Pancakes"
""
Or operator
The or operator evaluates the expressions left to right and returns the first value that evaluates to True or the last
value (if none are True).
>>> 1 or 2
1
>>> None or 1
1
>>> 0 or []
[]

Section 14.5: Using the cmp function to get the comparison result of two objects:

Python 2 includes a cmp function which allows you to determine if one object is less than, equal to, or greater than
another object. This function can be used to pick a choice out of a list based on one of those three options.
Suppose you need to print 'greater than' if x > y, 'less than' if x < y and 'equal' if x == y.
['equal', 'greater than', 'less than', ][cmp(x,y)]

This function is removed on Python 3. You can use the cmp_to_key(func) helper function located in functools in
Python 3 to convert old comparison functions to key functions.

Section 14.6: Else statement

Section 14.7: Testing if an object is None and assigning it
aDate=aDate or datetime.date.today()
This does a Short Circuit evaluation. If aDate is initialized and is not None, then it gets assigned to itself with no net
effect. If it is None, then the datetime.date.today() gets assigned to aDate.


Section 14.8: If statement


Chapter 15: Comparisons

Section 15.1: Chain Comparisons
You can compare multiple items with multiple comparison operators with chain comparison. For example
x > y > z
is just a short form of:
x > y and y > z

Side effects
As soon as one comparison returns False, the expression evaluates immediately to False, skipping all remaining
comparisons.
Note that the expression exp in a > exp > b will be evaluated only once, whereas in the case of
a > exp and exp > b
exp will be computed twice if a > exp is true.

Section 15.2: Comparison by `is` vs `==`
A common pitfall is confusing the equality comparison operators is and ==.

a == b compares the value of a and b.
a is b will compare the identities of a and b.

Basically, is can be thought of as shorthand for id(a) == id(b).
You should use is to test for None:
    if myvar is not None:

A use of is is to test for a “sentinel” (i.e. a unique object).
sentinel = object()
def myfunc(var=sentinel):
    GoalKicker.com – Python® Notes for Professionals 85
    if var is sentinel:
        # value wasn’t provided
        pass
    else:
        # value was provided
        pass

Section 15.3: Greater than or less than:
For strings they will compare lexicographically, which is similar to alphabetical order but not quite the same.
In these comparisons, lowercase letters are considered 'greater than' uppercase,

Section 15.4: Not equal to
Section 15.5: Equal To

Section 15.6: Comparing Objects
Note that this simple comparison assumes that other (the object being compared to) is the same object type.
Comparing to another type will throw an error:
Checking isinstance() or similar will help prevent this (if desired).

Chapter 16: Loops:
Section 16.1: Break and Continue in Loops
break statement
When a break statement executes inside a loop, control flow "breaks" out of the loop immediately:
continue statement
A continue statement will skip to the next iteration of the loop bypassing the rest of the current block but
continuing the loop. As with break, continue can only appear inside loops:
Nested Loops
break and continue only operate on a single level of loop.
Use return from within a function as a break
The return statement exits from a function, without executing the code that comes after it.

Section 16.2: For loops
for loops iterate over a collection of items, such as list or dict, and run a block of code with each element from
the collection.


Iteration is a general term for taking each item of something, one after another. Any time you use a loop, explicit or implicit, to go over a group of items, that is iteration.

In Python, iterable and iterator have specific meanings.

An iterable is an object that has an __iter__ method which returns an iterator, or which defines a __getitem__ method that can take sequential indexes starting from zero (and raises an IndexError when the indexes are no longer valid). So an iterable is an object that you can get an iterator from.

An iterator is an object with a next (Python 2) or __next__ (Python 3) method.

Whenever you use a for loop, or map, or a list comprehension, etc. in Python, the next method is called automatically to get each item from the iterator, thus going through the process of iteration.

for loop can iterate on any iterable object which is an object which defines a __getitem__ or a __iter__ function.
The __iter__ function returns an iterator, which is an object with a next function that is used to access the next
element of the iterable.

Section 16.3: Iterating over lists
If you want to loop though both the elements of a list and have an index for the elements as well, you can use
Python's enumerate function

enumerate will generate tuples, which are unpacked into index (an integer) and item (the actual value from the list).
The above loop will print

Iterate over a list with value manipulation using map and lambda, i.e. apply lambda function on each element in the list:
Iterate over a list with value manipulation using map and lambda, i.e. apply lambda function on each element in the
list:
x = map(lambda e : e.upper(), ['one', 'two', 'three', 'four'])
print(x)
Output:
['ONE', 'TWO', 'THREE', 'FOUR'] # Python 2.x
NB: in Python 3.x map returns an iterator instead of a list so you in case you need a list you have to cast the result

Section 16.4: Loops with an "else" clause
The for and while compound statements (loops) can optionally have an else clause (in practice, this usage is fairly
rare).
The else clause only executes after a for loop terminates by iterating to completion, or after a while loop
terminates by its conditional expression becoming false.
for i in range(3):
    print(i)
else:
    print('done')

Section 16.5: The Pass Statement
pass is a null statement for when a statement is required by Python syntax (such as within the body of a for or
while loop), but no action is required or desired by the programmer.

Section 16.6: Iterating over dictionaries
To iterate through its keys and values, use:
for key, value in d.items():
    print(key, "::", value)
Note that in Python 2, .keys(), .values() and .items() return a list object. If you simply need to iterate through
the result, you can use the equivalent .iterkeys(), .itervalues() and .iteritems().
The difference between .keys() and .iterkeys(), .values() and .itervalues(), .items() and .iteritems() is
that the iter* methods are generators. Thus, the elements within the dictionary are yielded one by one as they are
evaluated. When a list object is returned, all of the elements are packed into a list and then returned for further
evaluation.

Section 16.7: The "half loop" do-while Unlike other:

Section 16.8: Looping and Unpacking
collection = [('a', 'b', 'c'), ('x', 'y', 'z'), ('1', '2', '3')]
You can simply do this:
for i1, i2, i3 in collection:
    # logic
This will also work for most types of iterables, not just tuples.

Section 16.9: Iterating dierent portion of a list with dierent step size:

Section 16.10: While Loop

'''




# Ternary
n = 10
print("Hello") if n > 10 else print("Goodbye") if n > 5 else print("Good day")
# the above statement in  if else
if n > 10:
    print("Hello")
elif n > 5:
    print("goodbye")
else:
    print("Good day")

# IS operator behavior
#Beyond this, there are quirks of the run-time environment that further complicate things. Short strings and small
#integers will return True when compared with is, due to the Python machine attempting to use less memory for
#identical objects.
a = 'short'
b = 'short'
c = 5
d = 5
print(a is b) # True
print(c is d) # True
#But longer strings and larger integers will be stored separately.
a = 'not so short'
b = 'not so short'
c = 1000
d = 1000
print(a is b) # False
print(c is d) # False

#enumerate will generate tuples
for index, item in enumerate(['one', 'two', 'three', 'four']):
    print(index, '::', item)

# map list
x = map(lambda e : e.upper(), ['one', 'two', 'three', 'four'])
print(list(x))

print("For and While having else")
for i in range(3):
    print(i)
else:
    print('done')

i = 0

while i < 3:
    print(i)
    i += 1
else:
    print('done')