"""
Contains all the object classes
"""


class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format\
            (self.name, self.description, self.value)

# Subclasses of Item


class Weapon(Item):
    """
    An Item object that can do damage
    """
    def __init__(self, name, description, value, damage_desc, damage):
        self.damage_desc = damage_desc
        self.damage = damage
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format\
            (self.name, self.description, self.value, self.damage_desc)
 
# Subclasses of Weapon


class Rock(Weapon):
    """
    The starting weapon that does the least damage but the
    player can't attack an enemy without a weapon
    """
    def __init__(self):
        super().__init__(name="Rock",
                         description="""A fist-sized rock,
                          suitable for bludgeoning.""",
                         value=0,
                         damage_desc="2",
                         damage=2)


class Dagger(Weapon):
    """
    An item to be found that allows the player to do more damage to enemies
    """
    def __init__(self):
        super().__init__(name="Dagger",
                         description="""A small dagger with some rust.
                          Somewhat more dangerous than a rock.""",
                         value=2,
                         damage_desc="4",
                         damage=4)