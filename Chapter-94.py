"""
Chapter 94: Manipulating XML
Section 94.1: Opening and reading using an ElementTree

Import the ElementTree object, open the relevant .xml file and get the root tag:

import xml.etree.ElementTree as ET

tree = ET.parse("yourXMLfile.xml")
root = tree.getroot()

#to search through tree

for child in root:
    print(child.tag, child.attrib)

or
print(root[0][1].text)

To search for specific tags by name, use the .find or .findall:
print(root.findall("myTag"))
print(root[0].find("myOtherTag"))

Section 94.2: Create and Build XML Documents

Element() function is used to create XML elements

p=ET.Element('parent')

SubElement() function used to create sub-elements to a give element

c = ET.SubElement(p, 'child1')

dump() function is used to dump xml elements

ET.dump(p)

If you want to save to a file create a xml tree with ElementTree() function and to save to a file use write() method
tree = ET.ElementTree(p)
tree.write("output.xml")

Comment() function is used to insert comments in xml file
comment = ET.Comment('user comment')
p.append(comment) #this comment will be appended to parent element

Section 94.3: Modifying an XML File
element.set('attribute_name', 'attribute_value') #set the attribute to xml element
element.text="string_text"

If you want to remove an element use Element.remove() method
root.remove(element)

ElementTree.write() method used to output xml object to xml files.
tree.write('output.xml')

Section 94.4: Searching the XML with XPath
Starting with version 2.7 ElementTree has a better support for XPath queries. XPath is a syntax to enable you to
navigate through an xml like SQL is used to search through a database. Both find and findall functions support
XPath.

tree = ET.parse('sample.xml')
tree.findall('Books/Book')

tree.find("Books/Book[Title='The Colour of Magic']")

tree.find("Books/Book[@id='5']")

Search for the last book:
tree.find("Books/Book[last()]")


tree.findall(".//Author")

Section 94.5: Opening and reading large XML files using iterparse (incremental parsing)

for event, elem in ET.iterparse("yourXMLfile.xml"):
... do something ...

Alternatively, we can only look for specific events, such as start/end tags or namespaces. If this option is omitted (as
above), only "end" events are returned:

events=("start", "end", "start-ns", "end-ns")
for event, elem in ET.iterparse("yourXMLfile.xml", events=events):
... do something ...


Ex:
for event, elem in ET.iterparse("yourXMLfile.xml", events=("start","end")):
    if elem.tag == "record_tag" and event == "end":
        print elem.text
        elem.clear()
    ... do something else ...



"""