"""
Chapter 141: List destructuring (aka packing and unpacking)
Section 141.1: Destructuring assignment

If you try to unpack more than the length of the iterable, you'll get an error:
a, b, c = [1]
# Raises: ValueError: not enough values to unpack (expected 3, got 1)

Section 141.2: Packing function arguments


"""

#Destructuring as values
a, b = (1, 2)
print(a)
# Prints: 1
print(b)
# Prints: 2

#Destructuring as a list
#You can unpack a list of unknown length using the following syntax:
head, *tail = [1, 2, 3, 4, 5]
print(head)
# Prints: 1
print(tail)
# Prints: [2, 3, 4, 5]

#Which is equivalent to:
l = [1, 2, 3, 4, 5]
head = l[0]
tail = l[1:]

a, b, *other, z = [1, 2, 3, 4, 5]
print(a, b, z, other)
# Prints: 1 2 5 [3, 4]

#Ignoring values in destructuring assignments
#If you're only interested in a given value, you can use _ to indicate you aren’t interested. Note: this will still set _, just
#most people don’t use it as a variable.

a, _, c = (1, 2, 3)
print(a)
# Prints: 1
print(c)
# Prints: 3

#Python 3.x Version > 3.0
#Ignoring lists in destructuring assignments
#Finally, you can ignore many values using the *_ syntax in the assignment:

a, _, b, _, c, *_ = [1, 2, 3, 4, 5, 6]
print(a, b, c)
# Prints: 1 3 5


#Section 141.2: Packing function arguments
print("------Section 141.2: Packing function arguments-----")
#using *args, **kwargs we use for packing functional arguments

#Section 141.3: Unpacking function arguments
print("----Section 141.3: Unpacking function arguments-----")
#The *args and **kwargs parameters are special parameters that are set to a tuple and a dict, respectively: