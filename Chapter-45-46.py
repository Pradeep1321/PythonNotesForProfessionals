'''
Chapter 45: Math Module
Section 45.1: Rounding: round, floor, ceil, trunc
In addition to the built-in round function, the math module provides the floor, ceil, and trunc functions
Python 2.x Version ≤ 2.7
floor, ceil, trunc, and round always return a float.

Python 3.x Version ≥ 3.0
floor, ceil, and trunc always return an Integral value, while round returns an Integral value if called with one
argument.

Section 45.2: Trigonometry
Converting degrees to/from radians
All math functions expect radians so you need to convert degrees to radians:

All results of the inverse trigonometric functions return the result in radians, so you may need to convert it back to
degrees:

Apart from the math.atan there is also a two-argument math.atan2 function, which computes the correct quadrant
and avoids pitfalls of division by zero:

Section 45.3: Pow for faster exponentiation

Using the timeit module from the command line:
> python -m timeit 'for x in xrange(50000): b = x**3'
10 loops, best of 3: 51.2 msec per loop

from math import pow

pow(5,5)
pow(x,3)

Section 45.4: Infinity and NaN ("not a number")
In all versions of Python, we can represent infinity and NaN ("not a number") as follows:
pos_inf = float('inf') # positive infinity
neg_inf = float('-inf') # negative infinity
not_a_num = float('nan') # NaN ("not a number")
In Python 3.5 and higher, we can also use the defined constants math.inf and math.nan:

Python 3.x Version ≥ 3.5

pos_inf = math.inf
neg_inf = -math.inf
not_a_num = math.nan

We can test for either positive or negative infinity with the isinf method:
math.isinf(pos_inf)

We can test specifically for positive infinity or for negative infinity by direct comparison:
pos_inf == float('inf') # or == math.inf in Python 3.5+
neg_inf == float('-inf') # or == -math.inf in Python 3.5+

Python 3.2 and higher also allows checking for finiteness:
math.isfinite(pos_inf)
# Out: False
math.isfinite(0.0)
# Out: True

sys.float_info.max
(this is system-dependent)
pos_inf > sys.float_info.max
# Out: True
neg_inf < -sys.float_info.max
# Out: True

But if an arithmetic expression produces a value larger than the maximum that can be represented as a float, it
will become infinity:

pos_inf == sys.float_info.max * 1.0000001
# Out: True


However division by zero does not give a result of infinity (or negative infinity where appropriate), rather it raises a
ZeroDivisionError exception.

NaN is never equal to anything, not even itself. We can test for it is with the isnan method:
NaN always compares as "not equal", but never less than or greater than
Arithmetic operations on NaN always give NaN. This includes multiplication by -1: there is no "negative NaN"

Python 3.x Version ≥ 3.5
-math.nan

There is one subtle difference between the old float versions of NaN and infinity and the Python 3.5+ math library
constants:
Python 3.x Version ≥ 3.5
math.inf is math.inf, math.nan is math.nan
# Out: (True, True)
float('inf') is float('inf'), float('nan') is float('nan')
# Out: (False, False)


Section 45.5: Logarithms
math.log(x) gives the natural (base e) logarithm of x.

math.log can lose precision with numbers close to 1, due to the limitations of floating-point numbers. In order to
accurately calculate logs close to 1, use math.log1p, which evaluates the natural logarithm of 1 plus the argument:

math.log(1 + 1e-20) # 0.0
math.log1p(1e-20) # 1e-20

math.log10 can be used for logs base 10:

Python 2.x Version ≥ 2.3.0
When used with two arguments, math.log(x, base) gives the logarithm of x in the given base (i.e. log(x) /
log(base).

Section 45.6: Constants
math modules includes two commonly used mathematical constants.
    math.pi - The mathematical constant pi
    math.e - The mathematical constant e (base of natural logarithm)
from math import pi, e

Python 3.5 and higher have constants for infinity and NaN ("not a number"). The older syntax of passing a string to
float() still works.

Python 3.x Version ≥ 3.5
math.inf == float('inf')
# Out: True

-math.inf == float('-inf')
# Out: True

# NaN never compares equal to anything, even itself
math.nan == float('nan')
# Out: False

Section 45.7: Imaginary Numbers
Imaginary numbers in Python are represented by a "j" or "J" trailing the target number
1j # Equivalent to the square root of -1.
1j * 1j # = (-1+0j)

Section 45.8: Copying signs
In Python 2.6 and higher, math.copysign(x, y) returns x with the sign of y. The returned value is always a float.

Section 45.9: Complex numbers and the cmath module
The cmath module is similar to the math module, but defines functions appropriately for the complex plane.

We have the real part and the imag (imaginary) part, as well as the complex conjugate
# real part and imaginary part are both float type
z.real, z.imag
# Out: (1.0, 3.0)
z.conjugate()
# Out: (1-3j) # z.conjugate() == z.real - z.imag * 1j

Naturally the behavior of sqrt is different for complex numbers and real numbers. In non-complex math the square
root of a negative number raises an exception:

math.sqrt(-1)
# Exception: ValueError: math domain error

The cmath module also provides many functions with direct counterparts from the math module.
In addition to sqrt, there are complex versions of exp, log, log10, the trigonometric functions and their inverses
(sin, cos, tan, asin, acos, atan), and the hyperbolic functions and their inverses (sinh, cosh, tanh, asinh, acosh,
atanh). Note however there is no complex counterpart of math.atan2, the two-argument form of arctangent

The constants pi and e are provided. Note these are float and not complex.

The cmath module also provides complex versions of isinf, and (for Python 3.2+) isfinite. See "Infinity and NaN".
A complex number is considered infinite if either its real part or its imaginary part is infinite.
cmath.isinf(complex(float('inf'), 0.0))
# Out: True

Likewise, the cmath module provides a complex version of isnan. See "Infinity and NaN". A complex number is
considered "not a number" if either its real part or its imaginary part is "not a number".
cmath.isnan(0.0, float('nan'))
# Out: True

In Python 3.5 and higher, there is an isclose method in both cmath and math modules.

Python 3.x Version ≥ 3.5
z = cmath.rect(*cmath.polar(1+1j))
z
# Out: (1.0000000000000002+1.0000000000000002j)
cmath.isclose(z, 1+1j)
# True



Chapter 46: Complex math

Section 46.1: Advanced complex arithmetic

This module can calculate the phase of a complex number, in radians:
z = 2+3j # A complex number
cmath.phase(z) # 0.982793723247329

It allows the conversion between the cartesian (rectangular) and polar representations of complex numbers
cmath.polar(z) # (3.605551275463989, 0.982793723247329)
cmath.rect(2, cmath.pi/2) # (0+2j)


The module contains the complex version of
    Exponential and logarithmic functions (as usual, log is the natural logarithm and log10 the decimal logarithm):
        cmath.exp(z) # (-7.315110094901103+1.0427436562359045j)
        cmath.log(z) # (1.2824746787307684+0.982793723247329j)
        cmath.log10(-100) # (2+1.3643763538418412j)

    Square roots:
        cmath.sqrt(z) # (1.6741492280355401+0.8959774761298381j)

    Trigonometric functions and their inverses:
        cmath.sin(z) # (9.15449914691143-4.168906959966565j)
        cmath.cos(z) # (-4.189625690968807-9.109227893755337j)
        cmath.tan(z) # (-0.003764025641504249+1.00323862735361j)
        cmath.asin(z) # (0.5706527843210994+1.9833870299165355j)
        cmath.acos(z) # (1.0001435424737972-1.9833870299165355j)
        cmath.atan(z) # (1.4099210495965755+0.22907268296853878j)
        cmath.sin(z)**2 + cmath.cos(z)**2 # (1+0j)

    Hyperbolic functions and their inverses:
        cmath.sinh(z) # (-3.59056458998578+0.5309210862485197j)
        cmath.cosh(z) # (-3.7245455049153224+0.5118225699873846j)
        cmath.tanh(z) # (0.965385879022133-0.009884375038322495j)
        cmath.asinh(z) # (0.5706527843210994+1.9833870299165355j)
        cmath.acosh(z) # (1.9833870299165355+1.0001435424737972j)
        cmath.atanh(z) # (0.14694666622552977+1.3389725222944935j)
        cmath.cosh(z)**2 - cmath.sin(z)**2 # (1+0j)
        cmath.cosh((0+1j)*z) - cmath.cos(z) # 0j

Section 46.2: Basic complex arithmetic

Python has built-in support for complex arithmetic. The imaginary unit is denoted by j:
Complex numbers can be summed, subtracted, multiplied, divided and exponentiated
z = 2+3j # A complex number
w = 1-7j # Another complex number
z + w # (3-4j)
z - w # (1+10j)
z * w # (23-11j)
z / w # (-0.38+0.34j)
z**3 # (-46+9j)

Python can also extract the real and imaginary parts of complex numbers, and calculate their absolute value and
conjugate:
z.real # 2.0
z.imag # 3.0
abs(z) # 3.605551275463989
z.conjugate() # (2-3j)


'''
import math

