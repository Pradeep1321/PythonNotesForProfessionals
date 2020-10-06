"""
Chapter 85: setup.py
Parameter               Usage
name                    Name of your distribution.
version                 Version string of your distribution.
packages                List of Python packages (that is, directories containing modules) to include. This can be specified
                        manually, but a call to setuptools.find_packages() is typically used instead.
py_modules              List of top-level Python modules (that is, single .py files) to include.

Section 85.1: Purpose of setup.py
The setup script is the center of all activity in building, distributing, and installing modules using the Distutils. Its
purpose is the correct installation of the software.

python setup.py sdist
sdist will create an archive file (e.g., tarball on Unix, ZIP file on Windows) containing your setup script setup.py, and
your module foo.py. The archive file will be named foo-1.0.tar.gz (or .zip), and will unpack into a directory foo-1.0

If an end-user wishes to install your foo module, all she has to do is download foo-1.0.tar.gz (or .zip), unpack it,
and—from the foo-1.0 directory—run
python setup.py install

Section 85.2: Using source control metadata in setup.py
setuptools_scm is an officially-blessed package that can use Git or Mercurial metadata to determine the version
number of your package, and find Python packages and package data to include in it.

from setuptools import setup, find_packages
setup(
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    packages=find_packages(),
    include_package_data=True,
)
This example uses both features; to only use SCM metadata for the version, replace the call to find_packages()
with your manual package list, or to only use the package finder, remove use_scm_version=True.

Section 85.3: Adding command line scripts to your python package
Command line scripts inside python packages are common. You can organise your package in such a way that
when a user installs the package, the script will be available on their path

However if you would like to run it like so:
hello_world.py
from setuptools import setup
setup(
    name='greetings',
    scripts=['hello_world.py']
)

When you install the greetings package now, hello_world.py will be added to your path.
Another possibility would be to add an entry point:
entry_points={'console_scripts': ['greetings=greetings.hello_world:main']}

This way you just have to run it like:
greetings

Section 85.4: Adding installation options
But there is even more options, like installing the package and have the possibility to change the code and test it
without having to re-install it. This is done using:

python setup.py develop



"""