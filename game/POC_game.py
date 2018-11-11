import cmd
import textwrap, sys, os, time, random
from functools import partial
import string

screen_width = 100


##### HELPERS #####
def slow_print(words):
    for char in words:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)

    sys.stdout.write("\n")
    sys.stdout.flush()

###### PLAYER #####
class Player:
    def __init__(self):
        self.name = ""
        self.profession = ""
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = "b2"
        self.game_over = False


myPlayer = Player()


def title_screen_selection():
    option = ""
    options = {
        "play": start_game,
        "help": help_menu,
        "exit": sys.exit
    }
    while option not in ["play",
                         "help",
                         "exit"]:
        option = input("Select option > ").lower()
        options.get(option,
                    partial(print, "Select valid option"))()


# title_screen_selection()

def title_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(80 * "#")
    print("#", "WELCOME TO RPG GAME".center(76), "#")
    print(80 * "#")
    print()
    for option in ["Play", "Help", "Exit"]:
        print(f"--- {option} ---".center(80))


def help_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(80 * "#")
    print("#", "WELCOME TO RPG GAME".center(76), "#")
    print(80 * "#")
    print()
    for option in ["Use up, down, right, left to move",
                   "Type commands to execute",
                   "Use look to inspect rooms"]:
        print(f"--- {option} ---".center(80))
    print("Choose wisely:")
    for option in ["Play", "Help", "Exit"]:
        print(f"--- {option} ---".center(80))

    title_screen_selection()


##### MAP #####
"""
4x4 grid
a1, a2... player startrs at b2
--------------------
|    |    |    |    |
---------------------
|    |    |    |    |
---------------------
|    |    |    |    |
---------------------
|    |    |    |    |
---------------------
"""

DESCRIPTION = "description"
EXAMINATION = "examine"
SOLVED = "solved"
UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"
ZONENAME = "zonename"

solved_places = {f"{letter}{number}": False
                 for letter in "abcd"
                 for number in range(1, 5)}

# pretty print for easy hardcoding values
import pprint
from string import ascii_lowercase


def _select_field_due_movement(letter, number, direction):
    letters = ascii_lowercase

    directions = {UP: (-1, 0),
                  DOWN: (1, 0),
                  LEFT: (0, -1),
                  RIGHT: (0, 1)}

    return f"{letters[letters.index(letter)+directions[direction][0]]}{number+directions[direction][1]}"


zonemap = {f"{letter}{number}": {ZONENAME: "",
                                 DESCRIPTION: "description",
                                 EXAMINATION: "examine",
                                 SOLVED: False,
                                 UP: _select_field_due_movement(letter, number, UP) if letter > "a" else "",
                                 DOWN: _select_field_due_movement(letter, number, DOWN) if letter < "d" else "",
                                 LEFT: _select_field_due_movement(letter, number, LEFT) if number > 1 else "",
                                 RIGHT: _select_field_due_movement(letter, number, RIGHT) if number < 4 else ""}
           for letter in "abcd" for number in range(1, 5)}

# pprint.pprint(zonemap)

zonemap["a1"][ZONENAME] = "Town Market"
zonemap["a2"][ZONENAME] = "Town Entrance"
zonemap["a3"][ZONENAME] = "Town Square"
zonemap["a4"][ZONENAME] = "Town Hall"
zonemap["b2"][ZONENAME] = "Home"
zonemap["b2"][EXAMINATION] = "Your home looks as usual - nothing has changed"
zonemap["b2"][DESCRIPTION] = "This is your home"


# pprint.pprint(zonemap)
# print(zonemap["b2"][DESCRIPTION])
# print((zonemap["b2"]))

##### GAME INTERACTIVITY #####
def print_location():
    # os.system('cls' if os.name == 'nt' else 'clear')
    here = myPlayer.location
    print("Your position is:")
    print("", "#" * 6)
    print("", "#", here.center(2), "#")
    print("", "#" * 6)
    print("The", DESCRIPTION, "is:", zonemap[here][DESCRIPTION])


# print_location()

