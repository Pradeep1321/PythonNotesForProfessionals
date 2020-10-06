'''
Chapter 38: Classes
Section 38.1: Introduction to classes
A class, functions as a template that defines the basic characteristics of a particular object.
Every method, included in the class definition passes the object in question as its first parameter. The word
self is used for this parameter (usage of self is actually by convention, as the word self has no inherent
meaning in Python, but this is one of Python's most respected conventions, and you should always follow it).

Some of the class's methods have the following form: __functionname__(self, other_stuff). All such
methods are called "magic methods" and are an important part of classes in Python. For instance, operator
overloading in Python is implemented with magic methods.

Section 38.2: Bound, unbound, and static methods
The idea of bound and unbound methods was removed in Python 3. In Python 3 when you declare a method within
a class, you are using a def keyword, thus creating a function object. This is a regular function, and the surrounding
class works as its namespace.

Python 3.x Version ≥ 3.0
class A(object):
    def f(self, x):
        return 2 * x
A.f
# <function A.f at ...> (in Python 3.x)

In Python 2 the behavior was different: function objects within the class were implicitly replaced with objects of type
instancemethod, which were called unbound methods because they were not bound to any particular class instance.
It was possible to access the underlying function using .__func__ property.
Python 2.x Version ≥ 2.3

A.f
# <unbound method A.f> (in Python 2.x)

A.f.__class__
# <type 'instancemethod'>

A.f.__func__
# <function f at ...>


The latter behaviors are confirmed by inspection - methods are recognized as functions in Python 3, while the
distinction is upheld in Python 2.

Python 3.x Version ≥ 3.0
import inspect
inspect.isfunction(A.f)
# True
inspect.ismethod(A.f)
# False
Python 2.x Version ≥ 2.3
import inspect
inspect.isfunction(A.f)
# False
inspect.ismethod(A.f)
# True


In both versions of Python function/method A.f can be called directly, provided that you pass an instance of class A
as the first argument.
A.f(1, 7)
# Python 2: TypeError: unbound method f() must be called with
# A instance as first argument (got int instance instead)
# Python 3: 14
a = A()
A.f(a, 20)
# Python 2 & 3: 40

Now suppose a is an instance of class A, what is a.f then? Well, intuitively this should be the same method f of class
A, only it should somehow "know" that it was applied to the object a – in Python this is called method bound to a.

writing a.f invokes the magic __getattribute__ method of a, which first
checks whether a has an attribute named f (it doesn't), then checks the class A whether it contains a method with
such a name (it does), and creates a new object m of type method which has the reference to the original A.f in
m.__func__, and a reference to the object a in m.__self__. When this object is called as a function, it simply does
the following: m(...) => m.__func__(m.__self__, ...). Thus this object is called a bound method because when
invoked it knows to supply the object it was bound to as the first argument. (These things work same way in Python
2 and 3).

# Note: the bound method object a.f is recreated *every time* you call it:
a.f is a.f # False

# As a performance optimization you can store the bound method in the object's
# __dict__, in which case the method object will remain fixed:
a.f = a.f

a.f is a.f # True

Finally, Python has class methods and static methods – special kinds of methods. Class methods work the same
way as regular methods, except that when invoked on an object they bind to the class of the object instead of to the
object. Thus m.__self__ = type(a). When you call such bound method, it passes the class of a as the first
argument. Static methods are even simpler: they don't bind anything at all, and simply return the underlying
function without any transformations.

It is worth noting that at the lowest level, functions, methods, staticmethods, etc. are actually descriptors that
invoke __get__, __set__ and optionally __del__ special methods

Section 38.3: Basic inheritance
Note: As of Python 2.2, all classes implicitly inherit from the object class,
which is the base class for all built-in types.

super() is
used to call the __init__() method of Rectangle class, essentially calling any overridden method of the base class.
Note: in Python 3, super() does not require arguments.

Derived class objects can access and modify the attributes of its base classes

Built-in functions that work with inheritance
issubclass(DerivedClass, BaseClass): returns True if DerivedClass is a subclass of the BaseClass
isinstance(s, Class): returns True if s is an instance of Class or any of the derived classes of Class


Section 38.4: Monkey Patching

In this case, "monkey patching" means adding a new variable or method to a class after it's been defined. For
instance, say we defined class A as

Section 38.5: New-style vs. old-style classes
Python 2.x Version ≥ 2.2.0
New-style classes were introduced in Python 2.2 to unify classes and types. They inherit from the top-level object
type. A new-style class is a user-defined type, and is very similar to built-in types.

Old-style classes do not inherit from object. Old-style instances are always implemented with a built-in instance
type.
Python 3.x Version ≥ 3.0.0
In Python 3, old-style classes were removed.
New-style classes in Python 3 implicitly inherit from object, so there is no need to specify MyClass(object)
anymore.

Section 38.6: Class methods: alternate initializers
Class methods present alternate ways to build instances of classes.

Section 38.7: Multiple Inheritance
Python uses the C3 linearization algorithm to determine the order in which to resolve class attributes, including
methods. This is known as the Method Resolution Order (MRO).

Another powerful feature in inheritance is super. super can fetch parent classes features.
Multiple inheritance with init method of class, when every class has own init method then we try for multiple
inheritance then only init method get called of class which is inherit first.

Section 38.8: Properties
Python classes support properties, which look like regular object variables, but with the possibility of attaching
custom behavior and documentation.

Another common use of properties is to enable the class to present 'virtual attributes' - attributes which aren't
actually stored but are computed only when requested.

Section 38.9: Default values for instance variables
If the variable contains a value of an immutable type (e.g. a string) then it is okay to assign a default value like this
One needs to be careful when initializing mutable objects such as lists in the constructor.

Section 38.10: Class and instance variables
Instance variables are unique for each instance, while class variables are shared by all instances
Class variables can be accessed on instances of this class, but assigning to the class attribute will create an instance
variable which shadows the class variable

Section 38.11: Class composition
Class composition allows explicit relations between objects.

Section 38.12: Listing All Class Members
The dir() function can be used to get a list of the members of a class:
dir(Class)

Caveats:
Classes can define a __dir__() method. If that method exists calling dir() will call __dir__(), otherwise Python
will try to create a list of members of the class. This means that the dir function can have unexpected results.

Section 38.13: Singleton class
A singleton is a pattern that restricts the instantiation of a class to one instance/object. For

Section 38.14: Descriptors and Dotted Lookups
Descriptors are objects that are (usually) attributes of classes and that have any of __get__, __set__, or
__delete__ special methods.
Data Descriptors have any of __set__, or __delete__

These can control the dotted lookup on an instance, and are used to implement functions, staticmethod,
classmethod, and property. A dotted lookup (e.g. instance foo of class Foo looking up attribute bar - i.e. foo.bar)
uses the following algorithm:
1. bar is looked up in the class, Foo. If it is there and it is a Data Descriptor, then the data descriptor is used.
That's how property is able to control access to data in an instance, and instances cannot override this. If a
Data Descriptor is not there, then
2. bar is looked up in the instance __dict__. This is why we can override or block methods being called from an
instance with a dotted lookup. If bar exists in the instance, it is used. If not, we then
3. look in the class Foo for bar. If it is a Descriptor, then the descriptor protocol is used. This is how functions
(in this context, unbound methods), classmethod, and staticmethod are implemented. Else it simply returns
the object there, or there is an AttributeError


Chapter 39: Metaclasses

Metaclasses allow you to deeply modify the behaviour of Python classes (in terms of how they're defined,
instantiated, accessed, and more) by replacing the type metaclass that new classes use by default

Section 39.1: Basic Metaclasses
When type is called with three arguments it behaves as the (meta)class it is, and creates a new instance, ie. it
produces a new class/type.

Dummy = type('OtherDummy', (), dict(x=1))
Dummy.__class__ # <type 'type'>
Dummy().__class__.__class__ # <type 'type'>

It is possible to subclass type to create an custom metaclass.

Section 39.2: Singletons using metaclasses
A singleton is a pattern that restricts the instantiation of a class to one instance/object

Section 39.3: Using a metaclass
Metaclass syntax
Python 2.x Version ≤ 2.7
class MyClass(object):
    __metaclass__ = SomeMetaclass
Python 3.x Version ≥ 3.0
class MyClass(metaclass=SomeMetaclass):
    pass

Python 2 and 3 compatibility with six
import six

class MyClass(six.with_metaclass(SomeMetaclass)):
    pass

Section 39.4: Introduction to Metaclasses
To check the class of an object x, one can call type(x),
Most classes in python are instances of type. type itself is also a class. Such classes whose instances are also
classes are called metaclasses.

A metaclass which does something usually overrides type's __new__, to modify some properties of the class to be
created, before calling the original __new__ which creates the class:

Section 39.5: Custom functionality with metaclasses

Section 39.6: The default metaclass
Everything is an object in Python, so everything has a class
The class of a class is called a metaclass
The default metaclass is type, and by far it is the most common metaclass

metaclasses can be used control how your classes are initialized.



'''

