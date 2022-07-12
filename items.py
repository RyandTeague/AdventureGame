# import random

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


class Weapon(Item):
    def __init__(self, name, description, value, damage_desc, damage):
        self.damage_desc = damage_desc
        self.damage = damage
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage_desc)
 
# Subclasses of Weapon


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         damage_desc="1-2 + STR",
                         damage=2)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         value=2,
                         damage_desc="1-4 + DEX",
                         # damage= random.randint(1,4))  **I want weapons to have a damage range but for testing going to use a static number
                         damage=4)


print(Dagger().damage)