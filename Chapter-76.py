"""
Chapter 76: Copying data
Section 76.1: Copy a dictionary
A dictionary object has the method copy. It performs a shallow copy of the dictionary.
Section 76.2: Performing a shallow copy
A shallow copy is a copy of a collection without performing a copy of its elements

Section 76.3: Performing a deep copy
If you have nested lists, it is desirable to clone the nested lists as well. This action is called deep copy

Section 76.4: Performing a shallow copy of a list
You can create shallow copies of lists using slices.

Section 76.5: Copy a set
Sets also have a copymethod. You can use this method to perform a shallow copy
"""
import copy

#Section 76.1: Copy a dictionary
d1 = {1:[]}
d2 = d1.copy()
print(d1 is d2)
print(d1[1] is d2[1])

#Section 76.2: Performing a shallow copy
print("-----Section 76.2: Performing a shallow copy----")

c = [[1,2]]
d = copy.copy(c)
print(c is d)
print(c[0] is d[0])

#Section 76.3: Performing a deep copy
print("-------Section 76.3: Performing a deep copy---------")
c = [[1,2]]
d = copy.deepcopy(c)
print(c is d)
print(c[0] is d[0])

#Section 76.4: Performing a shallow copy of a list
print("------Section 76.4: Performing a shallow copy of a list-------")
l1 = [1,2,3]
l2 = l1[:] # Perform the shallow copy.
print(l1 is l2)

#Section 76.5: Copy a set
print("------Section 76.5: Copy a set--------")
s1 = {()}
s2 = s1.copy()
print(s1 is s2)
s2.add(3)
print(s1)
print(s2)