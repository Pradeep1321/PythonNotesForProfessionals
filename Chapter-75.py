"""
Chapter 75: Regular Expressions (Regex)
Python makes regular expressions available through the re module.

Section 75.1: Matching the beginning of a string
The first argument of re.match() is the regular expression, the second is the string to match

A raw string literal has a slightly different syntax than a string literal, namely a backslash \ in a raw string literal
means "just a backslash" and there's no need for doubling up backlashes to escape "escape sequences" such as
newlines (\n), tabs (\t), backspaces (\), form-feeds (\r), and so on. In normal string literals, each backslash must be
doubled up to avoid being taken as the start of an escape sequence.

Section 75.2: Searching

You can also search at the beginning of the string (use ^),
at the end of the string (use $),

Section 75.3: Precompiled patterns
Compiling a pattern allows it to be reused later on in a program. However, note that Python caches recently-used
expressions (docs, SO answer), so "programs that use only a few regular expressions at a time needn’t worry about
compiling regular expressions".

Section 75.4: Flags
For some special cases we need to change the behavior of the Regular Expression, this is done using flags. Flags can
be set in two ways, through the flags keyword or directly in the expression.

Common Flags
Flag                            Short Description
re.IGNORECASE, re.I         Makes the pattern ignore the case
re.DOTALL, re.S             Makes . match everything including newlines
re.MULTILINE, re.M          Makes ^ match the begin of a line and $ the end of a line
re.DEBUG                    Turns on debug information

Inline flags

(?iLmsux) (One or more letters from the set 'i', 'L', 'm', 's', 'u', 'x'.)
The group matches the empty string; the letters set the corresponding flags: re.I (ignore case), re.L (locale
dependent), re.M (multi-line), re.S (dot matches all), re.U (Unicode dependent), and re.X (verbose), for the
entire regular expression. This is useful if you wish to include the flags as part of the regular expression,
instead of passing a flag argument to the re.compile() function.
Note that the (?x) flag changes how the expression is parsed. It should be used first in the expression
string, or after one or more whitespace characters. If there are non-whitespace characters before the flag,
the results are undefined.


Section 75.5: Replacing
Replacements can be made on strings using re.sub.

Section 75.6: Find All Non-Overlapping Matches

Section 75.7: Checking for allowed characters


[^a-zA-Z0-9.]

Section 75.8: Splitting a string using regular expressions

re.split(r'\s+', 'James 94 Samantha 417 Scarlett 74')

Section 75.9: Grouping

Grouping is done with parentheses. Calling group() returns a string formed of the matching parenthesized
subgroups.

match.group() # Group without argument returns the entire match found
# Out: '123'
match.group(0) # Specifying 0 gives the same result as specifying no argument
# Out: '123'
Arguments can also be provided to group() to fetch a particular subgroup

Section 75.10: Escaping Special Characters
Special characters (like the character class brackets [ and ] below) are not matched literally

The re.escape() function escapes all special characters, so it is useful if you are composing a regular expression
based on user input:

Section 75.11: Match an expression only in specific locations
forget_this | or this | and this as well | (but keep this)


"""
import re

#Section 75.1: Matching the beginning of a string
print("------Section 75.1: Matching the beginning of a string---------")

pattern = r"123"
string = "123zzb"
print(re.match(pattern, string))
match = re.match(pattern, string)
print(match.group())

string = "\\t123zzb" # here the backslash is escaped, so there's no tab, just '\' and 't'
pattern = "\\t123" # this will match \t (escaping the backslash) followed by 123
#print(re.match(pattern, string).group()) # no match
print(re.match(pattern, "\t123zzb").group()) # matches '\t123'

pattern = r"\\t123"
print(re.match(pattern, string).group()) # matches '\\t123'

match = re.match(r"(123)", "a123zzb")
print(match is None)
match = re.search(r"(123)", "a123zzb")
print(match.group())

#Section 75.2: Searching
print("-------Section 75.2: Searching----")
pattern = r"(your base)"
sentence = "All your base are belong to us."
match = re.search(pattern, sentence)
print(match.group(1))
match = re.search(r"(belong.*)", sentence)
print(match.group())


match = re.search(r"^123", "123zzb")
match.group(0)
# Out: '123'
match = re.search(r"^123", "a123zzb")
print(match is None)
# Out: True

match = re.search(r"123$", "zzb123")
print(match.group(0))
# Out: '123'
match = re.search(r"123$", "123zzb")
print(match is None)
# Out: True
#or both (use both ^ and $):
match = re.search(r"^123$", "123")
print(match.group(0))
# Out: '123'

#Section 75.3: Precompiled patterns
print("-------Section 75.3: Precompiled patterns----------")

precompiled_pattern = re.compile(r"(\d+)")
matches = precompiled_pattern.search("The answer is 41!")
print(matches.group(1))

