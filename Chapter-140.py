"""
Chapter 140: Alternatives to switch statement from other languages

Section 140.1: Use what the language oers: the if/else construct

def switch(value):
    if value == 1:
        return "one"
    if value == 2:
        return "two"
    if value == 42:
        return "the answer to the question about life, the universe and everything"
    raise Exception("No case found!")

Section 140.2: Use a dict of functions
switch = {
    1: lambda: 'one',
    2: lambda: 'two',
    42: lambda: 'the answer of life the universe and everything',
    }

Section 140.3: Use class introspection
You can use a class to mimic the switch/case structure. The following is using introspection of a class (using the
getattr() function that resolves a string into a bound method on an instance) to resolve the "case" part.
Then that introspecting method is aliased to the __call__ method to overload the () operator.

class SwitchBase:
    def switch(self, case):
        m = getattr(self, 'case_{}'.format(case), None)
        if not m:
            return self.default
        return m
    __call__ = switch

Section 140.4: Using a context manager
class Switch:
    def __init__(self, value):
        self._val = value
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        return False # Allows traceback to occur
    def __call__(self, cond, *mconds):
        return self._val in (cond,)+mconds
def run_switch(value):
    with Switch(value) as case:
        if case(1):
            return 'one'
        if case(2):
            return 'two'
        if case(3):
            return 'the answer to the question about life, the universe and everything'
        # default
        raise Exception('Not a case!')

"""