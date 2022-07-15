# Adventure Game 

![Mock up of website on several differently sized devices](images/mockup.PNG)

Adventure Game is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

Users can try to beat the game using commands built into the game. If the player tries to perform
an action that the game doesn't have coded in then the game will ask the player what they were trying to do.
The program will then log this with the input, date, and time to a google sheet that the developer can review 
and potentially implement new features using player feedback.

The live link can be found here - https://adventuregamefeedback.herokuapp.com/

## How to play

The aim of the game is to escape the dungeon.

Currently the player can move through adjecent rooms in the dungeon by giving commands with the cardinal directions.

When the player encounters an enemy they can attack or flee to a random adjecent tile.

They are also able to find treasure and a different weapon in the dungeon if they explore.

If they find the cave exit they win, if they lose all their HP then they lose.

## Features

### Existing Features

- 

### Future Features

- Feedback implementation
    - The feedback inputted by player's is collected so that it can be used to either add keywords to commands so that
    there are multiple ways to call actions, or player's might be trying to try actions that dont exist but what they would 
    consider fun. The developer's can then choose to try and implement these ideas into the game, allowing the game to grow.

- Player classes and stats
    - In future versions of this game I would want to have the player choose a class at the beginning of the game which gave them certain stats and possibly
    unique actions. In terms of code I would just have these be subclasses of the player object.

- Damage rolls
    - Based off popular tabletop games such as Dungeons and Dragons I would want damage from weapons and enemies to be randomly generated from a range so
    that combat was less static. For player's weapons I would also the stats mentioned in the previous feature to add or subtract an amount of damage based
    on the type of item and the player's stat. 
## Data Model

The game is made up of several modules which contain model classes for the type of object they contain.
The Player module contains the player class which stores the player's inventory,gold value, hp, position in the game world, and whether they've
won the game or not. It also has methods to check if the player is still alive, as well as methods to help play the game such as changing it's x and y 
coordinates to call different rooms, as well as printing the player's inventory, and quitting the game.

The world module contains a method which parses a world text file to create 'rooms', assign them a class from the "rooms" module and assign them x and y values
to be called when the player's x and y values match. The layout is easily edited and planned by creating an excel sheet and putting the rooms into cells then 
copying over the text to the map.txt.

The rooms module contains a base class of room which has blank x y cordinates to be overwritten. as well as blank intro text and mody player methods. There are 
then two subclasses of room currently which are: Enemy Rooms, which runs functions from an enemy object contained in the enemies module, it also limits player's actions so they cant just leave; Loot rooms, which add an item to the player's inventory. 

The enemies module contains a base class for all enemies that contains hp values and blank damage values, it also contains a method to check if the enemy is still alive. There is currently only a giant spider enemy object that has been created with this base class.

The actions module contains an action base class which assigns names and keywords to the methods contained in the player class so that inputs from the plaer can call these actions. The action objects contained in this module are the same as the methods in the player modules.

The Items module contains a base class for all items which contains the values for the name of the item, the value of the item, and a description. There is currently only one sub-class for items which are weapons, and these include values for the damage the weapon does and a description of it's damage.

Finally the run.py module contains methods for editing the feedback spreadsheet when a player enters an incorrect action, as well as the play method which runs the game. This method loads in the world from the world module, creates the player, and then places the player within the world and runs through the room objects methods, checks to make sure the room didnt kill the player before displaying the actions, and then asks for input from the player. The player's input is then checked against available actions for that room
if it matches either the keyword or name of an action from the action module it will perform the matching method from the player module. If it does not match then it asks the player what they were trying to do and logs the input, intent, date, and time to an external spreadsheet that the developer can see. this process of input, performing action method, and performing room method loops until the player's victory value = true or the player's hp value =< 0.

```
def play():
    """
    Runs the game, loops until the game is lost, quit, or won
    """
    world.load_tiles()
    player = Player()
    # These lines load the starting room and display the text
    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            print("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            for action in available_actions:
                if action_input in action.hotkey:
                    player.do_action(action, **action.kwargs)
                    print("--------------------------------------------------")
                    break
                elif action_input.lower() == action.name.lower():
                    player.do_action(action, **action.kwargs)
                    print("--------------------------------------------------")
                    break
                elif action.hotkey == "q" and action_input != action.hotkey:
                    """
                    If the player inputs an invalid command then this code
                    will ask them what they were trying to and log it into
                    a spreadsheet that the developer can see. 
                    """
                    feedback(action_input)
                    # worksheet_to_update.append_row(data)
                    print("\n\t\t Thank you! Please try a different command!")
                
        elif not player.is_alive() and not player.victory:
            print("\n\t\tYOU HAVE DIED\n \n\t\t\t## GAME OVER ##\n")
```

## Testing

### Validator Testing

- Python
    - Only errors returned from PEP8onlne.com were "whitespace before "("" and I can't identify what whitespace it's referring to.

### Compatibility Testing

Site was tested across multiple virtual devices through chrome developor tools.

Site was tested to work on Google chrome, firefox, microsoft edge and internet explorer.

## Deployment

- The site was deployed using Code Institute's mock terminal for Heorku. The steps to deploy are as follows
    - Create a new Heroku App
    - Set the buildbacks to Python and NodeJS in that order
    - Link the heroku app to the repository
    - Click on Deploy

## Credits

- To complete this project I used Code Institute student template: [gitpod full template](https://github.com/Code-Institute-Org/python-essentials-template)

### Code

The basis of this game's code was adapted from this guide book: https://link.springer.com/book/10.1007/978-1-4842-3231-6

