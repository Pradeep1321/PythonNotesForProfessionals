"""
Chapter 99: Polymorphism
Section 99.1:Duck Typing
Polymorphism without inheritance in the form of duck typing as available in Python due to its dynamic typing
system. This means that as long as the classes contain the same methods the Python interpreter does not
distinguish between them, as the only checking of the calls occurs at run-time.


Section 99.2: Basic Polymorphism

Polymorphism is the ability to perform an action on an object regardless of its type.
This is generally implemented
by creating a base class and having two or more subclasses that all implement methods with the same signature.
Any other function or method that manipulates these objects can call the same methods regardless of which type
of object it is operating on, without needing to do a type check first. In object-oriented terminology when class X
extend class Y , then Y is called super class or base class and X is called subclass or derived class.


"""

#Section 99.1:Duck Typing

class Duck:
    def quack(self):
        print("Quaaaaaack!")
    def feathers(self):
        print("The duck has white and gray feathers.")
class Person:
    def quack(self):
        print("The person imitates a duck.")
    def feathers(self):
        print("The person takes a feather from the ground and shows it.")
    def name(self):
        print("John Smith")
def in_the_forest(obj):
    obj.quack()
    obj.feathers()
donald = Duck()
john = Person()
in_the_forest(donald)
in_the_forest(john)

#Section 99.2: Basic Polymorphism

class Shape:
    """
    This is a parent class that is intended to be inherited by other classes
    """
    def calculate_area(self):
        """
        This method is intended to be overridden in subclasses.
        If a subclass doesn't implement it but it is called, NotImplemented will be raised.
        """
        #raise NotImplemented
        return None
class Square(Shape):
    """
    This is a subclass of the Shape class, and represents a square
    """
    side_length = 2 # in this example, the sides are 2 units long
    def calculate_area(self):
        """
        This method overrides Shape.calculate_area(). When an object of type
        Square has its calculate_area() method called, this is the method that
        will be called, rather than the parent class' version.
        It performs the calculation necessary for this shape, a square, and
        returns the result.
        """
        return self.side_length * 2
class Triangle(Shape):
    """
    This is also a subclass of the Shape class, and it represents a triangle
    """
    base_length = 4
    height = 3
    def calculate_area(self):
        """
        This method also overrides Shape.calculate_area() and performs the area
        calculation for a triangle, returning the result.
        """
        return 0.5 * self.base_length * self.height

def get_area(input_obj):
    """
    This function accepts an input object, and will call that object's
    calculate_area() method. Note that the object type is not specified. It
    could be a Square, Triangle, or Shape object.
    """
    print(input_obj.calculate_area())

# Create one object of each class
shape_obj = Shape()
square_obj = Square()
triangle_obj = Triangle()
# Now pass each object, one at a time, to the get_area() function and see the
# result.
get_area(shape_obj)
get_area(square_obj)
get_area(triangle_obj)