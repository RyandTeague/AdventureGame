import world
from player import Player
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('AdventureGame_feedback')


def play():
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
                    print("----------------------------------------------------------------------------")
                    break
                elif action_input.lower() == action.name.lower():
                    player.do_action(action, **action.kwargs)
                    print("----------------------------------------------------------------------------")
                    break
                elif action.hotkey == "q" and action_input != action.hotkey:
                    """
                    If the player inputs an invalid command then this code will ask them
                    what they were trying to and log it into a spreadsheet that the developer 
                    can see. 
                    """
                    data = [action_input]
                    intent = input("\n\t\tSomething went wrong, what were you trying to do?:\n")
                    data.append(intent)
                    the_date = datetime.now().date()
                    the_time = datetime.now().time()
                    data.append(the_date,the_time)
                    worksheet_to_update = SHEET.worksheet("feedback")
                    worksheet_to_update.append_row(data)
                    print("\n\t\t Thank you! Please try a different command!")
                
        elif not player.is_alive() and not player.victory:
            print("\n\t\tYOU HAVE DIED\n \n\t\t\t## GAME OVER ##\n")



if __name__ == "__main__":
    play()