#Python has class methods and static methods
class D(object):
    multiplier = 2
    @classmethod
    def f(cls, x):
        return cls.multiplier * x
    @staticmethod
    def g(name):
        print("Hello, %s" % name)

#Note that class methods are bound to the class even when accessed on the instance
d = D()
d.multiplier = 1337
print(D.multiplier, d.multiplier)

#Section 38.4: Monkey Patching
class A(object):
    def __init__(self, num):
        self.num = num
    def __add__(self, other):
        return A(self.num + other.num)

def get_num(self):
    return self.num

#We can add get_num function to the class A with an assignment statement. Because functions are objects just like
# any other object, and methods are functions that
#belong to the class. The function get_num shall be available to all existing (already created) as well to the new
# Instances of A. These additions are available on all instances of that class (or its subclasses) automatically

A.get_num = get_num


#Section 38.5: New-style vs. old-style classes

#Section 38.7: Multiple Inheritance

#Multiple inheritance with init method of class, when every class has own init method then we try for multiple
#inheritance then only init method get called of class which is inherit first.

class Foo(object):
    def __init__(self):
        print ("foo init")
class Bar(object):
    def __init__(self):
        print ("bar init")
class FooBar(Foo, Bar):
    def __init__(self):
        print ("foobar init")
        super(FooBar, self).__init__()

