"""
Chapter 29: Basic Input and Output

Section 29.1: Using the print function
In Python 3, print functionality is in the form of a function:
Python 2.x Version ≥ 2.3
In Python 2, print was originally a statement, as shown below.

Note: using from __future__ import print_function in Python 2 will allow users to use the print() function the
same as Python 3 code. This is only available in Python 2.6 and above.


Section 29.2: Input from a File

Files can be opened using the built-in function open.Using a with <command> as
<name> syntax (called a 'Context Manager') makes using open and getting a handle for the file super easy

with open('somefile.txt', 'r') as fileobj:
    # write code here using fileobj

If you want to read that file as bytes use rb.
o append data to an existing file use a. Use
w to create a file or overwrite any existing files of the same name. You can use r+ to open a file for both reading and
writing. The first argument of open() is the filename, the second is the mode. If mode is left blank, it will default to
r.
When fileobj are first opened the file handle points to the very beginning of the file, which is the position 0. The file handle can display its
current position with tell:

The file handler position can be set to whatever is needed:
fileobj.seek(7)


# reads the next 4 characters
# starting at the current position
next4 = fileobj.read(4)



To demonstrate the difference between characters and bytes:
with open('shoppinglist.txt', 'r') as fileobj:
print(type(fileobj.read())) # <class 'str'>
with open('shoppinglist.txt', 'rb') as fileobj:
print(type(fileobj.read())) # <class 'bytes'>

Section 29.3: Read from stdin
Be aware that sys.stdin is a stream. It means that the for-loop will only terminate when the stream has ended.
You can now pipe the output of another program into your python program as follows:
    $ cat myfile | python myprogram.py
In this example cat myfile can be any unix command that outputs to stdout


Section 29.4: Using input() and raw_input()
Python 2.x Version ≥ 2.3
raw_input will wait for the user to enter text and then return the result as a string.
    foo = raw_input("Put a message here that asks the user for input")

Python 3.x Version ≥ 3.0
input will wait for the user to enter text and then return the result as a string.
foo = input("Put a message here that asks the user for input")

Section 29.5: Function to prompt user for a number

Section 29.6: Printing a string without a newline at the end

In Python 2.x, to continue a line with print, end the print statement with a comma. It will automatically add a
space.
print "Hello,",
print "World!"
# Hello, World!
Python 3.x Version ≥ 3.0
In Python 3.x, the print function has an optional end parameter that is what it prints at the end of the given string.
By default it's a newline character, so equivalent to this:
print("Hello, ", end="\n")
print("World!")
# Hello,
# World!


Chapter 30: Files & Folders I/O
Parameter           Details
fil ename           the path to your file or, if the file is in the working directory, the filename of your file
access_mode         a string value that determines how the file is opened
buffering           an integer value used for optional line buffering

Section 30.1: File modes
There are different modes you can open a file with, specified by the mode parameter. These include:
'r' - reading mode. The default. It allows you only to read the file, not to modify it. When using this mode the
file must exist.
'w' - writing mode. It will create a new file if it does not exist, otherwise will erase the file and allow you to
write to it.
'a' - append mode. It will write data to the end of the file. It does not erase the file, and the file must exist for
this mode.
'rb' - reading mode in binary. This is similar to r except that the reading is forced in binary mode. This is
also a default choice.
'r+' - reading mode plus writing mode at the same time. This allows you to read and write into files at the
same time without having to use r and w.
'rb+' - reading and writing mode in binary. The same as r+ except the data is in binary
'wb' - writing mode in binary. The same as w except the data is in binary.
'w+' - writing and reading mode. The exact same as r+ but if the file does not exist, a new one is made.
Otherwise, the file is overwritten.
'wb+' - writing and reading mode in binary mode. The same as w+ but the data is in binary.
'ab' - appending in binary mode. Similar to a except that the data is in binary.
'a+' - appending and reading mode. Similar to w+ as it will create a new file if the file does not exist.
Otherwise, the file pointer is at the end of the file if it exists.
'ab+' - appending and reading mode in binary. The same as a+ except that the data is in binary.


Python 3 added a new mode for exclusive creation so that you will not accidentally truncate or overwrite and
existing file.
'x' - open for exclusive creation, will raise FileExistsError if the file already exists
'xb' - open for exclusive creation writing mode in binary. The same as x except the data is in binary.
'x+' - reading and writing mode. Similar to w+ as it will create a new file if the file does not exist. Otherwise,
will raise FileExistsError.
'xb+' - writing and reading mode. The exact same as x+ but the data is binary

Python 3.x Version ≥ 3.3
try:
    with open("fname", "r") as fout:
        # Work with your open file
    except FileExistsError:
        # Your error handling goes here

In Python 2 you would have done something like
Python 2.x Version ≥ 2.0
import os.path
if os.path.isfile(fname):
    with open("fname", "w") as fout:
        # Work with your open file
else:
    # Your error handling goes here

Section 30.2: Reading a file line-by-line
Using the for loop iterator and readline() together is considered bad practice.
More commonly, the readlines() method is used to store an iterable collection of the file's lines:

Section 30.3: Iterate files (recursively)
To iterate all files, including in sub directories, use os.walk:
If you also wish to get information about the file, you may use the more efficient method os.scandir

Section 30.4: Getting the full contents of a file
The preferred method of file i/o is to use the with keyword. This will ensure the file handle is closed once the
reading or writing has been completed.


Section 30.5: Writing to a file
Python doesn't automatically add line breaks, you need to do that manually:
Do not use os.linesep as a line terminator when writing files opened in text mode (the default); use \n instead.

If you want to specify an encoding, you simply add the encoding parameter to the open function:
with open('my_file.txt', 'w', encoding='utf-8') as f:

We can print and write to a file
in python 3
with open('fred.txt', 'w') as outfile:
    s = "I'm Not Dead Yet!"
    print(s, file = outfile) # writes to outfile
    myfile = None
    print(s, file = myfile) # writes to stdout
    print(s, file = None) # writes to stdout


Python 2.x Version ≥ 2.0
outfile = open('fred.txt', 'w')
s = "I'm Not Dead Yet!"
print s # writes to stdout
print >> outfile, s # writes to outfile

Section 30.6: Check whether a file or path exists

Section 30.7: Random File Access Using mmap
Using the mmap module allows the user to randomly access locations in a file by mapping the file into memory. This
is an alternative to using normal file operations.

import mmap
with open('filename.ext', 'r') as fd:
    # 0: map the whole file
    mm = mmap.mmap(fd.fileno(), 0)
    # print characters at indices 5 through 10
    print mm[5:10]

Section 30.8: Replacing text in a file
for line in fileinput.input('filename.txt', inplace=True):

Section 30.9: Checking if a file is empty

Section 30.10: Read a file between a range of lines
You can make use of itertools for that
for line in itertools.islice(f, 12, 30):
This will read through the lines 13 to 20 as in python indexing starts from 0. So line number 1 is indexed as 0

Section 30.11: Copy a directory tree
import shutil
source='//192.168.1.2/Daily Reports'
destination='D:\\Reports\\Today'
shutil.copytree(source, destination)
The destination directory must not exist already


Section 30.12: Copying contents of one file to a dierent file
import shutil
shutil.copyfile(src, dst)

Chapter 31: os.path
The path parameters can be passed as either
strings, or bytes. Applications are encouraged to represent file names as (Unicode) character strings.

Section 31.1: Join Paths
import os
os.path.join('a', 'b', 'c')

Section 31.2: Path Component Manipulation

Section 31.3: Get the parent directory

Section 31.4: If the given path exists
os.path.exists(path)

Section 31.5: check if the given path is a directory, file,
symbolic link, mount point etc

to check if the given path is a directory
os.path.isdir(dirname)

to check if the given path is a file
os.path.isfile(filename)

symlink = dirname + 'some_sym_link'
os.path.islink(symlink)

to check if the given path is a mount point
os.path.ismount(mount_path)

Section 31.6: Absolute Path from Relative Path
Use os.path.abspath
os.getcwd()
os.path.abspath('foo')
os.path.abspath('../foo')
os.path.abspath('/foo')




"""

#Section 29.3: Read from stdin

import sys
import fileinput

#for line in sys.stdin:
#    print(line)


#for line in fileinput.input():
#    process(line)
