"""
Chapter 114: Idioms
Section 114.1: Dictionary key initializations
Prefer dict.get method if you are not sure if the key is present. It allows you to return a default value if key is not
found. The traditional method dict[key] would raise a KeyError exception.

Rather than doing
def add_student():
    try:
        students['count'] += 1
    except KeyError:
        students['count'] = 1

Do by using get

def add_student():
    students['count'] = students.get('count', 0) + 1

Section 114.2: Switching variables
To switch the value of two variables you can use tuple unpacking.
x = True
y = False
x, y = y, x

Section 114.3: Use truth value testing
Python will implicitly convert any object to a Boolean value for testing, so use it wherever possible

Section 114.4: Test for "__main__" to avoid unexpected code execution

It is good practice to test the calling program's __name__ variable before executing your code.
The benefit, however, comes if you decide to import your file in another program (for example if you are writing it
as part of a library). You can then import your file, and the __main__ trap will ensure that no code is executed
unexpectedly:

# A new program file
import my_program # main() is not run
# But you can run main() explicitly if you really want it to run:
my_program.main()



"""