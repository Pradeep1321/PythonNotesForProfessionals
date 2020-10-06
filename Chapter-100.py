"""
Chapter 100: Method Overriding
Section 100.1: Basic method overriding


"""
#Section 100.1: Basic method overriding
class Parent(object):
    def introduce(self):
        print("Hello!")
    def print_name(self):
        print("Parent")
class Child(Parent):
    def print_name(self):
        print("Child")
p = Parent()
c = Child()
p.introduce()
p.print_name()
c.introduce()
c.print_name()