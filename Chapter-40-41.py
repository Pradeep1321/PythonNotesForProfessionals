'''
Chapter 40: String Formatting

Section 40.1: Basics of String Formatting
You can use str.format to format output. Bracket pairs are replaced with arguments in the order in which the
arguments are passed:

print('{}, {} and {}'.format(foo, bar, baz))

Indexes can also be specified inside the brackets. The numbers correspond to indexes of the arguments passed to
the str.format function (0-based).

print('{0}, {1}, {2}, and {1}'.format(foo, bar, baz))

Named arguments can be also used:
print("X value is: {x_val}. Y value is: {y_val}.".format(x_val=2, y_val=3))

Object attributes can be referenced when passed into str.format

Dictionary keys can be used as well:

Note: In addition to str.format, Python also provides the modulo operator %--also known as the string
formatting or interpolation operator. str.format is a successor of %
and it offers greater flexibility, for instance by making it easier to carry out multiple substitutions

you can also include a format specification inside the curly brackets: preceded by a colon (:).
:~^20 (^ stands for center
alignment, total width 20, fill with ~ character):
'{:~^20}'.format('centered')

Section 40.2: Alignment and padding

Python 2.x Version ≥ 2.6
The format() method can be used to change the alignment of the string. You have to do it with a format expression
of the form :[fill_char][align_operator][width] where align_operator is one of:
< forces the field to be left-aligned within width.
> forces the field to be right-aligned within width.
^ forces the field to be centered within width.
= forces the padding to be placed after the sign (numeric types only).
fill_char (if omitted default is whitespace) is the character used for the padding.


Section 40.3: Format literals (f-string)
Literal format strings were introduced in PEP 498 (Python3.6 and upwards), allowing you to prepend f to the
beginning of a string literal to effectively apply .format to it with all variables in the current scope.

Note: The f'' does not denote a particular type like b'' for bytes or u'' for unicode in python2. The formatting is
immediately applied, resulting in a normal string.

Section 40.5: Named placeholders
Format strings may contain named placeholders that are interpolated using keyword arguments to format.

Using a dictionary (Python 2.x)
    data = {'first': 'Hodor', 'last': 'Hodor!'}
    print('{first} {last}'.format(**data))
Using a dictionary (Python 3.2+)
    print('{first} {last}'.format_map(data))

str.format_map allows to use dictionaries without having to unpack them first. Also the class of data (which might
be a custom type) is used instead of a newly filled dict.

Section 40.6: String formatting with datetime
Any class can configure its own string formatting syntax through the __format__ method. A type in the standard
Python library that makes handy use of this is the datetime type, where one can use strftime-like formatting
codes directly within str.format:

'North America: {dt:%m/%d/%Y}. ISO: {dt:%Y-%m-%d}.'.format(dt=datetime.now())

Section 40.7: Formatting Numerical Values

Section 40.8: Nested formatting

Section 40.9: Format using Getitem and Getattr
Any data structure that supports __getitem__ can have their nested structure formatted:

Section 40.10: Padding and truncating strings, combined

Section 40.11: Custom formatting for a class
For every value which is passed to the format function, Python looks for a __format__ method for that argument.
Your own custom class can therefore have their own __format__ method to determine how the format function will
display and format your class and it's attributes.

This is different than the __str__ method, as in the __format__ method you can take into account the formatting
language, including alignment, field width etc, and even (if you wish) implement your own format specifiers, and
your own formatting language extensions

object.__format__(self, format_spec)

If your custom class does not have a custom __format__ method and an instance of the class is passed to
the format function, Python2 will always use the return value of the __str__ method or __repr__
method to determine what to print (and if neither exist then the default repr will be used), and you will
need to use the s format specifier to format this. With Python3, to pass your custom class to the format
function, you will need define __format__ method on your custom class.


Chapter 41: String Methods

Section 41.1: Changing the capitalization of a string

str.casefold
str.upper
str.lower
str.capitalize
str.title
str.swapcase

Python 3.x Version ≥ 3.3
str.casefold()

str.casefold creates a lowercase string that is suitable for case insensitive comparisons. This is more aggressive
than str.lower and may modify strings that are already in lowercase or cause strings to grow in length, and is not
intended for display purposes.

"XßΣ".casefold()
# 'xssσ'

"XßΣ".lower()
# 'xßς'

str.upper("This is a 'string'")
# "THIS IS A 'STRING'"

This is most useful when applying one of these methods to many strings at once in say, a map function.
map(str.upper,["These","are","some","'strings'"])
# ['THESE', 'ARE', 'SOME', "'STRINGS'"]

Section 41.2: str.translate: Translating characters in a string
Python supports a translate method on the str type which allows you to specify the translation table (used for
replacements) as well as any characters which should be deleted in the process.
str.translate(table[, deletechars])
Parameter         Description
table               It is a lookup table that defines the mapping from one character to another.
deletechars         A list of characters which are to be removed from the string.

The maketrans method (str.maketrans in Python 3 and string.maketrans in Python 2) allows you to generate a
translation table.

Section 41.3: str.format and f-strings: Format values into a string
Python provides string interpolation and formatting functionality through the str.format function, introduced in
version 2.6 and f-strings introduced in version 3.6.

Python also supports C-style qualifiers for string formatting

Section 41.4: String module's useful constants
Python's string module provides constants for string related operations. To use them, import the string module:

Section 41.5: Stripping unwanted leading/trailing characters from a string

Section 41.6: Reversing a string

Section 41.7: Split a string based on a delimiter into a list of strings
str.split(sep=None, maxsplit=-1)
If sep isn't provided, or is None, then the splitting takes place wherever there is whitespace. However, leading and
trailing whitespace is ignored, and multiple consecutive whitespace characters are treated the same as a single
whitespace character:

Section 41.8: Replace all occurrences of one substring with another substring
str.replace(old, new[, count]):

Section 41.9: Testing what a string is composed of
These are str.isalpha, str.isdigit, str.isalnum, str.isspace. Capitalization can be tested with str.isupper,
str.islower and str.istitle.
Bytestrings (bytes in Python 3, str in Python 2), only support isdigit, which only checks for basic ASCII digits.

str.isalnum
This is a combination of str.isalpha and str.isnumeric, specifically it evaluates to True if all characters in the
given string are alphanumeric, that is, they consist of alphabetic or numeric characters:

Section 41.10: String Contains
Python makes it extremely intuitive to check if a string contains a given substring. Just use the in operator:
"foo" in "foo.baz.bar" --> True

Section 41.11: Join a list of strings into one string
" ".join(["once","upon","a","time"])
"---".join(["once", "upon", "a", "time"])

Section 41.12: Counting number of times a substring appears in a string
One method is available for counting the number of occurrences of a sub-string in another string, str.count

str.count(sub[, start[, end]])

Section 41.13: Case insensitive string comparisons
The first thing to note it that case-removing conversions in unicode aren't trivial. There is text for which
text.lower() != text.upper().lower(), such as "ß":

But let's say you wanted to caselessly compare "BUSSE" and "Buße". You probably also want to compare "BUSSE"
and "BU􀀀E" equal - that's the newer capital form. The recommended way is to use casefold:

Python 3.x Version ≥ 3.3
>>> help(str.casefold)
Help on method_descriptor:
casefold(...)
    S.casefold() -> str
    Return a version of S suitable for caseless comparisons.

Do not just use lower. If casefold is not available, doing .upper().lower() helps (but only somewhat).

Then you should consider accents. If your font renderer is good, you probably think "ê" == "ê" - but it doesn't:
>>> "ê" == "ê"
False

This is because they are actually

>>> import unicodedata
>>> [unicodedata.name(char) for char in "ê"]
['LATIN SMALL LETTER E WITH CIRCUMFLEX']
>>> [unicodedata.name(char) for char in "ê"]
['LATIN SMALL LETTER E', 'COMBINING CIRCUMFLEX ACCENT']
The simplest way to deal with this is unicodedata.normalize. You probably want to use NFKD normalization, but
feel free to check the documentation. Then one does
>>> unicodedata.normalize("NFKD", "ê") == unicodedata.normalize("NFKD", "ê")
True
import unicodedata
def normalize_caseless(text):
    return unicodedata.normalize("NFKD", text.casefold())
def caseless_equal(left, right):
    return normalize_caseless(left) == normalize_caseless(right)

Section 41.14: Justify strings
ljust and rjust are very similar. Both have a width parameter and an optional fillchar parameter

print('{} -> {} mi. ({} km.)'.format(str(road).rjust(4), str(miles).ljust(4),
str(kms).ljust(4)))

Section 41.15: Test the starting and ending characters of a string
In order to test the beginning and ending of a given string in Python, one can use the methods str.startswith()
and str.endswith().

str.startswith(prefix[, start[, end]])

Section 41.16: Conversion between str or bytes data and unicode characters
The contents of files and network messages may represent encoded characters. They often need to be converted to
unicode for proper display.

In Python 2, you may need to convert str data to Unicode characters. The default ('', "", etc.) is an ASCII string, with
any values outside of ASCII range displayed as escaped values. Unicode strings are u'' (or u"", etc.).

Python 2.x Version ≥ 2.3
# You get "© abc" encoded in UTF-8 from a file, network, or other data source

s = '\xc2\xa9 abc'  # s is a byte array, not a string of characters
                    # Doesn't know the original was UTF-8
                    # Default form of string literals in Python 2
s[0] # '\xc2' - meaningless byte (without context such as an encoding)
type(s) # str - even though it's not a useful one w/o having a known encoding

u = s.decode('utf-8') # u'\xa9 abc'
                        # Now we have a Unicode string, which can be read as UTF-8 and printed properly
                        # In Python 2, Unicode string literals need a leading u
                        # str.decode converts a string which may contain escaped bytes to a Unicode
u[0]            # u'\xa9' - Unicode Character 'COPYRIGHT SIGN' (U+00A9) '©'
type(u)         # unicode

u.encode('utf-8')       # '\xc2\xa9 abc'
                        # unicode.encode produces a string with escaped bytes for non-ASCII characters

In Python 3 you may need to convert arrays of bytes (referred to as a 'byte literal') to strings of Unicode characters.
The default is now a Unicode string, and bytestring literals must now be entered as b'', b"", etc. A byte literal will
return True to isinstance(some_val, byte), assuming some_val to be a string that might be encoded as bytes.

Python 3.x Version ≥ 3.0
# You get from file or network "© abc" encoded in UTF-8

s = b'\xc2\xa9 abc'         # s is a byte array, not characters
                            # In Python 3, the default string literal is Unicode; byte array literals need a leading b

s[0] # b'\xc2' - meaningless byte (without context such as an encoding)
type(s) # bytes - now that byte arrays are explicit, Python can show that.

u = s.decode('utf-8')           # '© abc' on a Unicode terminal
                                # bytes.decode converts a byte array to a string (which will, in Python 3, be Unicode)

u[0]        # '\u00a9' - Unicode Character 'COPYRIGHT SIGN' (U+00A9) '©'
type(u)     # str
            # The default string literal in Python 3 is UTF-8 Unicode

u.encode('utf-8')           # b'\xc2\xa9 abc'
                            # str.encode produces a byte array, showing ASCII-range bytes as unescaped characters.


'''
import string
#Object attributes can be referenced when passed into str.format
class AssignValue(object):
    def __init__(self, value):
        self.value = value

