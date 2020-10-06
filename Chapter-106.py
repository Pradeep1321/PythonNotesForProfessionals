"""
Chapter 106: Dynamic code execution with `exec` and `eval`
Argument                    Details
expression              The expression code as a string, or a code object
object                  The statement code as a string, or a code object
globals                 The dictionary to use for global variables. If locals is not specified, this is also used for locals. If
                        omitted, the globals() of calling scope are used.
locals                  A mapping object that is used for local variables. If omitted, the one passed for globals is used
                        instead. If both are omitted, then the globals() and locals() of the calling scope are used for
                        globals and locals respectively.

Section 106.1: Executing code provided by untrusted user using exec, eval, or ast.literal_eval
It is not possible to use eval or exec to execute code from untrusted user securely. Even ast.literal_eval is
prone to crashes in the parser. It is sometimes possible to guard against malicious code execution, but it doesn't
exclude the possibility of outright crashes in the parser or the tokenizer.
To evaluate code by an untrusted user you need to turn to some third-party module, or perhaps write your own
parser and your own virtual machine in Python.

Section 106.2: Evaluating a string containing a Python literal with ast.literal_eval
If you have a string that contains Python literals, such as strings, floats etc, you can use ast.literal_eval to
evaluate its value instead of eval.

Section 106.3: Evaluating statements with exec


Section 106.4: Evaluating an expression with eval

expression = '5 + 3 * a'
 a = 5
 result = eval(expression)
  result  will be 20

Section 106.5: Precompiling an expression to evaluate it multiple times
compile built-in function can be used to precompile an expression to a code object; this code object can then be
passed to eval. This will speed up the repeated executions of the evaluated code. The 3rd parameter to compile
needs to be the string 'eval'.


Section 106.6: Evaluating an expression with eval using custom globals

variables = {'a': 6, 'b': 7}
>> eval('a * b', globals=variables)
42

As a plus, with this the code cannot accidentally refer to the names defined outside
>> eval('variables')
{'a': 6, 'b': 7}
>> eval('variables', globals=variables)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "<string>", line 1, in <module>
NameError: name 'variables' is not defined


Using defaultdict allows for example having undefined variables set to zero:
>> from collections import defaultdict
>> variables = defaultdict(int, {'a': 42})
>> eval('a * c', globals=variables) # note that 'c' is not explicitly defined
0

"""

import ast

code = """(1, 2, {'foo': 'bar'})"""
object = ast.literal_eval(code)
print(object)
print(type(object))

code = """for i in range(5):\n print('Hello world!')"""
exit(code)

print("----106.4---")
expression = '5 + 3 * a'
a = 5
result = eval(expression)
print(result)

print("----106.5---")
code = compile('a * b + c', '<string>', 'eval')
print(code)
a, b, c = 1, 2, 3
eval(code)
