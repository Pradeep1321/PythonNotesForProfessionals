"""
Chapter 91: urllib
Section 91.1: HTTP GET

Python 2.x Version ≤ 2.7
Python 2
import urllib
response = urllib.urlopen('http://stackoverflow.com/documentation/')

Using urllib.urlopen() will return a response object, which can be handled similar to a file.
print response.code
# Prints: 200

print response.read()
response.read() and response.readlines() can be used to read the actual html file returned from the request.
These methods operate similarly to file.read*

Python 3.x Version ≥ 3.0
Python 3
import urllib.request
print(urllib.request.urlopen("http://stackoverflow.com/documentation/"))
# Prints: <http.client.HTTPResponse at 0x7f37a97e3b00>
response = urllib.request.urlopen("http://stackoverflow.com/documentation/")
print(response.code)
# Prints: 200
print(response.read())
# Prints: b'<!DOCTYPE html>\r\n<html>\r\n<head>\r\n\r\n<title>Documentation - Stack Overflow</title>


Section 91.2: HTTP POST
To POST data pass the encoded query arguments as data to urlopen()
Python 2.x Version ≤ 2.7
Python 2
import urllib
query_parms = {'username':'stackoverflow', 'password':'me.me'}
encoded_parms = urllib.urlencode(query_parms)
response = urllib.urlopen("https://stackoverflow.com/users/login", encoded_parms)
response.code
# Output: 200
response.read()
# Output: '<!DOCTYPE html>\r\n<html>\r\n<head>\r\n\r\n<title>Log In - Stack Overflow'

Python 3.x Version ≥ 3.0
Python 3

import urllib
query_parms = {'username':'stackoverflow', 'password':'me.me'}
encoded_parms = urllib.parse.urlencode(query_parms).encode('utf-8')
response = urllib.request.urlopen("https://stackoverflow.com/users/login", encoded_parms)
response.code
# Output: 200
response.read()
# Output: b'<!DOCTYPE html>\r\n<html>....etc'


Section 91.3: Decode received bytes according to content type encoding
The received bytes have to be decoded with the correct character encoding to be interpreted as text:

Python 3.x Version ≥ 3.0
import urllib.request
response = urllib.request.urlopen("http://stackoverflow.com/")
data = response.read()

encoding = response.info().get_content_charset()
html = data.decode(encoding)

Python 2.x Version ≤ 2.7
import urllib2
response = urllib2.urlopen("http://stackoverflow.com/")
data = response.read()
encoding = response.info().getencoding()
html = data.decode(encoding)

Section 92.6: Simple web content download with urllib.request
The standard library module urllib.request can be used to download web content:
from urllib.request import urlopen
response = urlopen('http://stackoverflow.com/questions?sort=votes')
data = response.read()
# The received bytes should usually be decoded according the response's character set
encoding = response.info().get_content_charset()
html = data.decode(encoding)
A similar module is also available in Python 2.






"""