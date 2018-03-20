from functools import partial

from terminal_actions.printing import print_actions

actions = {
    "help": partial(print_actions),
    "look around": partial(print, "get_room_content"),
    "exit": partial(exit, 0)
}