my_value = AssignValue(6)
print('My value is: {0.value}'.format(my_value)) # "0" is optional
# Out: "My value is: 6"

#Dictionary keys can be used as well:
my_dict = {'key': 6, 'other_key': 7}
print("My other key is: {0[other_key]}".format(my_dict)) # "0" is optional
# Out: "My other key is: 7"

#Same applies to list and tuple indices:
my_list = ['zero', 'one', 'two']
print("2nd element is: {0[2]}".format(my_list))

t = (12, 45, 22222, 103, 6)
print('{0} {2} {1} {2} {3} {2} {4} {2}'.format(*t))
# Out: 12 22222 45 22222 103 22222 6 22222

#As format is a function, it can be used as an argument in other functions

number_list = [12,45,78]
print(map('the number is {}'.format, number_list))
# Out: ['the number is 12', 'the number is 45', 'the number is 78']

from datetime import datetime,timedelta

once_upon_a_time = datetime(2010, 7, 1, 12, 0, 0)
delta = timedelta(days=13, hours=8, minutes=20)
gen = (once_upon_a_time + x * delta for x in range(5))
print('\n'.join(map('{:%Y-%m-%d %H:%M:%S}'.format, gen)))

#Section 40.2: Alignment and padding

print("-----Section 40.3: Format literals (f-string)-----")
foo = 'bar'
print(f'Foo is {foo}')
print(f'{foo:^7s}')

