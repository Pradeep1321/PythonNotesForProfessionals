"""
Chapter 131: Unzipping Files
To extract or uncompress a tarball, ZIP, or gzip file, Python's tarfile, zipfile, and gzip modules are provided
respectively. Python's tarfile module provides the TarFile.extractall(path=".", members=None) function for
extracting from a tarball file. Python's zipfile module provides the ZipFile.extractall([path[, members[,
pwd]]]) function for extracting or unzipping ZIP compressed files. Finally, Python's gzip module provides the
GzipFile class for decompressing.

Section 131.1: Using Python ZipFile.extractall() to decompress a ZIP file
file_unzip = 'filename.zip'
unzip = zipfile.ZipFile(file_unzip, 'r')
unzip.extractall()
unzip.close()

Section 131.2: Using Python TarFile.extractall() to decompress a tarball
file_untar = 'filename.tar.gz'
untar = tarfile.TarFile(file_untar)
untar.extractall()
untar.close()

Chapter 132: Working with ZIP archives
Section 132.1: Examining Zipfile Contents

There are a few ways to inspect the contents of a zipfile. You can use the printdir to just get a variety of
information sent to stdout
with zipfile.ZipFile(filename) as zip:
    zip.printdir()

# Out:
# File Name Modified Size
# pyexpat.pyd 2016-06-25 22:13:34 157336


We can also get a list of filenames with the namelist method.
print(zip.namelist())
# Out: ['pyexpat.pyd', 'python.exe', 'python3.dll', 'python35.dll', ... etc. ...]

we can call the infolist method, which returns a list of ZipInfo objects
with zipfile.ZipFile(filename) as zip:
    info = zip.infolist()
    print(zip[0].filename)
    print(zip[0].date_time)
    print(info[0].file_size)
# Out: pyexpat.pyd
# Out: (2016, 6, 25, 22, 13, 34)
# Out: 157336

Section 132.2: Opening Zip Files
import the zipfile module, and set the filename

zip = zipfile.ZipFile(filename)
print(zip)
# <zipfile.ZipFile object at 0x0000000002E51A90>
zip.close()

or
with zipfile.ZipFile(filename, 'r') as z:
    print(zip)
# <zipfile.ZipFile object at 0x0000000002E51A90>


Section 132.3: Extracting zip file contents to a directory
with zipfile.ZipFile('zipfile.zip','r') as zfile:
    zfile.extractall('path')

If you want extract single files use extract method, it takes name list and path as input parameter
f=open('zipfile.zip','rb')
zfile=zipfile.ZipFile(f)
for cont in zfile.namelist():
    zfile.extract(cont,path)

Section 132.4: Creating new archives
To create new archive open zipfile with write mode

new_arch=zipfile.ZipFile("filename.zip",mode="w")

To add files to this archive use write() method.

new_arch.write('filename.txt','filename_in_archive.txt') #first parameter is filename and second
parameter is filename in archive by default filename will be taken if not provided
new_arch.close()

If you want to write string of bytes into the archive you can use writestr() method.
str_bytes="string buffer"
new_arch.writestr('filename_string_in_archive.txt',str_bytes)
new_arch.close()



Chapter 133: Getting start with GZip
The data compression is provided by the zlib module.

The gzip module provides the GzipFile class which is modeled after Python’s File Object. The GzipFile class reads
and writes gzip-format files, automatically compressing or decompressing the data so that it looks like an ordinary
file object.

Section 133.1: Read and write GNU zip files
import gzip
import os

outfilename = 'example.txt.gz'
output = gzip.open(outfilename, 'wb')
try:
    output.write('Contents of the example file go here.\n')
finally:
    output.close()
print(outfilename, 'contains', os.stat(outfilename).st_size, 'bytes of compressed data')
os.system('file -b --mime %s' % outfilename)


"""