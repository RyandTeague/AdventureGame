import items
import enemies
import actions
import world
from player import Player

# Variable for gold room
gold_looted = False

"""
Superclass for rooms of the game world, x and y coordinates
are used to dictate the relative position of rooms
"""


class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
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

        return moves

# Children of Map_pos creating types of rooms


class StartingRoom(Room):
    # starting room where player starts
    def intro_text(self):
        return """
        You find yourself if a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class LootRoom(Room):
    # Room where player finds an item
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(Room):
    # Room where player combats enemies
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print(f"Enemy does {self.enemy.damage} damage. You have {player.hp} HP remaining.")

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()

# Subclasses that are sepecific rooms


class EmptyCavePath(Room):
    def intro_text(self):
        return """
        Another unremarkable part of the cave. You must forge onwards.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class SnakePitRoom(Room):
    def intro_text(self):
        return """
        You enter the room when the ground gives way suddenly!

        You fall into a pit of snakes, you manage to climb out but not without sustaining injuries.
        """

    def modify_player(self, player):
        snake_damage = 2
        player.hp = player.hp - snake_damage
        print(f"You have taken {snake_damage} damage you have {player.hp} HP remaining...")


class GiantSpiderRoom(EnemyRoom):
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
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        return """
        Your notice something shiny in the corner.
        It's a dagger! You pick it up.
        """



class Find5GoldRoom(Room):
    def intro_text(self):
        if gold_looted = false:
            return """
            Your notice Shiny Coins scattered around on the Ground.

            You pick up 5 coins!
            """
        else:
            return """
            The Room is empty, you scan the ground for any signs
            of more gold but there is none.
            """

        def modify_player(self, player):
            player.inventory.items.Gold = player.inventory.items.Gold + 5

    

class LeaveCaveRoom(Room):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!

        Victory is yours!
        """

    def modify_player(self, player):
        player.victory = True