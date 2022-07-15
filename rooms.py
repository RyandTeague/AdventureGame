"""
Contains all the rooms or 'tiles' that the player can move to trigger
different events
"""

import items
import enemies
import actions
import world
from player import Player


class Room:
    """
    Superclass for rooms of the game world, x and y coordinates
    are used to dictate the relative position of rooms
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        """
        Throws up errors if a room object has been created 
        without intro text
        """
        raise NotImplementedError()

    def modify_player(self, player):
        """
        Throws up errors if a room object has been created 
        without something that changes the player in some 
        way
        """
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.QuitGame())

        return moves

# Children of Map_pos creating types of rooms


class StartingRoom(Room):
    """
    starting room where player starts
    """
    def intro_text(self):
        return """
        You find yourself if a cave with a flickering torch on the wall.
        You can make out a dimly lit and foreboding path ahead.
        """

    def modify_player(self, player):
        """
        Room has no action on player
        """
        pass


class LootRoom(Room):
    """
    Room where player finds an item
    """
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        if self.item not in player.inventory:
            self.add_loot(player)


class EnemyRoom(Room):
    """
    Room where player combats enemies
    """
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, player):
        """
        Reduces the player's hp
        """
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print(f"""Enemy does {self.enemy.damage} damage.
             You have {player.hp} HP remaining.""")

    def available_actions(self):
        """
        Checks if enemy is still alive and limits player's actions
        if they are.
        """
        if self.enemy.is_alive():
            moves = [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
            moves.append(actions.QuitGame())
            return moves
        else:
            moves = self.adjacent_moves()
            moves.append(actions.QuitGame())
            return moves

# Subclasses that are sepecific rooms


class EmptyCavePath(Room):
    def intro_text(self):
        return """
        Another unremarkable part of the cave. You must forge onwards.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class Find5GoldRoom(Room):
    """
    Room where player gains 5 gold
    """
    def __init__(self, x, y):
        self.gold = 5
        self.gold_looted = False
        super().__init__(x, y)

    def intro_text(self):
        if self.gold_looted:
            return """
            The Room is empty, you scan the ground for any signs
            of more gold but there is none.
            """
        else:
            return """
            Found Gold!
            """

    def modify_player(self, player):
        """
        Adds 5 to the gold value from the player object
        """
        if not self.gold_looted:
            self.gold_looted = True
            player.gold = player.gold + self.gold
            print("+{} gold added.".format(self.gold))


class SnakePitRoom(Room):
    """
    A room that damages the player but is not an enemy
    """
    def intro_text(self):
        return """
        You enter the room when the ground gives way suddenly!

        You fall into a pit of snakes, you manage to climb out 
        but not without sustaining injuries.
        """

    def modify_player(self, player):
        snake_damage = 2
        player.hp = player.hp - snake_damage
        print(f"""You have taken {snake_damage} damage
        you have {player.hp} HP remaining...""")


class GiantSpiderRoom(EnemyRoom):
    """ creates a room with a giant spider enemy """
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant spider jumps down from its web in front of you!
            """
        else:
            return """
            The corpse of a dead spider rots on the ground.
            """


class FindDaggerRoom(LootRoom):
    """
    creates a room where the player can pick up
    a dagger object and add it to their inventory
    """
    def __init__(self, x, y):
        self.dagger_looted = False
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        if not self.dagger_looted:
            self.dagger_looted = True
            return """
            You notice something shiny in the corner.
            It's a dagger! You pick it up.
            """
        else:
            return """ 
            This room is empty.
            You must keep moving!
            """


class LeaveCaveRoom(Room):
    """
    creates a room that changes the victory value to true,
    ending the game
    """
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!

        Victory is yours!
        """

    def modify_player(self, player):
        player.victory = True