"""
Chapter 77: Context Managers (“with”Statement)

Section 77.1: Introduction to context managers and the with statement
A context manager is an object that is notified when a context (a block of code) starts and ends. You commonly use
one with the with statement. It takes care of the notifying.

For example, file objects are context managers. When a context ends, the file object is closed automatically.

with open(filename) as open_file:
    file_contents = open_file.read()

# the open_file object has automatically been closed.

Anything that ends execution of the block causes the context manager's exit method to be called. This includes
exceptions, and can be useful when an error causes you to prematurely exit from an open file or connection.
Exiting a script without properly closing files/connections is a bad idea, that may cause data loss or other problems.
By using a context manager you can ensure that precautions are always taken to prevent damage or loss in this
way. This feature was added in Python 2.5.

Section 77.2: Writing your own context manager
A context manager is any object that implements two magic methods __enter__() and __exit__() (although it can
implement other methods as well):

If the context exits with an exception, the information about that exception will be passed as a triple exc_type,
exc_value, traceback (these are the same variables as returned by the sys.exc_info() function). If the context
exits normally, all three of these arguments will be None.

Section 77.3: Writing your own contextmanager using generator syntax
It is also possible to write a context manager using generator syntax thanks to the contextlib.contextmanager
decorator:

Section 77.4: Multiple context managers
You can open several content managers at the same time:

with open(input_path) as input_file, open(output_path, 'w') as output_file:
    # do something with both files.
    # e.g. copy the contents of input_file into output_file
    for line in input_file:
        output_file.write(line + '\n')

Section 77.5: Assigning to a target
Many context managers return an object when entered. You can assign that object to a new name in the with
statement.

For example, using a database connection in a with statement could give you a cursor object:
with database_connection as cursor:
    cursor.execute(sql_query)

File objects return themselves, this makes it possible to both open the file object and use it as a context manager in
one expression:
with open(filename) as open_file:
    file_contents = open_file.read()


Section 77.6: Manage Resources
Using these magic methods (__enter__, __exit__) allows you to implement objects which can be used easily with
the with statement.


"""
import contextlib


#Section 77.1: Introduction to context managers and the with statement
print("-------Section 77.1: Introduction to context managers and the with statement---------")

#Section 77.2: Writing your own context manager
print("--------Section 77.2: Writing your own context manager------")

class AContextManager():
    def __enter__(self):
        print("Entered")
        # optionally return an object
        return "A-instance"
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exited" + (" (with an exception)" if exc_type else ""))
        # return True if you want to suppress the exception

#Section 77.3: Writing your own contextmanager using generator syntax
print("------Section 77.3: Writing your own contextmanager using generator syntax-------")
@contextlib.contextmanager
def context_manager(num):
    print('Enter')
    yield num + 1
    print('Exit')
with context_manager(2) as cm:
    # the following instructions are run when the 'yield' point of the context
    # manager is reached.
    # 'cm' will have the value that was yielded
    print('Right in the middle with cm = {}'.format(cm))

@contextlib.contextmanager
def error_handling_context_manager(num):
    print("Enter")
    try:
        yield num + 1
    except ZeroDivisionError:
        print("Caught error")
    finally:
        print("Cleaning up")
    print("Exit")

with error_handling_context_manager(-1) as cm:
    print("Dividing by cm = {}".format(cm))
    print(2 / cm)

#Section 77.4: Multiple context managers
print("-------Section 77.4: Multiple context managers-------")

#Section 77.5: Assigning to a target
print("-------Section 77.5: Assigning to a target------")

#Section 77.6: Manage Resources
print("------Section 77.6: Manage Resources------")
class File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file
    def __exit__(self, *args):
        self.open_file.close()

for _ in range(10000):
    with File('foo.txt', 'w') as f:
        f.write('foo')