precompiled_pattern = re.compile(r"(.*\d+)")
matches = precompiled_pattern.search("The answer is 41!")
print(matches.group(1))
matches = precompiled_pattern.match("The answer is 41!")
print(matches.group(1))

#Section 75.4: Flags
print("------Section 75.4: Flags------")

#Flags keyword
m = re.search("b", "ABC")
print(m is None)
# Out: True
m = re.search("b", "ABC", flags=re.IGNORECASE)
print(m.group())
# Out: 'B'
m = re.search("a.b", "A\nBC", flags=re.IGNORECASE|re.DOTALL)
print(m.group())
# Out: 'A\nB'

#Section 75.5: Replacing
print("----Section 75.5: Replacing------")

#Replacing strings
print(re.sub(r"t[0-9][0-9]", "foo", "my name t13 is t44 what t99 ever t44"))
# Out: 'my name foo is foo what foo ever foo'

#Using group references
print(re.sub(r"t([0-9])([0-9])", r"t\2\1", "t13 t19 t81 t25"))
# Out: 't31 t91 t18 t52'

#However, if you make a group ID like '10', this doesn't work: \10 is read as 'ID number 1 followed by 0'. So you have
#to be more specific and use the \g<i> notation:

print(re.sub(r"t([0-9])([0-9])", r"t\g<2>\g<1>", "t13 t19 t81 t25"))
# Out: 't31 t91 t18 t52'

#Using a replacement function
items = ["zero", "one", "two"]
print(re.sub(r"a\[([0-3])\]", lambda match: items[int(match.group(1))], "Items: a[0], a[1], something,a[2]"))
# Out: 'Items: zero, one, something, two'

#Section 75.6: Find All Non-Overlapping Matches
print("---------Section 75.6: Find All Non-Overlapping Matches------------")
print(re.findall(r"[0-9]{2,3}", "some 1 text 12 is 945 here 4445588899"))

#You could also use re.finditer() which works in the same way as re.findall() but returns an iterator with
#SRE_Match objects instead of a list of strings:
results = re.finditer(r"([0-9]{2,3})", "some 1 text 12 is 945 here 4445588899")
for result in results:
    print(result.group(0))

#Section 75.7: Checking for allowed characters
print("-----Section 75.7: Checking for allowed characters--------")

#Section 75.9: Grouping
print("-------Section 75.9: Grouping------")
sentence = "This is a phone number 672-123-456-9910"
pattern = r".*(phone).*?([\d-]+)"
match = re.match(pattern, sentence)
match.groups() # The entire match as a list of tuples of the paranthesized subgroups
# Out: ('phone', '672-123-456-9910')
m.group() # The entire match as a string
# Out: 'This is a phone number 672-123-456-9910'
m.group(0) # The entire match as a string
# Out: 'This is a phone number 672-123-456-9910'
#m.group(1) # The first parenthesized subgroup.
# Out: 'phone'
#m.group(2) # The second parenthesized subgroup.
# Out: '672-123-456-9910'
#m.group(1, 2) # Multiple arguments give us a tuple.
# Out: ('phone', '672-123-456-9910')

#Named groups
match = re.search(r'My name is (?P<name>[A-Za-z ]+)', 'My name is John Smith')
print(match.group('name'))
#Creates a capture group that can be referenced by name as well as by index.
#Non-capturing groups
#Using (?:) creates a group, but the group isn't captured. This means you can use it as a group, but it won't pollute
#your "group space".
print(re.match(r'(\d+)(\+(\d+))?', '11+22').groups())
print(re.match(r'(\d+)(?:\+(\d+))?', '11+22').groups())

#Section 75.10: Escaping Special Characters
print("-------Section 75.10: Escaping Special Characters---------")
match = re.search(r'[b]', 'a[b]c')
print(match.group())
match = re.search(r'\[b\]', 'a[b]c')
print(match.group())
print(re.escape('a[b]c'))
match = re.search(re.escape('a[b]c'), 'a[b]c')
print(match.group())
username = 'A.C.' # suppose this came from the user
re.findall(r'Hi {}!'.format(username), 'Hi A.C.! Hi ABCD!')
# Out: ['Hi A.C.!', 'Hi ABCD!']
re.findall(r'Hi {}!'.format(re.escape(username)), 'Hi A.C.! Hi ABCD!')
# Out: ['Hi A.C.!']

#Section 75.11: Match an expression only in specific locations
print("-----Section 75.11: Match an expression only in specific locations--------")

import regex as re
string = "An apple a day keeps the doctor away (I eat an apple everyday)."
rx = re.compile(r'''\([^()]*\) (*SKIP)(*FAIL) # match anything in parentheses and "throw it away"
                    | # or = apple 
                    # match an apple
''', re.VERBOSE)