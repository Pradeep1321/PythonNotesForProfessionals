"""
Chapter 57: The dis module
Python is a hybrid interpreter. When running a program, it first assembles it into bytecode which can then be run in
the Python interpreter (also called a Python virtual machine). The dis module in the standard library can be used to
make the Python bytecode human-readable by disassembling classes, methods, functions, and code objects.s

The Python interpreter is stack-based and uses a first-in last-out system.

Each operation code (opcode) in the Python assembly language (the bytecode) takes a fixed number of items from
the stack and returns a fixed number of items to the stack. If there aren't enough items on the stack for an opcode,
the Python interpreter will crash, possibly without an error message.


Section 57.2: Constants in the dis module

EXTENDED_ARG = 145 # All opcodes greater than this have 2 operands
HAVE_ARGUMENT = 90 # All opcodes greater than this have at least 1 operands

cmp_op = ('<', '<=', '==', '!=', '>', '>=', 'in', 'not in', 'is', 'is ...
# A list of comparator id's. The indices are used as operands in some opcodes

# All opcodes in these lists have the respective types as there operands
hascompare = [107]
hasconst = [100]
hasfree = [135, 136, 137]
hasjabs = [111, 112, 113, 114, 115, 119]
hasjrel = [93, 110, 120, 121, 122, 143]
haslocal = [124, 125, 126]
hasname = [90, 91, 95, 96, 97, 98, 101, 106, 108, 109, 116]
# A map of opcodes to ids
opmap = {'BINARY_ADD': 23, 'BINARY_AND': 64, 'BINARY_DIVIDE': 21, 'BIN...
# A map of ids to opcodes
opname = ['STOP_CODE', 'POP_TOP', 'ROT_TWO', 'ROT_THREE', 'DUP_TOP', '...


Section 57.3: Disassembling modules
To disassemble a Python module, first this has to be turned into a .pyc file (Python compiled)
python -m compileall <file>.py

import dis
import marshal
with open("<file>.pyc", "rb") as code_f:
    code_f.read(8) # Magic number and modification time
    code = marshal.load(code_f) # Returns a code object which can be disassembled
    dis.dis(code) # Output the disassembly

This will compile a Python module and output the bytecode instructions with dis. The module is never imported so
it is safe to use with untrusted code.

Chapter 58: The base64 Module
Base 64 encoding represents a common scheme for encoding binary into ASCII string format using radix 64. The
base64 module is part of the standard library, which means it installs along with Python. Understanding of bytes
and strings is critical to this topic and can be reviewed here. This topic explains how to use the various features and
number bases of the base64 module.

Parameter                                                       Description
base64.b64encode(s, altchars=None)
s                                           A bytes-like object
altchars                                    A bytes-like object of length 2+ of characters to replace the
                                            '+' and '=' characters when creating the Base64 alphabet.
                                            Extra characters are ignored.
base64.b64decode(s, altchars=None,
validate=False)
s                                           A bytes-like object
altchars
                                            A bytes-like object of length 2+ of characters to replace the
                                            '+' and '=' characters when creating the Base64 alphabet.
                                            Extra characters are ignored.
validate                                    If validate is True, the characters not in the normal Base64
                                            alphabet or the alternative alphabet are not discarded
                                            before the padding check
base64.standard_b64encode(s)
s                                           A bytes-like object
base64.standard_b64decode(s)
s                                           A bytes-like object
base64.urlsafe_b64encode(s)
s                                           A bytes-like object
base64.urlsafe_b64decode(s)
s                                           A bytes-like object
b32encode(s)
s                                           A bytes-like object
b32decode(s)
s                                           A bytes-like object
base64.b16encode(s)
s                                           A bytes-like object
base64.b16decode(s)
s                                           A bytes-like object
base64.a85encode(b, foldspaces=False,
wrapcol=0, pad=False, adobe=False)
b                                           A bytes-like object
foldspaces                                  If foldspaces is True, the character 'y' will be used instead
                                            of 4 consecutive spaces.
wrapcol                                     The number characters before a newline (0 implies no newlines)
pad                                         If pad is True, the bytes are padded to a multiple of 4 before encoding
adobe                                       If adobe is True, the encoded sequenced with be framed
                                            with '<~' and ''~>' as used with Adobe products
base64.a85decode(b, foldspaces=False,
adobe=False, ignorechars=b'\t\n\r\v')
b                                           A bytes-like object
foldspaces                                  If foldspaces is True, the character 'y' will be used instead
                                            of 4 consecutive spaces.
adobe                                       If adobe is True, the encoded sequenced with be framed
                                            with '<~' and ''~>' as used with Adobe products
ignorechars                                 A bytes-like object of characters to ignore in the encoding process

base64.b85encode(b, pad=False)
b                                           A bytes-like object
pad                                         If pad is True, the bytes are padded to a multiple of 4 before encoding
base64.b85decode(b)
b                                           A bytes-like object

Section 58.1: Encoding and Decoding Base64
To include the base64 module in your script, you must import it first:

The base64 encode and decode functions both require a bytes-like object. To get our string into bytes, we must
encode it using Python's built in encode function. Most commonly, the UTF-8 encoding is used, however a full list of
these standard encodings (including languages with different characters) can be found here in the official Python
Documentation

Section 58.2: Encoding and Decoding Base32
The base64 module also includes encoding and decoding functions for Base32. These functions are very similar to
the Base64 functions:

Section 58.3: Encoding and Decoding Base16
The base64 module also includes encoding and decoding functions for Base16. Base 16 is most commonly referred
to as hexadecimal. These functions are very similar to the both the Base64 and Base32 functions:

Section 58.4: Encoding and Decoding ASCII85Adobe created its own encoding called ASCII85 which is similar to Base85, but has its differences. This encoding is
used frequently in Adobe PDF files. These functions were released in Python version 3.4. Otherwise, the functions
base64.a85encode() and base64.a85encode() are similar to the previous:

Section 58.5: Encoding and Decoding Base85
Just like the Base64, Base32, and Base16 functions, the Base85 encoding and decoding functions are
base64.b85encode() and base64.b85decode():



"""
import dis
import base64

