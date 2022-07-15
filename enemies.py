"""
Contains all the enemy objects that the player
can lose hp to
"""

# Superclass


class Enemy:
    """
    Base class that is used to create all other enemies
    """
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
 
    def is_alive(self):
        return self.hp > 0

# Subclasses


class GiantSpider(Enemy):
    """
    creates a spider enemy 
    """
    def __init__(self):
        super().__init__(name="Giant Spider", hp=10, damage=2)

