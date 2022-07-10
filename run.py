from adventurelib import *
import random

# Creating object classes

class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

# Subclasses of Item

class Gold(Item):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(name="Gold",
                         description="A bag of round coins, a quick count shows that you have {} coins".format(str(self.amount)),
                         value=self.amount)

print(Gold(100))