price = 478.23
print(f"{f'${price:0.2f}':*>20s}")


#The expressions in an f-string are evaluated in left-to-right order. This is detectable only if the expressions have side effects:
def fn(l, incr):
    result = l[0]
    l[0] += incr
    return result

lst = [0]
print(f'{fn(lst,2)} {fn(lst,3)}')
print( f'{fn(lst,2)} {fn(lst,3)}')
print(lst)

#Section 40.4: Float formatting
print('{0:.0f}'.format(42.12345))
print('{0:.1f}'.format(42.12345))
print('{0:.3f}'.format(42.12345))

#Floating point numbers can also be formatted in scientific notation or as percentages:
print('{0:.3e}'.format(42.12345))

#You can also combine the {0} and {name} notations. This is especially useful when you want to round all variables
#to a pre-specified number of decimals with 1 declaration:
s = 'Hello'
a, b, c = 1.12345, 2.34567, 34.5678
digits = 2
print('{0}! {1:.{n}f}, {2:.{n}f}, {3:.{n}f}'.format(s, a, b, c, n=digits))

#Section 40.5: Named placeholders


#Section 40.7: Formatting Numerical Values
print('{:c}'.format(65)) # Unicode character
print('{:d}'.format(0x0a)) # base 10
print('{:n}'.format(0x0a)) # base 10 using current locale for separators

