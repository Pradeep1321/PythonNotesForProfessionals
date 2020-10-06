"""
Chapter 51: The os Module
Parameter                   Details
Path                A path to a file. The path separator may be determined by os.path.sep.
Mode                The desired permission, in octal (e.g. 0700)
This module provides a portable way of using operating system dependent functionality

Section 51.1: makedirs - recursive directory creation
If we use os.mkdir , we would have an exception because dir2 would not have existed yet. so we have to use os.makedirs.
os.makedirs won't like it if the target directory exists already. If we re-run it again:

Section 51.2: Create a directory
os.mkdir('newdir1', mode=0o700)

Section 51.3: Get current directory
Use the os.getcwd() function

Section 51.4: Determine the name of the operating system
os.name

Section 51.5: Remove a directory

Remove the directory at path:
os.rmdir(path)

You should not use os.remove() to remove a directory. That function is for files and using it on directories will
result in an OSError

Section 51.6: Follow a symlink (POSIX)
Sometimes you need to determine the target of a symlink. os.readlink will do this:

print(os.readlink(path_to_symlink))

Section 51.7: Change permissions on a file
os.chmod(path, mode)
where mode is the desired permission, in octal



"""

#Section 51.1: makedirs - recursive directory creation
print("-----Section 51.1: makedirs - recursive directory creation----------")
import os

# the below give error as dir1 doesnt exists
#os.mkdir("./dir1/subdir1")

try:
    os.makedirs("./dir2/subdir1")
except OSError:
    if not os.path.isdir("./dir2/subdir1"):
        raise
try:
    os.makedirs("./dir2/subdir2")
except OSError:
    if not os.path.isdir("./dir2/subdir2"):
        raise

#Section 51.2: Create a directory
print("------Section 51.2: Create a directory-------")

# the below give error if newdir already exists
try:
    os.mkdir('newdir')
except OSError:
    print("directory already exists")

#If you need to specify permissions, you can use the optional mode argument:
try:
    os.mkdir('newdir1', mode=0o700)
except OSError:
    print("directory already exists")

#Section 51.3: Get current directory
print("------Section 51.3: Get current directory---------")
print(os.getcwd())

#Section 51.4: Determine the name of the operating system
print("----Section 51.4: Determine the name of the operating system-------")
print(os.name)

