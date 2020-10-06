""""
Chapter 129: tempfile NamedTemporaryFile
param                   description
mode                mode to open file, default=w+b
delete              To delete file on closure, default=True
suffix              filename suffix, default=''
prefix              filename prefix, default='tmp'
dir                 dirname to place tempfile, default=None
buffsize            default=-1, (operating system default used)


Section 129.1: Create (and write to a) known, persistent temporary file
You can create temporary files which has a visible name on the file system which can be accessed via the name
property. The file can, on unix systems, be configured to delete on closure (set by delete param, default is True) or
can be reopened later



"""

import tempfile
with tempfile.NamedTemporaryFile(delete=False) as t:
    t.write(b'Hello World!')
    path = t.name
    print(path)
with open(path) as t:
    print(t.read())