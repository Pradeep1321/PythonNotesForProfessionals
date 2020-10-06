"""
Chapter 64: Indexing and Slicing

Paramer                 Description
obj             The object that you want to extract a "sub-object" from
start           The index of obj that you want the sub-object to start from (keep in mind that Python is zero-indexed,
                meaning that the first item of obj has an index of 0). If omitted, defaults to 0.
stop            The (non-inclusive) index of obj that you want the sub-object to end at. If omitted, defaults to len(obj).
step            Allows you to select only every step item. If omitted, defaults to 1.

Section 64.1: Basic Slicing

For any iterable (for eg. a string, list, etc), Python allows you to slice and return a substring or sublist of its data.
Format for slicing:
    iterable_name[start:stop:step]
where,
start is the first index of the slice. Defaults to 0 (the index of the first element)
stop one past the last index of the slice. Defaults to len(iterable)
step is the step size (better explained by the examples below)

#Section 64.2: Reversing an object

You can use slices to very easily reverse a str, list, or tuple (or basically any collection object that implements
slicing with the step parameter).


Section 64.3: Slice assignment

Section 64.4: Making a shallow copy of an array
A quick way to make a copy of an array (as opposed to assigning a variable with another reference to the original array) is:
arr[:]

Note that this makes a shallow copy, and is identical to arr.copy().

Section 64.5: Indexing custom classes: __getitem__, __setitem__ and __delitem__

Section 64.6: Basic Indexing
If you try to access an index which is not present in the list, an IndexError will be raised:

"""

#Section 64.1: Basic Slicing
print("-------Section 64.1: Basic Slicing--------")
a = "abcdef"
a # "abcdef"
# Same as a[:] or a[::] since it uses the defaults for all three indices
a[-1] # "f"
a[:] # "abcdef"
a[::] # "abcdef"
a[3:] # "def" (from index 3, to end(defaults to size of iterable))
a[:4] # "abcd" (from beginning(default 0) to position 4 (excluded))
a[2:4] # "cd" (from position 2, to position 4 (excluded))
#In addition, any of the above can be used with the step size defined:
a[::2] # "ace" (every 2nd element)
a[1:4:2] # "bd" (from index 1, to index 4 (excluded), every 2nd element)
#Indices can be negative, in which case they're computed from the end of the sequence
a[:-1] # "abcde" (from index 0 (default), to the second last element (last element - 1))
a[:-2] # "abcd" (from index 0 (default), to the third last element (last element -2))
a[-1:] # "f" (from the last element to the end (default len())
3Step sizes can also be negative, in which case slice will iterate through the list in reverse order:
a[3:1:-1] # "dc" (from index 2 to None (default), in reverse order)
3This construct is useful for reversing an iterable
a[::-1]  # "fedcba" (from last element (default len()-1), to first, in reverse order(-1))
#Notice that for negative steps the default end_index is None (see http://stackoverflow.com/a/12521981 )
a[5:None:-1] # "fedcba" (this is equivalent to a[::-1])
a[5:0:-1] # "fedcb" (from the last element (index 5) to second element (index 1)

#Section 64.2: Reversing an object
print("-------Section 64.2: Reversing an object------------")
s = 'reverse me!'
s[::-1] # '!em esrever'

#Section 64.3: Slice assignment
print("-------Section 64.3: Slice assignment-------")

#This means that if you have a list, you can replace multiple members in a single assignment:
lst = [1, 2, 3]
lst[1:3] = [4, 5]
print(lst) # Out: [1, 4, 5]
#The assignment shouldn't match in size as well, so if you wanted to replace an old slice with a new slice that is
#different in size, you could:
lst = [1, 2, 3, 4, 5]
lst[1:4] = [6]
print(lst) # Out: [1, 6, 5]

#It's also possible to use the known slicing syntax to do things like replacing the entire list:
lst = [1, 2, 3]
lst[:] = [4, 5, 6]
print(lst) # Out: [4, 5, 6]

#Or just the last two members:
lst = [1, 2, 3]
lst[-2:] = [4, 5, 6]
print(lst) # Out: [1, 4, 5, 6]

#Section 64.4: Making a shallow copy of an array
print("-------Section 64.4: Making a shallow copy of an array---------")
arr = ['a', 'b', 'c']
copy = arr[:]
arr.append('d')
print(arr) # ['a', 'b', 'c', 'd']
print(copy) # ['a', 'b', 'c']

#Section 64.5: Indexing custom classes: __getitem__, __setitem__ and __delitem__
print("--------Section 64.5: Indexing custom classes: __getitem__,__setitem__ and __delitem__-------------")

#Section 64.6: Basic Indexing
print("--------Section 64.6: Basic Indexing-----")
