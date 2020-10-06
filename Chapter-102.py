"""
Chapter 102: String representations of class instances: __str__ and __repr__ methods

Section 102.1: Motivation
class Card:
    def __init__(self, suit, pips):
        self.suit = suit
        self.pips = pips

But we can tell Python how we want instances of our custom classes to be converted to strings. And the way we do
this is with the __str__ "dunder" (for double-underscore) or "magic" method.

As was covered, the __str__ method was called when we passed our Card instance to print and the __repr__
method was called when we passed a list of our instances to print.

So instead, there is a mechanism in place to eliminate the need for that. One I snuck you past up to this point. It
turns out that if a class implements the __repr__ method but not the __str__ method, and you pass an instance of
that class to str() (whether implicitly or explicitly), Python will fallback on your __repr__ implementation and use
that.



"""
#Section 102.1: Motivation
class Card:
    def __init__(self, suit, pips):
        self.suit = suit
        self.pips = pips

ace_of_spades = Card('Spades', 1)
four_of_clubs = Card('Clubs', 4)
six_of_hearts = Card('Hearts', 6)

my_hand = [ace_of_spades, four_of_clubs, six_of_hearts]
print(my_hand)

#That output is comprised of two important bits: the type of the object and the object's id. The second part alone
#(the hexadecimal number) is enough to uniquely identify the object at the time of the print call.[1]
string_of_card = str(ace_of_spades)
print(string_of_card)

#But we can tell Python how we want instances of our custom classes to be converted to strings. And the way we do
#this is with the __str__ "dunder" (for double-underscore) or "magic" method.

class Card:
    special_names = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}
    def __init__(self, suit, pips):
        self.suit = suit
        self.pips = pips
    def __str__(self):
        card_name = Card.special_names.get(self.pips, str(self.pips))
        return "%s of %s (S)" % (card_name, self.suit)

    def __repr__(self):
        card_name = Card.special_names.get(self.pips, str(self.pips))
        return "%s of %s (R)" % (card_name, self.suit)


ace_of_spades = Card('Spades', 1)
print(ace_of_spades)


ace_of_spades = Card('Spades', 1)
four_of_clubs = Card('Clubs', 4)
six_of_hearts = Card('Hearts', 6)
my_hand = [ace_of_spades, four_of_clubs, six_of_hearts]

print(my_hand)

#As was covered, the __str__ method was called when we passed our Card instance to print and the __repr__
#method was called when we passed a list of our instances to print.