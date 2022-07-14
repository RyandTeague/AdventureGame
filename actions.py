"""
Contains the objects that call the different player actions and have methods
or keywords that the player can call in the game.py module
"""

from player import Player
 
class Action():
    """
    Creating the class to build orders that the player can give to the game
    """
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs
 
    def __str__(self):
        return "{}: {}".format(self.hotkey[0], self.name)

# Creating the specific orders for the player to control the game, including hotkeys
class MoveNorth(Action):
    """
    Makes the player take the move_north action, called when an input from game.py
    matches the name or hotkeys
    """
    def __init__(self):
        super().__init__(method=Player.move_north, name='Move north', hotkey='n')
 
class MoveSouth(Action):
    """
    calls the move_south player action
    """
    def __init__(self):
        super().__init__(method=Player.move_south, name='Move south', hotkey='s')
 
class MoveEast(Action):
    """
    calls the move_east player action
    """
    def __init__(self):
        super().__init__(method=Player.move_east, name='Move east', hotkey=['e', '1'])
 
class MoveWest(Action):
    """
    calls the move_west player action
    """
    def __init__(self):
        super().__init__(method=Player.move_west, name='Move west', hotkey='w')
 
class ViewInventory(Action):
    """
    Prints the player's inventory
    """
    def __init__(self):
        super().__init__(method=Player.print_inventory, name='View inventory', hotkey='i')

class QuitGame(Action):
    """
    Quits Game
    """
    def __init__(self):
        super().__init__(method=Player.quit, name='Quit Game', hotkey='q')

class Attack(Action):
    """
    Calls the attack player action
    """
    def __init__(self, enemy):
        super().__init__(method=Player.attack, name="Attack", hotkey='a', enemy=enemy)

class Flee(Action):
    """
    Calls the flee player actions
    """
    def __init__(self, tile):
        super().__init__(method=Player.flee, name="Flee", hotkey='f', tile=tile)