#Format integers to different bases (hex, oct, binary)
print('{0:x}'.format(10)) # base 16, lowercase - Hexadecimal
print('{0:X}'.format(10)) # base 16, uppercase - Hexadecimal
print('{:o}'.format(10)) # base 8 - Octal
print('{:b}'.format(10))# base 2 - Binary
print('{0:#b}, {0:#o}, {0:#x}'.format(42)) # With prefix
print('8 bit: {0:08b}; Three bytes: {0:06x}'.format(42)) # Add zero padding

#Use formatting to convert an RGB float tuple to a color hex string:
r, g, b = (1.0, 0.4, 0.0)
print('#{:02X}{:02X}{:02X}'.format(int(255 * r), int(255 * g), int(255 * b)))

#Only integers can be converted:
#print('{:x}'.format(42.0)) # will not work as x is used for base 16

#Section 40.8: Nested formatting
print('{:.>10}'.format('foo'))
print('{:.>{}}'.format('foo', 10))
print('{:{}{}{}}'.format('foo', '*', '^', 15))

data = ["a", "bbbbbbb", "ccc"]
m = max(map(len, data))
for d in data:
    print('{:>{}}'.format(d, m))

#Section 40.9: Format using Getitem and Getattr
person = {'first': 'Arthur', 'last': 'Dent'}
print('{p[first]} {p[last]}'.format(p=person))

#Object attributes can be accessed using getattr():
class Person(object):
    first = 'Zaphod'
    last = 'Beeblebrox'
print('{p.first} {p.last}'.format(p=Person()))


#Section 40.10: Padding and truncating strings, combined
#s = \"\"\"
#print(s.format(a="1"*1, c="3"*3, e="5"*5))

#Section 40.11: Custom formatting for a class


#Section 40.11: Custom formatting for a class
class Example(object):
    def __init__(self,a,b,c):
        self.a, self.b, self.c = a,b,c
    def __format__(self, format_spec):
        """ Implement special semantics for the 's' format specifier """
        # Reject anything that isn't an s
        if format_spec[-1] != 's':
            raise ValueError('{} format specifier not understood for this object',
            format_spec[:-1])
        # Output in this example will be (<a>,<b>,<c>)
        raw = "(" + ",".join([str(self.a), str(self.b), str(self.c)]) + ")"
        # Honor the format language by using the inbuilt string format
        # Since we know the original format_spec ends in an 's'
        # we can take advantage of the str.format method with a
        # string argument we constructed above
        return "{r:{f}}".format( r=raw, f=format_spec )

inst = Example(1,2,3)
print("{0:>20s}".format(inst))

#Section 41.2: str.translate: Translating characters in a string
#The translate method returns a string which is a translated copy of the original string.

translation_table = str.maketrans("aeiou", "12345")
my_string = "This is a string!"
translated = my_string.translate(translation_table)
print(translated)

#You can set the table argument to None if you only need to delete characters
#print('this syntax is very useful'.translate(None, 'aeiou'))

