"""
Chapter 65: Plotting with Matplotlib
Matplotlib (https://matplotlib.org/) is a library for 2D plotting based on NumPy

Section 65.1: Plots with Common X-axis but dierent Y-axis :

Using twinx()

we will plot a sine curve and a hyperbolic sine curve in the same plot with a common x-axis having
different y-axis. This is accomplished by the use of twinx() command.


"""
import numpy as np
import matplotlib.pyplot as plt

#Section 65.1: Plots with Common X-axis but dierent Y-axis :
print("-------Section 65.1: Plots with Common X-axis but different Y-axis :-----------")

x = np.linspace(0, 2.0*np.pi, 101)
y = np.sin(x)
z = np.sinh(x)
