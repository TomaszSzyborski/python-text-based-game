# import own packages
from main.user_actions.user_actions import act

while True:
    user_input = input("What do you want to do? (type 'help' for instructions):\n")
    act(user_input)

