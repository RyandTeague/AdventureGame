import world
from player import Player
 
def play():
    world.load_tiles() player = Player()
    while player.is_alive() and not player.victory:
        #Loop begins here