"""
Chapter 70: Exponentiation
Section 70.1: Exponentiation using builtins: ** and pow()

Exponentiation can be used by using the builtin pow-function or the ** operator:
Base: int, exponent: int < 0:
2 ** -3
# Out: 0.125 (result is a float)
This is also valid for Python 3.x.
Before Python 2.2.0, this raised a ValueError.
Base: int < 0 or float < 0, exponent: float != int
(-2) ** (0.5) # also (-2.) ** (0.5)
# Out: (8.659560562354934e-17+1.4142135623730951j) (result is complex)
Before python 3.0.0, this raised a ValueError.

The operator module contains two functions that are equivalent to the **-operator:
import operator
operator.pow(4, 2) # 16
operator.__pow__(4, 3) # 64

val1, val2 = 4, 2
val1.__pow__(val2) # 16
val2.__rpow__(val1) # 16
# in-place power operation isn't supported by immutable classes like int, float, complex:
# val1.__ipow__(val2)

Section 70.2: Square root: math.sqrt() and cmath.sqrt

The math module contains the math.sqrt()-function that can compute the square root of any number (that can be
converted to a float) and the result will always be a float:


The math.sqrt() function raises a ValueError if the result would be complex:

math.sqrt(-10)
    ValueError: math domain error

math.sqrt(x) is faster than math.pow(x, 0.5) or x ** 0.5 but the precision of the results is the same. The cmath
module is extremely similar to the math module, except for the fact it can compute complex numbers and all of its
results are in the form of a + bi. It can also use .sqrt():


Section 70.3: Modular exponentiation: pow() with 3 arguments
Supplying pow() with 3 arguments pow(a, b, c) evaluates the modular exponentiation ab mod c:

For built-in types using modular exponentiation is only possible if:
First argument is an int
Second argument is an int >= 0
Third argument is an int != 0
These restrictions are also present in python 3.x


Section 70.4: Computing large integer roots
Even though Python natively supports big integers, taking the nth root of very large numbers can fail in Python.

Section 70.5: Exponentiation using the math module: math.pow()
The math-module contains another math.pow() function. The difference to the builtin pow()-function or ** operator
is that the result is always a float:
Which excludes computations with complex inputs:
and computations that would lead to complex results:

Section 70.6: Exponential function: math.exp() and cmath.exp()
Both the math and cmath-module contain the Euler number: e and using it with the builtin pow()-function or **-
operator works mostly like math.exp():

However the result is different and using the exponential function directly is more reliable than builtin
exponentiation with base math.e:

Section 70.7: Exponential function minus 1: math.expm1()
The math module contains the expm1()-function that can compute the expression math.e ** x - 1 for very small x
with higher precision than math.exp(x) or cmath.exp(x) would allow:

Section 70.8: Magic methods and exponentiation: builtin, math and cmath

Section 70.9: Roots: nth-root with fractional exponents
While the math.sqrt function is provided for the specific case of square roots, it's often convenient to use the
exponentiation operator (**) with fractional exponents to perform nth-root operations, like cube roots


"""

#Section 70.1: Exponentiation using builtins: ** and pow()
print("------Section 70.1: Exponentiation using builtins: ** and pow()-------")
import operator
print(operator.pow(4, 2)) # 16
print(operator.__pow__(4, 3)) # 64
val1, val2 = 4, 2
print(val1.__pow__(val2)) # 16
print(val2.__rpow__(val1)) # 16

#Section 70.2: Square root: math.sqrt() and cmath.sqrt
print("---Section 70.2: Square root: math.sqrt() and cmath.sqrt---------")

import math
import cmath
math.sqrt(9) # 3.0
math.sqrt(11.11) # 3.3331666624997918
#math.sqrt(Decimal('6.25')) # 2.5

#Section 70.3: Modular exponentiation: pow() with 3 arguments
print("-----Section 70.3: Modular exponentiation: pow() with 3 arguments-------")
pow(3, 4, 17) # 13
# equivalent unoptimized expression:
print(3 ** 4 % 17) # 13

def modular_inverse(x, p):
    """Find a such as a·x ≡ 1 (mod p), assuming p is prime."""
    return pow(x, p-2, p)
print([modular_inverse(x, 13) for x in range(1,13)])

#Section 70.4: Computing large integer roots

#Section 70.6: Exponential function: math.exp() and cmath.exp()
print("---Section 70.6: Exponential function: math.exp() and cmath.exp()----")
math.e ** 2 # 7.3890560989306495
math.exp(2) # 7.38905609893065
import cmath
cmath.e ** 2 # 7.3890560989306495
cmath.exp(2) # (7.38905609893065+0j)
print(math.e ** 10) # 22026.465794806703
print(math.exp(10)) # 22026.465794806718
print(cmath.exp(10).real) # 22026.465794806718
# difference starts here ---------------^

#Section 70.7: Exponential function minus 1: math.expm1()
print("-----Section 70.7: Exponential function minus 1: math.expm1()-------")

print(math.e ** 1e-3 - 1) # 0.0010005001667083846
print(math.exp(1e-3) - 1) # 0.0010005001667083846
print(math.expm1(1e-3)) # 0.0010005001667083417
                       # ------------------^

print(math.e ** 1e-15 - 1) # 1.1102230246251565e-15
print(math.exp(1e-15) - 1) # 1.1102230246251565e-15
print(math.expm1(1e-15)) # 1.0000000000000007e-15
                           # ^-------------------

#Section 70.8: Magic methods and exponentiation: builtin, math and cmath
print("-----Section 70.8: Magic methods and exponentiation: builtin, math and cmath-------")


#Section 70.9: Roots: nth-root with fractional exponents
print("-----Section 70.9: Roots: nth-root with fractional exponents-----")
