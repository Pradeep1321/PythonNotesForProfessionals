"""
Chapter 49: JSON Module
Section 49.1: Storing data in a file

Section 49.2: Retrieving data from a file

Section 49.3: Formatting JSON output

Section 49.4: `load` vs `loads`, `dump` vs `dumps`

The json module contains functions for both reading and writing to and from unicode strings, and reading and
writing to and from files. These are differentiated by a trailing s in the function name

As you can see the main difference is that when dumping json data you must pass the file handle to the function, as
opposed to capturing the return value. Also worth noting is that you must seek to the start of the file before reading
or writing, in order to avoid data corruption. When opening a file the cursor is placed at position 0,

Section 49.5: Calling `json.tool` from the command line to pretty-print JSON output

we can call the module directly from the command line (passing the filename as an argument) to pretty-print it:

$ python -m json.tool foo.json

The module will also take input from STDOUT, so (in Bash) we equally could do:
$ cat foo.json | python -m json.tool


Section 49.6: JSON encoding custom objects


Section 49.7: Creating JSON from Python dict

Section 49.8: Creating Python dict from JSON

"""
import json
from io import StringIO
from datetime import datetime

#Section 49.1: Storing data in a file
print("---------Section 49.1: Storing data in a file----------")

filename = r'C:\Data\Python\PythonNotesForProfessionals\testjason.txt'
d = {
    'foo': 'bar',
    'alice': 1,
    'wonderland': [1, 2, 3]
}

with open(filename, 'w') as f:
    json.dump(d, f)

#Section 49.2: Retrieving data from a file
print("-------Section 49.2: Retrieving data from a file------------")

with open(filename, 'r') as f:
    d = json.load(f)

#Section 49.3: Formatting JSON output
print("---------Section 49.3: Formatting JSON output---------")
data = {"cats": [{"name": "Tubbs", "color": "white"}, {"name": "Pepper", "color": "black"}]}
print(json.dumps(data))

#Setting indentation to get prettier output
print(json.dumps(data, indent=2))

#Sorting keys alphabetically to get consistent output
print(json.dumps(data, sort_keys=True))

#Getting rid of whitespace to get compact output
print(json.dumps(data, separators=(',', ':')))

#Section 49.4: `load` vs `loads`, `dump` vs `dumps`
print("----Section 49.4: `load` vs `loads`, `dump` vs `dumps`------")
data = {u"foo": u"bar", u"baz": []}
json_string = json.dumps(data)
json.loads(json_string)

json_file = StringIO()
data = {u"foo": u"bar", u"baz": []}
json.dump(data, json_file)
json_file.seek(0) # Seek back to the start of the file before reading
json_file_content = json_file.read()
json_file.seek(0) # Seek back to the start of the file before reading
json.load(json_file)

json_file_path = './data.json'
data = {u"foo": u"bar", u"baz": []}
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file)
with open(json_file_path) as json_file:
    json_file_content = json_file.read()
# u'{"foo": "bar", "baz": []}'
with open(json_file_path) as json_file:
    json.load(json_file)
# {u"foo": u"bar", u"baz": []}


#Having both ways of dealing with json data allows you to idiomatically and efficiently work with formats which build
#upon json, such as pyspark's json-per-line:
#loading from a file
#data = [json.loads(line) for line in open(filename).splitlines()]

#dumping to a file
#with open(filename, 'w') as json_file:
#    for item in data:
#        json.dump(item, json_file)
#        json_file.write('\n')

#Section 49.5: Calling `json.tool` from the command line to pretty-print JSON output
{"foo": {"bar": {"baz": 1}}}
#we can call the module directly from the command line (passing the filename as an argument) to pretty-print it:
# $ python -m json.tool foo.json

#Section 49.6: JSON encoding custom objects
print("-----Section 49.6: JSON encoding custom objects------")

data = {'datetime': datetime(2016, 9, 26, 4, 44, 0)}
#print(json.dumps(data))

#we get an error saying TypeError: datetime.datetime(2016, 9, 26, 4, 44) is not JSON serializable.


class DatetimeJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return obj.isoformat()
        except AttributeError:
            # obj has no isoformat method; let the builtin JSON encoder handle it
            return super(DatetimeJSONEncoder, self).default(obj)
encoder = DatetimeJSONEncoder()
print(encoder.encode(data))
# prints {"datetime": "2016-09-26T04:44:00"}

#Section 49.7: Creating JSON from Python dict
print("---Section 49.7: Creating JSON from Python dict--------")
print(json.dumps(d))

#Section 49.8: Creating Python dict from JSON
print("--------Section 49.8: Creating Python dict from JSON----------")
s = '{"wonderland": [1, 2, 3], "foo": "bar", "alice": 1}'
print(json.loads(s))
