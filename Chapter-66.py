"""
Chapter 66: graph-tool
Section 66.1: PyDotPlus
PyDotPlus is an improved version of the old pydot project that provides a Python Interface to Graphviz’s Dot
language.


"""
import pydotplus


#Section 66.1: PyDotPlus
print("-----Section 66.1: PyDotPlus--------")

graph_a = pydotplus.graph_from_dot_file('demo.dot')
graph_a.write_svg('test.svg') # generate graph in svg.