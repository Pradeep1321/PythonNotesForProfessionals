"""
Chapter 9: Simple Mathematical Operators

Numerical types and their metaclasses
Section 9.1: Division
In Python 2 the result of the ' / ' operator depends on the type of the numerator and denominator.
if a and b are ints, the result is an int.
if c float, the result of a / c is a float

You can also use the operator module.
import operator
operator.div(a, b) # = 1
operator.__div__(a, b) # = 1

Python 2.x Version ≥ 2.2
What if you want float division:
from __future__ import division # applies Python 3 style division to the entire module
a / b # = 1.5
a // b # = 1

from operator import truediv
truediv(a, b) # = 1.5
import operator # the operator module provides 2-argument arithmetic functions
operator.truediv(a, b) # = 1.5
operator.floordiv(a, b) # = 1
operator.floordiv(a, c) # = 1.0


import operator # the operator module provides 2-argument arithmetic functions
operator.truediv(a, b) # = 1.5
operator.floordiv(a, b) # = 1
operator.floordiv(a, c) # = 1.0

Possible combinations (builtin types):
int and int (gives an int in Python 2 and a float in Python 3)
int and float (gives a float)
int and complex (gives a complex)
float and float (gives a float)
float and complex (gives a complex)
complex and complex (gives a complex)

Section 9.2: Addition
# The "+=" operator is equivalent to:
a = operator.iadd(a, b) # a = 5 since a is set to 3 right before this line
Possible combinations (builtin types):
int and int (gives an int)
int and float (gives a float)
int and complex (gives a complex)
float and float (gives a float)
float and complex (gives a complex)
complex and complex (gives a complex)
Note: the + operator is also used for concatenating strings, lists and tuples:


Section 9.3: Exponentiation
(a ** b) # = 8
pow(a, b) # = 8
import math
math.pow(a, b) # = 8.0 (always float; does not allow complex results)
import operator
operator.pow(a, b) # = 8

Another difference between the built-in pow and math.pow is that the built-in pow can accept three arguments:
a, b, c = 2, 3, 2
pow(2, 3, 2) # 0, calculates (2 ** 3) % 2, but as per Python docs,
# does so more efficiently

Special functions:
import math
import cmath
c = 4
math.sqrt(c) # = 2.0 (always float; does not allow complex results)
cmath.sqrt(c) # = (2+0j) (always complex)
x = 8
math.pow(x, 1/3) # evaluates to 2.0
x**(1/3) # evaluates to 2.0

The function math.exp(x) computes e ** x.
math.exp(0) # 1.0
math.exp(1) # 2.718281828459045 (e)
The function math.expm1(x) computes e ** x - 1. When x is small, this gives significantly better precision than
math.exp(x) - 1.
math.expm1(0) # 0.0
math.exp(1e-6) - 1 # 1.0000004999621837e-06
math.expm1(1e-6) # 1.0000005000001665e-06
# exact result # 1.000000500000166666708333341666...

Section 9.4: Trigonometric Functions:

math.sin(a)
math.cosh(b)
math.atan(math.pi)
math.hypot(a, b)
To convert from radians -> degrees and degrees -> radians respectively use math.degrees and math.radians

Section 9.5: Inplace Operations:
a += 1
# and
a *= 2

Any mathematic operator can be used before the '=' character to make an inplace operation:
-= decrement the variable in place
+= increment the variable in place
*= multiply the variable in place
/= divide the variable in place
//= floor divide the variable in place # Python 3
%= return the modulus of the variable in place
**= raise to a power in place

Other in place operators exist for the bitwise operators (^, | etc)

Section 9.6: Subtraction:
Possible combinations (builtin types):
int and int (gives an int)
int and float (gives a float)
int and complex (gives a complex)
float and float (gives a float)
float and complex (gives a complex)
complex and complex (gives a complex)

Section 9.7: Multiplication:
Possible combinations (builtin types):
int and int (gives an int)
int and float (gives a float)
int and complex (gives a complex)
float and float (gives a float)
float and complex (gives a complex)
complex and complex (gives a complex)

Note: The * operator is also used for repeated concatenation of strings, lists, and tuples:
3 * 'ab' # = 'ababab'
3 * ('a', 'b') # = ('a', 'b', 'a', 'b', 'a', 'b')


Section 9.8:Logarithms:
math.log(5) # = 1.6094379124341003
# optional base argument. Default is math.e

# Logarithm base e - 1 (higher precision for low values)
math.log1p(5) # = 1.791759469228055
# Logarithm base 2
math.log2(8) # = 3.0
# Logarithm base 10
math.log10(100) # = 2.0
cmath.log10(100) # = (2+0j)

Section 9.9: Modulus
Like in many other languages, Python uses the % operator for calculating modulus.
operator.mod(3 , 4) # 3

You can also use negative numbers.
-9 % 7 # 5
9 % -7 # -5
-9 % -7 # -2

quotient, remainder = divmod(9, 4)
# quotient = 2, remainder = 1 as 4 * 2 + 1 == 9

Chapter 10: Bitwise Operators:
Bitwise operations alter binary strings at the bit level.

Section 10.1: Bitwise NOT
In essence, this means that whereas 1010 0110 has an unsigned value of 166 (arrived at by adding (128 * 1) +
(64 * 0) + (32 * 1) + (16 * 0) + (8 * 0) + (4 * 1) + (2 * 1) + (1 * 0)), it has a two's-complement value
of -90 (arrived at by adding (128 * 1) - (64 * 0) - (32 * 1) - (16 * 0) - (8 * 0) - (4 * 1) - (2 * 1) -
(1 * 0), and complementing the value).
In this way, negative numbers range down to -128 (1000 0000). Zero (0) is represented as 0000 0000, and minus
one (-1) as 1111 1111

In general, though, this means ~n = -n - 1.
Note, the overall effect of this operation when applied to positive numbers can be summarized:
~n -> -|n+1|
And then, when applied to negative numbers, the corresponding effect is:
~-n -> |n-1|

Section 10.2: Bitwise XOR (Exclusive OR)
The ^ operator will perform a binary XOR in which a binary 1 is copied if and only if it is the value of exactly one
operand.
# 0 ^ 0 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1
# 1 ^ 1 = 0


Section 10.3: Bitwise AND
The & operator will perform a binary AND, where a bit is copied if it exists in both operands
# 0 & 0 = 0
# 0 & 1 = 0
# 1 & 0 = 0
# 1 & 1 = 1

Section 10.4: Bitwise OR
The | operator will perform a binary "or," where a bit is copied if it exists in either operand.
# 0 | 0 = 0
# 0 | 1 = 1
# 1 | 0 = 1
# 1 | 1 = 1

Section 10.5: Bitwise Left Shift
The << operator will perform a bitwise "left shift," where the left operand's value is moved left by the number of bits
given by the right operand.
# 2 = 0b10
2 << 2
# Out: 8
# 8 = 0b1000
bin(2 << 2)
# Out: 0b1000
Performing a left bit shift of 1 is equivalent to multiplication by 2:

Section 10.6: Bitwise Right Shift:
The >> operator will perform a bitwise "right shift," where the left operand's value is moved right by the number of
bits given by the right operand.
Performing a right bit shift of n is equivalent to integer division by 2**n:


Section 10.7: Inplace Operations:
All of the Bitwise operators (except ~) have their own in place versions

Chapter 11: Boolean Operators
Section 11.1: `and` and `or` are not guaranteed to return a boolean
When you use or, it will either return the first value in the expression if it's true, else it will blindly return the second
value. I.e. or is equivalent to:

For and, it will return its first value if it's false, else it returns the last value:

Section 11.2: A simple example:
if 3.14 < x < 3.142:

Section 11.3: Short-circuit evaluation:

Section 11.4: and
Evaluates to the second argument if and only if both of the arguments are truthy. Otherwise evaluates to the first
falsey argument.

Section 11.5: or
Evaluates to the first truthy argument if either one of the arguments is truthy. If both arguments are falsey,
evaluates to the second argument
Section 11.6: not
It returns the opposite of the following statement:

Chapter 12: Operator Precedence:
Python operators have a set order of precedence, which determines what operators are evaluated first in a
potentially ambiguous expression.

Section 12.1: Simple Operator Precedence Examples in python
Python follows PEMDAS rule. PEMDAS stands for Parentheses, Exponents, Multiplication and Division, and Addition
and Subtraction.




"""