"""
Chapter 50: Sqlite3 Module

Section 50.1: Sqlite3 - Not require separate server process

To use the module, you must first create a Connection object
that represents the database. Here the data will be stored in the example.db file:

You can also supply the special name :memory: to create a database in RAM. Once you have a Connection, you can
create a Cursor object and call its execute() method to perform SQL commands

Section 50.2: Getting the values from the database and Error handling


"""
import sqlite3


#Section 50.1: Sqlite3 - Not require separate server process
print("-----Section 50.1: Sqlite3 - Not require separate server process-------")

conn = sqlite3.connect('example.db')
c = conn.cursor()
# Create table
try:
    c.execute('CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)')
except sqlite3.Error as e:
    print("An error occurred:", e.args[0])

# Insert a row of data
try:
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
except sqlite3.Error as e:
    print("An error occurred:", e.args[0])
# Save (commit) the changes
try:
    conn.commit()
except sqlite3.Error as e:
    print("An error occurred:", e.args[0])

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
#onn.close()

#Section 50.2: Getting the values from the database and Error handling

c.execute('SELECT * from stocks')
for row in c:
    print(row) # will be a list
#To fetch single matching fetchone() method
print(c.fetchone())

#For multiple rows use fetchall() method
a=c.fetchall() #which is similar to list(cursor) method used previously
for row in a:
    print(row)

#Error handling can be done using sqlite3.Error built in function
#try:
#    #SQL Code
#except sqlite3.Error as e:
#    print("An error occurred:", e.args[0])