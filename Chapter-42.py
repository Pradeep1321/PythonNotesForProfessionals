"""
Chapter 42: Using loops within functions

Section 42.1: Return statement inside loop in a function
"""

def func(params):
    for value in params:
        print ('Got value {}'.format(value))
        if value == 1:
            # Returns from function as soon as value is 1
                print (">>>> Got 1")
                return 
        return print ("Still looping")
    return "Couldn't find 1"

func([5, 3, 1, 2, 8, 9])