#Section 57.1: What is Python bytecode?
print("-------Section 57.1: What is Python bytecode?---------")
def hello():
    print("Hello, World")

dis.dis(hello)

#Section 57.2: Constants in the dis module
print("------Section 57.2: Constants in the dis module--------")

#Section 57.3: Disassembling modules
print("------Section 57.3: Disassembling modules-------")

#Section 58.1: Encoding and Decoding Base64
print("-=----------Section 58.1: Encoding and Decoding Base64----------")
s = "Hello World!"
b = s.encode("UTF-8")
#The output of the last line would be:
#b'Hello World!'
#The b prefix is used to denote the value is a bytes object.
e = base64.b64encode(b)
print(e)
s1 = e.decode("UTF-8")
print(s1)
# Base32 Encode the bytes
e = base64.b32encode(b)
#Decoding the Base32 bytes to string
s1 = e.decode("UTF-8")
# Printing Base32 encoded string
print("Base32 Encoded:", s1)
# Encoding the Base32 encoded string into bytes
b1 = s1.encode("UTF-8")
# Decoding the Base32 bytes
d = base64.b32decode(b1)
# Decoding the bytes to string
s2 = d.decode("UTF-8")
print(s2)

# Base16 Encode the bytes
e = base64.b16encode(b)
# Decoding the Base16 bytes to string
s1 = e.decode("UTF-8")

# ASCII85 Encode the bytes
e = base64.a85encode(b)
# Decoding the ASCII85 bytes to string
s1 = e.decode("UTF-8")
# Printing ASCII85 encoded string

# Base85 Encode the bytes
e = base64.b85encode(b)
# Decoding the Base85 bytes to string
s1 = e.decode("UTF-8")