#Section 41.3: str.format and f-strings: Format values into a string
i = 10
f = 1.5
s = "foo"
l = ['a', 1, 2]
d = {'a': 1, 2: 'foo'}
#The following statements are all equivalent
print("{} {} {} {} {}".format(i, f, s, l, d))
print(str.format("{} {} {} {} {}", i, f, s, l, d))
print("{0} {1} {2} {3} {4}".format(i, f, s, l, d))
print("{0:d} {1:0.1f} {2} {3!r} {4!r}".format(i, f, s, l, d))
print("{i:d} {f:0.1f} {s} {l!r} {d!r}".format(i=i, f=f, s=s, l=l, d=d))
print(f"{i} {f} {s} {l} {d}")
print(f"{i:d} {f:0.1f} {s} {l!r} {d!r}")

print("Python also supports C-style qualifiers for string formatting")
print("%d %0.1f %s %r %r" % (i, f, s, l, d))
print("%(i)d %(f)0.1f %(s)s %(l)r %(d)r" % dict(i=i, f=f, s=s, l=l, d=d))

#str.format can also be numbered to reduce duplication when formatting strings
print("str.format can also be numbered to reduce duplication when formatting strings")
print("I am from {}. I love cupcakes from {}!".format("Australia", "Australia"))
print("I am from {0}. I love cupcakes from {0}!".format("Australia"))

#the { and } characters can be escaped by using double brackets
print("the { and } characters can be escaped by using double brackets")

print("{'a': 5, 'b': 6}")
print("{{'{}': {}, '{}': {}}}".format("a", 5, "b", 6))
print(f"{{'{'a'}': {5}, '{'b'}': {6}}}")

#Section 41.4: String module's useful constants
print("--*4 Section 41.4: String module's useful constants --*4")

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
print(string.whitespace)
print(string.printable)

#Section 41.5: Stripping unwanted leading/trailing characters from a string
print("-------Section 41.5: Stripping unwanted leading/trailing characters from a string-----------")

print(" a line with leading and trailing space ".strip())
print(">>> a Python prompt".strip('> '))
print(" spacious string ".rstrip())
print(" spacious string ".rstrip())

#Section 41.6: Reversing a string
print("--------Section 41.6: Reversing a string--------")
print(''.join(reversed('hello')))

#Section 41.7: Split a string based on a delimiter into a list of strings
print("-----Section 41.7: Split a string based on a delimiter into a list of strings ------")

print("This is a sentence.".split())
print(" This is a sentence. ".split())
print("     ".split())
print("This is a sentence.".split(' '))
print("Earth,Stars,Sun,Moon".split(','))
print(" This is a sentence. ".split(' '))
print("This is a sentence.".split('e'))
print("This is a sentence.".split('en'))

print("This is a sentence.".split('e', maxsplit=0))
print("This is a sentence.".split('e', maxsplit=1))
print("This is a sentence.".split('e', maxsplit=-1))

print("This is a sentence.".rsplit('e', maxsplit=1))
print("This is a sentence.".rsplit('e', maxsplit=2))

#Section 41.8: Replace all occurrences of one substring with another substring
print("-----Section 41.8: Replace all occurrences of one substring with another substring ---------")

print("It can foo multiple examples of foo if you want.".replace('foo', 'spam'))
print("It can foo multiple examples of foo if you want, \
... or you can limit the foo with the third argument.".replace('foo', 'spam', 1))

#Section 41.9: Testing what a string is composed of
print("-------Section 41.9: Testing what a string is composed of--------------")


#Section 41.12: Counting number of times a substring appears in a string
print("Section 41.12: Counting number of times a substring appears in a string")

s = "She sells seashells by the seashore."
print(s.count("sh"))
print(s.count("se"))
print(s.count("sea"))
print(s.count("seashells"))
print(s.count("sea", 13))

#Section 41.13: Case insensitive string comparisons
print("--------------Section 41.13: Case insensitive string comparisons-------")

#Section 41.15: Test the starting and ending characters of a string

print("------Section 41.15: Test the starting and ending characters of a string--------")
s = "This is a test string"
print(s.startswith("Thi"))
print(s.startswith("thi"))

print(s.startswith("is", 2))

#You can also use a tuple to check if it starts with any of a set of strings
print(s.startswith(('This', 'That')))

s = "this ends in a full stop."
print(s.endswith('.'))

print(s.endswith('stop.'))

#You can also use a tuple to check if it ends with any of a set of strings
print(s.endswith(('.', 'something')))

#Section 41.16: Conversion between str or bytes data and unicode characters
print("------Section 41.16: Conversion between str or bytes data and unicode characters------")


