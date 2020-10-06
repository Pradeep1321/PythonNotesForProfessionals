"""
Chapter 78: The __name__ special variable
The __name__ special variable is used to check whether a file has been imported as a module or not, and to identify
a function, class, module object by their __name__ attribute.

Section 78.1: __name__ == '__main__'
The special variable __name__ is not set by the user. It is mostly used to check whether or not the module is being
run by itself or run because an import was performed. To avoid your module to run certain parts of its code when it
gets imported, check if __name__ == '__main__'.

Section 78.2: Use in logging
When configuring the built-in logging functionality, a common pattern is to create a logger with the __name__ of the
current module:

logger = logging.getLogger(__name__)
This means that the fully-qualified name of the module will appear in the logs, making it easier to see where
messages have come from.

Section 78.3: function_class_or_module.__name__
The special attribute __name__ of a function, class or module is a string containing its name.

The __name__ attribute is not, however, the name of the variable which references the class, method or function,
rather it is the name given to it when defined.


"""