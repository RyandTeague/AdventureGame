"""
contains the player class
"""
import items, world
import random
 
class Player():
    """
    Class representing the player character, contains all the information such as
    items and health. Also contains all the actions the player can take
    """
    def __init__(self):
        self.inventory = [items.Rock()]
        self.hp = 100
        self.location_x, self.location_y = world.starting_position
        self.victory = False
        self.gold = 15
 
    def is_alive(self):
        """
        Checks to see if the player has been killed
        """
        return self.hp > 0

    #Player actions
 
    def print_inventory(self):
        """
        Displays the player's inventory
        """
        print("Inventory:")
        for item in self.inventory:
            print(item, '\n')
        print("Gold: {}".format(self.gold))
        

    def move(self, dx, dy):
        """
        Changes the x y values of player and displays the intro text for that room
        """
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())
 
    def move_north(self):
        """
        moves the player one tile up the Y axis
        """
        self.move(dx=0, dy=-1)
 
    def move_south(self):
        """
        moves the player one tile down the Y axis
        """
        self.move(dx=0, dy=1)
 
    def move_east(self):
        """
        moves the player one tile up the x axis
        """
        self.move(dx=1, dy=0)
 
    def move_west(self):
        """
        moves the player one tile down the X axis
        """
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        """
        Checks the player's inventory for which weapon has the highest
        damage then subtracts it's value from the enemy's HP
        """
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i

        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def flee(self, tile):
        """
        Moves the player randomly to an adjacent tile
        """
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

    def quit(self):
        """
        Quits the game
        """
        print("\n\t\tYou have abandoned your journey!\n \n\t\t\t## GAME OVER ##\n")
        quit()

    # method to call player actions from commands

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)