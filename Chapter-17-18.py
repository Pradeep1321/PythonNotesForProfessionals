'''
Chapter 17: Arrays
Parameter       Details
b               Represents signed integer of size 1 byte
B               Represents unsigned integer of size 1 byte
c               Represents character of size 1 byte
u               Represents unicode character of size 2 bytes
h               Represents signed integer of size 2 bytes
H               Represents unsigned integer of size 2 bytes
i               Represents signed integer of size 2 bytes
I               Represents unsigned integer of size 2 bytes
w               Represents unicode character of size 4 bytes
l               Represents signed integer of size 4 bytes
L               Represents unsigned integer of size 4 bytes
f               Represents floating point of size 4 bytes
d               Represents floating point of size 8 bytes

"Arrays" in Python are not the arrays in conventional programming languages like C and Java, but closer to lists. A
list can be a collection of either homogeneous or heterogeneous elements, and may contain ints, strings or other lists.

Section 17.1: Access individual elements through indexes
my_array = array('i', [1,2,3,4,5])

Section 17.2: Basic Introduction to Arrays
An array is a data structure that stores values of same data type. In Python, this is the main difference between
arrays and lists.

To use arrays in python language, you need to import the standard array module. This is because array is not a
fundamental data type like strings, integer etc. Here is how you can import array module in python :
from array import *
arrayIdentifierName = array(typecode, [Initializers])

Section 17.3: Append any value to the array using append() method

Section 17.4: Insert value in an array using insert() method
my_array = array('i', [1,2,3,4,5])
my_array.insert(0,0)
#array('i', [0, 1, 2, 3, 4, 5])

Section 17.5: Extend python array using extend() method
my_array = array('i', [1,2,3,4,5])
my_extnd_array = array('i', [7,8,9,10])
my_array.extend(my_extnd_array)
# array('i', [1, 2, 3, 4, 5, 7, 8, 9, 10])

Section 17.6: Add items from list into array using fromlist() method
my_array = array('i', [1,2,3,4,5])
c=[11,12,13]
my_array.fromlist(c)
# array('i', [1, 2, 3, 4, 5, 11, 12, 13])

Section 17.7: Remove any array element using remove() method

Section 17.9: Fetch any element through its index using index() method

Section 17.10: Reverse a python array using reverse() method

Section 17.11: Get array buer information through buer_info() method
my_array = array('i', [1,2,3,4,5])
my_array.buffer_info()
#>>(33881712, 5)

Section 17.12: Check for number of occurrences of an element using count() method

Section 17.13: Convert array to string using tostring() method

Section 17.14: Convert array to a python list with same elements using tolist() method

Section 17.15: Append a string to char array using fromstring() method
You are able to append a string to a character array using fromstring()
my_char_array = array('c', ['g','e','e','k'])
my_char_array.fromstring("stuff")
print(my_char_array)
#array('c', 'geekstuff')

Chapter 18: Multidimensional arrays

Section 18.1: Lists in lists


'''