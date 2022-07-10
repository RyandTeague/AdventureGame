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