def prompt():
    # os.system('cls' if os.name == 'nt' else 'clear')
    print("\n", "=" * 80)
    print("What would you like to do?")
    action = input("action > ").lower()

    moving_actions = ("move", "go", "travel", "walk")
    looking_actions = ("examine", "inspect", "interact", "look")
    exit_actions = ("exit", "quit")
    acceptable_actions = moving_actions + looking_actions + exit_actions

    while action not in acceptable_actions:
        print("Unknown action")
        print("Use one of following actions:")
        print(", ".join(acceptable_actions))
        action = input("action > ").lower()
    if action in exit_actions:
        sys.exit()
    elif action in moving_actions:
        player_move()
    elif action in looking_actions:
        player_examine()


def player_move():
    ask = "Where would you like to go?\n> "
    destination = ""
    while destination == "":
        answer = input(ask)
        if answer in ["up", "north"]:
            destination = zonemap[myPlayer.location][UP]
        elif answer in ["down", "south"]:
            destination = zonemap[myPlayer.location][DOWN]
        elif answer in ["right", "east"]:
            destination = zonemap[myPlayer.location][RIGHT]
        elif answer in ["left", "west"]:
            destination = zonemap[myPlayer.location][LEFT]

        if destination == "":
            print("Cannot go there.\nSelect other destination.")
        else:
            movement_handler(destination)


def movement_handler(destination):
    print(f"You have moved to {destination} .")
    myPlayer.location = destination
    print_location()


def player_examine():
    if zonemap[myPlayer.location][SOLVED]:
        print("All riddles are solved here")
    else:
        print("You can find and solve a puzzle here")

    print("As if you want to move, your surroundings are:")
    print("You are here:", myPlayer.location, zonemap[myPlayer.location][DESCRIPTION])
    temporary_location = myPlayer.location
    for direction in (UP, DOWN, LEFT, RIGHT):
        myPlayer.location = zonemap[myPlayer.location][direction]
        if myPlayer.location:
            print("When you go", direction, "you'll be in", myPlayer.location)
        else:
            print("You can't go", direction)
            print("There's a city wall there")
        myPlayer.location = temporary_location
    myPlayer.location = temporary_location


##### GAME FUNCIONALITY #####
def start_game():
    setup_game()
    main_game_loop()



def main_game_loop():
    # pprint.pprint(zonemap)
    while myPlayer.game_over is False:
        prompt()
        # handle events, if bosses are defeated, puzzles solved, explored areas etc. etc.


def setup_game():
    os.system('cls' if os.name == 'nt' else 'clear')

    ##### NAME HANDLING
    question1 = "Greetings stranger! What is your name?"
    slow_print(question1)
    while True:
        player_name = input("name > ").title()
        if player_name in string.whitespace:
            slow_print("Could you speak up a bit? I didn't hear that...")
        else:
            break

    myPlayer.name = player_name

    ##### PROFESSION HANDLING
    question2 = f"So {myPlayer.name}! What is your profession?"
    slow_print(question2)
    while True:
        q2_options = "(You can choose Warrior, Mage or Rogue)"
        slow_print(q2_options)
        player_profession = input("profession> ").title()
        valid_professions = ("Warrior", "Mage", "Rogue")
        if player_profession in valid_professions:
            myPlayer.profession = player_profession
            slow_print(f"Aaaahhh... so you're a {player_profession}")
            break
        else:
            print("Come again? I din't catch that...")

    ##### PLAYER STATS
    stats = {
        "Warrior": {"hp": 120,
                    "mp": 20},
        "Mage": {"hp": 40,
                 "mp": 120},
        "Rogue": {"hp": 80,
                  "mp": 80}
    }

    myPlayer.hp = stats[myPlayer.profession]["hp"]
    myPlayer.mp = stats[myPlayer.profession]["mp"]

    ##### INTRODUCTION
    slow_print(f"Nice to meet you {myPlayer.name} the {myPlayer.profession}")

    speech_1 = "Welcome to medieval city of Lublin, Poland"
    speech_2 = "I hope its citizens will greet you as warm as I do!"
    speech_3 = "But beware... Some say that something is lurking in the shadows..."
    for speech in [speech_1, speech_2, speech_3]:
        slow_print(speech)

    print("#" * 80)
    print("#", "Zacznijmy więc naszą przygodę".center(76), "#")
    print("#" * 80)


##### starting the game
title_screen()
title_screen_selection()