#Section 45.1: Rounding: round, floor, ceil, trunc
print("---Section 45.1: Rounding: round, floor, ceil, trunc---")
x = 1.55
y = -1.55
# round to the nearest integer
round(x) # 2
round(y) # -2
# the second argument gives how many decimal places to round to (defaults to 0)
round(x, 1) # 1.6
round(y, 1) # -1.6
# get the largest integer less than x
math.floor(x) # 1
math.floor(y) # -2
# get the smallest integer greater than x
math.ceil(x) # 2
math.ceil(y) # -1
# drop fractional part of x
math.trunc(x) # 1, equivalent to math.floor for positive numbers
math.trunc(y) # -1, equivalent to math.ceil for negative numbers

#Section 45.2: Trigonometry
print("----Section 45.2: Trigonometry--------")

#Calculating the length of the hypotenuse
math.hypot(2, 4) # Just a shorthand for SquareRoot(2**2 + 4**2)

math.radians(45) # Convert 45 degrees to radians

math.degrees(math.asin(1)) # Convert the result of asin to degrees

#Sine, cosine, tangent and inverse functions
# Sine and arc sine
math.sin(math.pi / 2)
# Out: 1.0
math.sin(math.radians(90)) # Sine of 90 degrees
# Out: 1.0
math.asin(1)
# Out: 1.5707963267948966 # "= pi / 2"
math.asin(1) / math.pi
# Out: 0.5
# Cosine and arc cosine:
math.cos(math.pi / 2)
# Out: 6.123233995736766e-17
# Almost zero but not exactly because "pi" is a float with limited precision!
math.acos(1)
# Out: 0.0
# Tangent and arc tangent:
math.tan(math.pi/2)
# Out: 1.633123935319537e+16
# Very large but not exactly "Inf" because "pi" is a float with limited precision

