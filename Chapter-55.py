"""
Chapter 55: Random module

Section 55.1: Creating a random user password

Note that other routines made immediately available by the random module — such as random.choice,
random.randint, etc. — are unsuitable for cryptographic purposes.

Python 3.x Version ≥ 3.6
Starting from Python 3.6, the secrets module is available, which exposes cryptographically safe functionality.


Section 55.2: Create cryptographically secure random numbers
In order to create a cryptographically secure pseudorandom number, one can use SystemRandom which, by using
os.urandom, is able to act as a Cryptographically secure pseudorandom number generator, CPRNG.

You can also use os.urandom directly to obtain cryptographically secure random bytes.

Section 55.3: Random and sequences: shuffle, choice and sample

You can use random.shuffle() to mix up/randomize the items in a mutable and indexable sequence. For example a list:

Choice() Takes a random element from an arbitrary sequence:

Sample(): Like choice it takes random elements from an arbitrary sequence but you can specify how many:


Section 55.4: Creating random integers and floats: randint, randrange, random, and uniform
randint()
Returns a random integer between x and y (inclusive):

randrange()
random.randrange has the same syntax as range and unlike random.randint, the last value is not inclusive:

random
Returns a random floating point number between 0 and 1:

uniform
Returns a random floating point number between x and y (inclusive):

Section 55.5: Reproducible random numbers: Seed and State
Setting a specific Seed will create a fixed random-number series:

one can also just use getstate and setstate to recover to a previous state

Section 55.6: Random Binary Decision

"""
import random
from random import SystemRandom
from random import randrange
from string import punctuation, ascii_letters, digits


#Section 55.1: Creating a random user password
print("------Section 55.1: Creating a random user password---------")

symbols = ascii_letters + digits + punctuation
secure_random = random.SystemRandom()
password = "".join(secure_random.choice(symbols) for i in range(10))
print(password)

#Section 55.2: Create cryptographically secure random numbers
print("-----------Section 55.2: Create cryptographically secure random numbers------")
secure_rand_gen = SystemRandom()
print([secure_rand_gen.randrange(10) for i in range(10)])
print(secure_rand_gen.randint(0, 20))

#Section 55.3: Random and sequences: shuffle, choice and sample

print("-------Section 55.3: Random and sequences: shuffle, choice and sample-----------")

#shuffle
laughs = ["Hi", "Ho", "He"]
random.shuffle(laughs) # Shuffles in-place! Don't do: laughs = random.shuffle(laughs)
print(laughs)

#choice()
print(random.choice(laughs))

#sample()
#                   |--sequence--|--number--|
print(random.sample( laughs , 1 )) # Take one element

#it will not take the same element twice:
print(random.sample(laughs, 3)) # Take 3 random element from the sequence.

#print(random.sample(laughs, 4)) # Take 4 random element from the 3-item sequence.
#ValueError: Sample larger than population

#Section 55.4: Creating random integers and floats: randint, randrange, random, and uniform
print("----------Section 55.4: Creating random integers and floats: randint, randrange, random, and uniform----------")

random.randint(1, 8)


print(random.randrange(100)) # Random integer between 0 and 99
print(random.randrange(20, 50)) # Random integer between 20 and 49
print(random.randrange(10, 20, 3)) # Random integer between 10 and 19 with step 3 (10, 13, 16 and 19)

print(random.random())

print(random.uniform(1, 8))

#Section 55.5: Reproducible random numbers: Seed and State
print("------Section 55.5: Reproducible random numbers: Seed and State---------")

print(random.seed(5))# Create a fixed state
print(random.randrange(0, 10)) # Get a random integer between 0 and 9

#Resetting the seed will create the same "random" sequence again:
random.seed(5) # Reset the random module to the same fixed state
print(random.randrange(0, 10))
print(random.randrange(0, 10))
#one can also just use getstate and setstate to recover to a previous state
save_state = random.getstate() # Get the current state
print(random.randrange(0, 10))
print(random.randrange(0, 10))

random.setstate(save_state) # Reset to saved state
print(random.randrange(0, 10))
print(random.randrange(0, 10))

#To pseudo-randomize the sequence again you seed with None
random.seed(None)

#Or call the seed method with no arguments
random.seed()

#Section 55.6: Random Binary Decision
print("----Section 55.6: Random Binary Decision--------")
probability = 0.3
if random.random() < probability:
    print("Decision with probability 0.3")
else:
    print("Decision with probability 0.7")