a = FooBar()

#But it doesn't mean that Bar class is not inherit. Instance of final FooBar class is also instance of Bar class and Foo
#class.

print (isinstance(a,FooBar))
print (isinstance(a,Foo))
print (isinstance(a,Bar))

#Section 38.8: Properties

# Virtual Attributes
class Character(object):
    def __init__(name, max_hp):
        self._name = name
        self._hp = max_hp
        self._max_hp = max_hp
    # Make hp read only by not providing a set method
    @property
    def hp(self):
        return self._hp

    # Make name read only by not providing a set method
    @property
    def name(self):
        return self.name

    def take_damage(self, damage):
        self.hp -= damage
        self.hp = 0 if self.hp < 0 else self.hp

    @property
    def is_alive(self):
        return self.hp != 0

    @property
    def is_wounded(self):
        return self.hp < self.max_hp if self.hp > 0 else False

    @property
    def is_dead(self):
        return not self.is_alive

#Section 38.9: Default values for instance variables
#One needs to be careful when initializing mutable objects such as lists in the constructor. Consider the following
#example:

class Rectangle2D(object):
    def __init__(self, width, height, pos=[0,0], color='blue'):
        self.width = width
        self.height = height
        self.pos = pos
        self.color = color

r1 = Rectangle2D(5,3)
r2 = Rectangle2D(7,8)
r1.pos[0] = 4
r1.pos # [4, 0]
r2.pos

'''This behavior is caused by the fact that in Python default parameters are bound at function execution and not at
function declaration. To get a default instance variable that's not shared among instances, one should use a
construct like this:'''
class Rectangle2D(object):
    def __init__(self, width, height, pos=None, color='blue'):
        self.width = width
        self.height = height
        self.pos = pos or [0, 0] # default value is [0, 0]
        self.color = color

#Section 38.10: Class and instance variables
class D:
    x = []
    def __init__(self, item):
     self.x.append(item) # note that this is not an assignment!
d1 = D(1)
d2 = D(2)
d1.x
# [1, 2]
d2.x
# [1, 2]
D.x
# [1, 2]

#Section 38.11: Class composition
class Country(object):
    def __init__(self):
        self.cities=[]
    def addCity(self,city):
        self.cities.append(city)

class City(object):
    def __init__(self, numPeople):
        self.people = []
        self.numPeople = numPeople
    def addPerson(self, person):
        self.people.append(person)
    def join_country(self,country):
        self.country = country
        country.addCity(self)
        for i in range(self.numPeople):
            Person(i).join_city(self)

class Person(object):
    def __init__(self, ID):
        self.ID=ID
    def join_city(self, city):
        self.city = city
        city.addPerson(self)
    def people_in_my_country(self):
        x= sum([len(c.people) for c in self.city.country.cities])
        return x

US=Country()
NYC=City(10).join_country(US)
SF=City(5).join_country(US)
print(US.cities[0].people[0].people_in_my_country())

print("Singleton")
#Section 39.2: Singletons using metaclasses
class SingletonType(type):
    def __call__(cls, *args, **kwargs):
        try:
            return cls.__instance
        except AttributeError:
            cls.__instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls.__instance

#Python 2.x Version ≤ 2.7
#class MySingleton(object):
#   __metaclass__ = SingletonType
#Python 3.x Version ≥ 3.0
class MySingleton(metaclass=SingletonType):
    pass

print(MySingleton() is MySingleton())

#Section 39.3: Using a metaclass

