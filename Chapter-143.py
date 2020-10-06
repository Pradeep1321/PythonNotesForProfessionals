"""
Chapter 143: Mixins
Section 143.1: Mixin
A Mixin is a set of properties and methods that can be used in different classes, which don't come from a base
class.

class Foo(main_super, mixin): ...

The important thing with mixins is that they allow you to add functionality to much different objects, that don't
share a "main" subclass with this functionality but still share the code for it nonetheless. Without mixins, doing
something like the above example would be much harder, and/or might require some repetition.

Section 143.2: Overriding Methods in Mixins

Mixins are a sort of class that is used to "mix in" extra properties and methods into a class. This is usually fine
because many times the mixin classes don't override each other's, or the base class' methods. But if you do
override methods or properties in your mixins this can lead to unexpected results because in Python the class
hierarchy is defined right to left.



"""