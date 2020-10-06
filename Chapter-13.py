"""
Chapter 13: Variable Scope and Binding
Section 13.1: Nonlocal Variables
The nonlocal keyword adds a scope override to the inner scope.
Basically nonlocal will allow you to assign to variables in an outer scope, but not a global scope. So you can't use
nonlocal in our counter function because then it would try to assign to a global scope.

Section 13.2: Global Variables
1. if you've found global x, then x is a global variable
2. If you've found nonlocal x, then x belongs to an enclosing function, and is neither local nor global
3. If you've found x = 5 or for x in range(3) or some other binding, then x is a local variable
4. Otherwise x belongs to some enclosing scope (function scope, global scope, or builtins)

Section 13.3: Local Variables:
If a name is bound inside a function, it is by default accessible only within the function:

Section 13.4: The del command

del v
If v is a variable, the command del v removes the variable from its scope

Note that del is a binding occurrence, which means that unless explicitly stated otherwise (using nonlocal
or global), del v will make v local to the current scope. If you intend to delete v in an outer scope, use
nonlocal v or global v in the same scope of the del v statement.

del v.name
This command triggers a call to v.__delattr__(name).
The intention is to make the attribute name unavailable.

Section 13.5: Functions skip class scope when looking up names:
Classes have a local scope during definition, but functions inside the class do not use that scope when looking up
names. Because lambdas are functions, and comprehensions are implemented using function scope, this can lead
to some surprising behavior


Names in class scope are not accessible. Names are resolved in the innermost enclosing function scope.
If a class definition occurs in a chain of nested scopes, the resolution process skips class definitions.

Section 13.6: Local vs Global Scope
print(globals().keys()) # prints all variable names in global scope
print(locals().keys()) # prints all variable names in local scope
On the other hand, nonlocal (see Nonlocal Variables ), available in Python 3, takes a local variable from an
enclosing scope into the local scope of current function

Section 13.7: Binding Occurrence:
x = 5
x += 7
for x in iterable: pass
Each of the above statements is a binding occurrence - x become bound to the object denoted by 5. If this statement
appears inside a function, then x will be function-local by default. See the "Syntax" section for a list of binding
statements

"""
x = [0, 1, 2, 3, 4]
del x[1:3]
print(x) # out: [0, 3, 4]

a = 'global'
class Fred:
    a = 'class' # class scope
    b = (a for i in range(10)) # function scope
    c = [a for i in range(10)] # function scope
    d = a # class scope
    e = lambda: a # function scope
    f = lambda a=a: a # default argument uses class scope
    @staticmethod # or @classmethod, or regular instance method
    def g(): # function scope
        return a
print("============")
print(Fred.a) # class
print(next(Fred.b)) # global
print(Fred.c[0]) # class in Python 2, global in Python 3
print(Fred.d) # class
print(Fred.e()) # global
print(Fred.f()) # class
print(Fred.g()) # global

print("==============")
foo = 1
def func():
    #global foo
    foo = 2 # creates a new variable foo in local scope, global foo is not affected
    print(foo) # prints 2
    # global variable foo still exists, unchanged:
    print(globals()['foo']) # prints 1
    #print(locals()['foo']) # prints 2
print(foo)
func()
print(foo)
print("----")
foo = 1
def func():
    global foo
    foo = 2 # this modifies the global foo, rather than creating a local variable

func()
print("========")
def f1():
    def f2():
        foo = 2 # a new foo local in f2
        print(foo)
        def f3():
            nonlocal foo # foo from f2, which is the nearest enclosing scope
            print(foo) # 2
            foo = 20 # modifies foo from f2!
        f3()
        print(foo)
    f2()
f1()