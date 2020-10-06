"""
Chapter 74: The Print Function
Section 74.1: Print basics
In Python 3 and higher, print is a function rather than a keyword.

Another way to print multiple parameters is by using a +
print(str(foo) + " " + bar + " " + str(baz))

You can prevent the print function from automatically printing a newline by using the end parameter:

Section 74.2: Print parameters
Argument sep: place a string between arguments.
print('apples','bananas', 'cherries', sep=', ')

Argument end: use something other than a newline at the end
Without the end argument, all print() functions write a line and then go to the beginning of the next line. You can
change it to do nothing (use an empty string of ''), or double spacing between paragraphs by using two newlines

There is a fourth parameter flush which will forcibly flush the stream.

"""
import sys
print('apples','bananas', 'cherries', sep=', ')

#Argument end: use something other than a newline at the end

def sendit(out, *values, sep=' ', end='\n'):
    print(*values, sep=sep, end=end, file=out)

sendit(sys.stdout, 'apples', 'bananas', 'cherries', sep='\t')
with open("delete-me.txt", "w+") as f:
    sendit(f, 'apples', 'bananas', 'cherries', sep=' ', end='\n')

with open("delete-me.txt", "rt") as f:
    print(f.read())