#Python 3.x Version ≥ 3.5
math.atan(math.inf)
# Out: 1.5707963267948966 # This is just "pi / 2"
math.atan(float('inf'))
# Out: 1.5707963267948966 # This is just "pi / 2"

math.atan2(1, 2) # Equivalent to "math.atan(1/2)"
# Out: 0.4636476090008061 # ≈ 26.57 degrees, 1st quadrant
math.atan2(-1, -2) # Not equal to "math.atan(-1/-2)" == "math.atan(1/2)"
# Out: -2.677945044588987 # ≈ -153.43 degrees (or 206.57 degrees), 3rd quadrant
math.atan2(1, 0) # math.atan(1/0) would raise ZeroDivisionError
# Out: 1.5707963267948966 # This is just "pi / 2"

#Hyperbolic sine, cosine and tangent
# Hyperbolic sine function
math.sinh(math.pi) # = 11.548739357257746
math.asinh(1) # = 0.8813735870195429
# Hyperbolic cosine function
math.cosh(math.pi) # = 11.591953275521519
math.acosh(1) # = 0.0
# Hyperbolic tangent function
math.tanh(math.pi) # = 0.99627207622075
math.atanh(0.5) # = 0.5493061443340549

#The built-in functions abs and complex are also part of the language itself and don't require any import:
abs(1 + 1j)
# Out: 1.4142135623730951 # square root of 2
complex(1)
# Out: (1+0j)
complex(imag=1)
# Out: (1j)
complex(1, 1)
# Out: (1+1j)
complex('1 + 1j')
# Exception: ValueError: complex() arg is a malformed string

import cmath
cmath.sqrt(-1)
# Out: 1j

cmath.polar(1 + 1j)
# Out: (1.4142135623730951, 0.7853981633974483) # == (sqrt(1 + 1), atan2(1, 1))
abs(1 + 1j), cmath.phase(1 + 1j)
# Out: (1.4142135623730951, 0.7853981633974483) # same as previous calculation
cmath.rect(math.sqrt(2), math.atan(1))
# Out: (1.0000000000000002+1.0000000000000002j)

cmath.phase(complex(-1.0, 0.0))
# Out: 3.141592653589793
cmath.phase(complex(-1.0, -0.0))
# Out: -3.141592653589793


