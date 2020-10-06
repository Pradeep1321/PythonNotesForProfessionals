"""
Chapter 115: Data Serialization
Parameter                   Details
protocol                Using pickle or cPickle, it is the method that objects are being Serialized/Unserialized. You probably
                        want to use pickle.HIGHEST_PROTOCOL here, which means the newest method.

Section 115.1: Serialization using JSON
JSON is a cross language, widely used method to serialize data


"""

import json

families = (['John'], ['Mark', 'David', {'name': 'Avraham'}])
# Dumping it into string
json_families = json.dumps(families)
# [["John"], ["Mark", "David", {"name": "Avraham"}]]
# Dumping it to file
with open('families.json', 'w') as json_file:
    json.dump(families, json_file)

# Loading it from string
json_families = json.loads(json_families)
# Loading it from file
with open('families.json', 'r') as json_file:
    json_families = json.load(json_file)

#Section 115.2: Serialization using Pickle
# Importing pickle
try:
    import cPickle as pickle # Python 2
except ImportError:
    import pickle # Python 3



# Creating Pythonic object:
class Family(object):
    def __init__(self, names):
        self.sons = names
    def __str__(self):
        return ' '.join(self.sons)
my_family = Family(['John', 'David'])
# Dumping to string
pickle_data = pickle.dumps(my_family, pickle.HIGHEST_PROTOCOL)

# Dumping to file
with open('family.p', 'w') as pickle_file:
    pickle.dump(families, pickle_file, pickle.HIGHEST_PROTOCOL)

# Loading from string
my_family = pickle.loads(pickle_data)

# Loading from file
with open('family.p', 'r') as pickle_file:
    my_family = pickle.load(pickle_file)


