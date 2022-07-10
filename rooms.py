import items, enemies

# Superclass for rooms of the game world, x and y coordinates are used to dictate the relative position of rooms
class Map_pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def intro_text(self):
    raise NotImplementedError()
 
    def modify_player(self, player):
    raise NotImplementedError()

# Subclasses creating individual rooms

class StartingRoom(MapTile):
    #starting room where player starts
    def intro_text(self):
        return """
        You find yourself if a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

class LootRoom(MapTile):
    # Room where player finds an item
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)
 
    def add_loot(self, player):
        player.inventory.append(self.item)
 
    def modify_player(self, player):
        self.add_loot(player)

class EnemyRoom(MapTile):
    # Room where player combats enemies
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
 
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp)