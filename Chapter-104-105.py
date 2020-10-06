"""
Chapter 104: Reading and Writing CSV
Section 104.1: Using pandas
Write a CSV file from a dict or a DataFrame.

Section 104.2: Writing a TSV file

Chapter 105: Writing to CSV from String or List
Parameter                               Details
open ("/path/", "mode")             Specify the path to your CSV file
open (path, "mode")                 Specify mode to open file in (read, write, etc.)
csv.writer(file, delimiter)         Pass opened CSV file here
csv.writer(file, delimiter=' ')     Specify delimiter character or pattern

Writing to a .csv file is not unlike writing to a regular file in most regards, and is fairly straightforward.

Section 105.1: Basic Write Example

Section 105.2: Appending a String as a newline in a CSV file
def append_to_csv(input_string):
    with open("fileName.csv", "a") as csv_file:
        csv_file.write(input_row + "\n")

"""
import pandas as pd
d = {'a': (1, 101), 'b': (2, 202), 'c': (3, 303)}
df = pd.DataFrame.from_dict(d, orient="index")
df.to_csv("data.csv")
#Read a CSV file as a DataFrame and convert it to a dict:
df = pd.read_csv("data.csv")
d = df.to_dict()

#Section 104.2: Writing a TSV file
print("------Section 104.2: Writing a TSV file--------")

import csv
with open('output.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    tsv_writer.writerow(['name', 'field'])
    tsv_writer.writerow(['Dijkstra', 'Computer Science'])
    tsv_writer.writerow(['Shelah', 'Math'])
    tsv_writer.writerow(['Aumann', 'Economic Sciences'])


#Chapter 105: Writing to CSV from String or List