"""
Chapter 79: Checking Path Existence and Permissions
Parameter           Details
os.F_OK         Value to pass as the mode parameter of access() to test the existence of path.
os.R_OK         Value to include in the mode parameter of access() to test the readability of path.
os.W_OK         Value to include in the mode parameter of access() to test the writability of path.
os.X_OK         Value to include in the mode parameter of access() to determine if path can be executed.

Section 79.1: Perform checks using os.access


"""
import os
path = "/home/myFiles/directory1"

#also it's possible to perform all checks together

os.access(path, os.F_OK & os.R_OK & os.W_OK & os.E_OK)