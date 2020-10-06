"""
Chapter 111: Garbage Collection
Section 111.1: Reuse of primitive objects
>> import sys
>> sys.getrefcount(1)
797
>> a = 1
>> b = 1
>> sys.getrefcount(1)
799

>> a = 999999999
>> sys.getrefcount(999999999)
3
>> b = 999999999
>> sys.getrefcount(999999999)
3

Note that the refcount increases, meaning that a and b reference the same underlying object when they refer to the
1 primitive. However, for larger numbers, Python actually doesn't reuse the underlying object:
Because the refcount for 999999999 does not change when assigning it to a and b we can infer that they refer to
two different underlying objects, even though they both are assigned the same primitive.

Section 111.2: Eects of the del command

Removing a variable name from the scope using del v, or removing an object from a collection using del v[item]
or del[i:j], or removing an attribute using del v.name, or any other way of removing references to an object, does
not trigger any destructor calls or any memory being freed in and of itself. Objects are only destructed when their
reference count reaches zero.


Section 111.3: Reference Counting
The vast majority of Python memory management is handled with reference counting
Every time an object is referenced (e.g. assigned to a variable), its reference count is automatically increased. When
it is dereferenced (e.g. variable goes out of scope), its reference count is automatically decreased.
When the reference count reaches zero, the object is immediately destroyed and the memory is immediately
freed. Thus for the majority of cases, the garbage collector is not even needed.

Section 111.4: Garbage Collector for Reference Cycles
The only time the garbage collector is needed is if you have a reference cycle.The simples example of a reference
cycle is one in which A refers to B and B refers to A, while nothing else refers to either A or B. Neither A or B are
accessible from anywhere in the program, so they can safely be destructed, yet their reference counts are 1 and so
they cannot be freed by the reference counting algorithm alone.

Section 111.5: Forcefully deallocating objects
You can force deallocate objects even if their refcount isn't 0 in both Python 2 and 3.
Both versions use the ctypes module to do so.
WARNING: doing this will leave your Python environment unstable and prone to crashing without a traceback!
Using this method could also introduce security problems (quite unlikely) Only deallocate objects you're sure you'll
never reference again. Ever.

Python 3.x Version ≥ 3.0
import ctypes
deallocated = 12345
ctypes.pythonapi._Py_Dealloc(ctypes.py_object(deallocated))

Python 2.x Version ≥ 2.3
import ctypes, sys
deallocated = 12345
(ctypes.c_char * sys.getsizeof(deallocated)).from_address(id(deallocated))[:4] = '\x00' * 4

If you deallocate None, you get a special message - Fatal Python error: deallocating None before crashing

Section 111.6: Viewing the refcount of an object

Section 111.7: Do not wait for the garbage collection to clean up
In particular you should not wait for garbage collection to close file handles, database connections and open
network connections.

>> f = open("test.txt")
>> del f
A more explicit way to clean up is to call f.close(). You can do it even more elegant, that is by using the with
statement, also known as the context manager :

>> with open("test.txt") as f:
... pass
... # do something with f
>> #now the f object still exists, but it is closed

The with statement allows you to indent your code under the open file. This makes it explicit and easier to see how
long a file is kept open. It also always closes a file, even if an exception is raised in the while block.

Section 111.8: Managing garbage collection
There are two approaches for influencing when a memory cleanup is performed. They are influencing how often
the automatic process is performed and the other is manually triggering a cleanup.

The garbage collector can be manipulated by tuning the collection thresholds which affect the frequency at which
the collector runs. Python uses a generation based memory management system. New objects are saved in the
newest generation - generation0 and with each survived collection, objects are promoted to older generations.
After reaching the last generation - generation2, they are no longer promoted.

The thresholds can be changed using the following snippet:
import gc
gc.set_threshold(1000, 100, 10) # Values are just for demonstration purpose

The first argument represents the threshold for collecting generation0. Every time the number of allocations
exceeds the number of deallocations by 1000 the garbage collector will be called.

The older generations are not cleaned at each run to optimize the process. The second and third arguments are
optional and control how frequently the older generations are cleaned. If generation0 was processed 100 times
without cleaning generation1, then generation1 will be processed. Similarly, objects in generation2 will be
processed only when the ones in generation1 were cleaned 10 times without touching generation2.


One instance in which manually setting the thresholds is beneficial is when the program allocates a lot of small
objects without deallocating them which leads to the garbage collector running too often (each
generation0_threshold object allocations). Even though, the collector is pretty fast, when it runs on huge numbers
of objects it poses a performance issue. Anyway, there's no one size fits all strategy for choosing the thresholds and
it's use case dependable.

Manually triggering a collection can be done as in the following snippet:
import gc
gc.collect()

The garbage collection is automatically triggered based on the number of allocations and deallocations, not on the
consumed or available memory.

For long-running programs, the garbage collection can be triggered on a time basis or on an event basis. An
example for the first one is a web server that triggers a collection after a fixed number of requests. For the later, a
web server that triggers a garbage collection when a certain type of request is received.


"""

#Section 111.2: Eects of the del command
print("------Section 111.2: Eects of the del command-------")

import gc
gc.disable() # disable garbage collector

class Track:
    def __init__(self):
        print("Initialized")
    def __del__(self):
        print("Destructed")

def bar():
    return Track()

t = bar()
another_t = t # assign another reference
print("...")
del t # not destructed yet - another_t still refers to it
del another_t # final reference gone, object is destructed

#Section 111.3: Reference Counting
print("----Section 111.3: Reference Counting--------")


def foo():
    Track()
    # destructed immediately since no longer has any references
    print("---")
    t = Track()
    # variable is referenced, so it's not destructed yet
    print("---")
    # variable is destructed when function exits

foo()


#Section 111.4: Garbage Collector for Reference Cycles
print("-----Section 111.4: Garbage Collector for Reference Cycles--------")

A = Track()
B = Track()
A.other = B
B.other = A
del A; del B # objects are not destructed due to reference cycle
gc.collect() # trigger collection


#Section 111.5: Forcefully deallocating objects
print("----Section 111.5: Forcefully deallocating objects------")

#Section 111.6: Viewing the refcount of an object
print("------Section 111.6: Viewing the refcount of an object--------")
import sys
a = object()
print(sys.getrefcount(a))

b = a
print(sys.getrefcount(a))
del b
print(sys.getrefcount(a))

#Section 111.7: Do not wait for the garbage collection to clean up
print("-------Section 111.7: Do not wait for the garbage collection to clean up------")