"""
Chapter 144: Attribute Access
>> book1.title
'P.G. Wodehouse'

Section 144.2: Setters, Getters & Properties
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        if not author:
            self.author = "Unknown"
        else:
           self.author = author


"""