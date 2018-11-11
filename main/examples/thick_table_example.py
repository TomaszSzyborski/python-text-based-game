import random
import string


def draw_table(width: int = 80, height: int = 40,
               top_left_corner: str = "", top_right_corner: str = "",
               bottom_left_corner: str = "", bottom_right_corner: str = "",
               top_bottom_sides: str = "", left_right_sides: str = "",
               data: list = None):
    """

    @param width: int - number of characters - represents column table + 2 as border
    @param height: int - number of charactes - represents rows in table + 2 as border
    @param top_left_corner: str - single character representing top left corner the table
    @param top_right_corner: str - single character representing top right corner the table
    @param bottom_left_corner: str - single character representing bottom left corner the table
    @param bottom_right_corner: str - single character representing bottom right corner the table
    @param top_bottom_sides: str - single character representing top and bottom sides of the table
    @param left_right_sides: str - single character representing left and right sides of the table
    @param data: list of strings to be written in table
    @return: None
    """
    for i in range(height):
        if i == 0:
            print(f"{top_left_corner}{top_bottom_sides*(width-2)}{top_right_corner}")
        elif i == height - 1:
            print(f"{bottom_left_corner}{top_bottom_sides*(width-2)}{bottom_right_corner}")
        else:
            to_print = data[i-1].center(width, ' ')
            print(f"{left_right_sides}{to_print[1:-1]}{left_right_sides}")


thick = {
    "width": 80,
    "height": 40,
    "top_left_corner": "╔",
    "top_right_corner": "╗",
    "bottom_left_corner": "╚",
    "bottom_right_corner": "╝",
    "top_bottom_sides": "═",
    "left_right_sides": "║"
}

basic = {
    "width": 80,
    "height": 40,
    "top_left_corner": "+",
    "top_right_corner": "+",
    "bottom_left_corner": "+",
    "bottom_right_corner": "+",
    "top_bottom_sides": "-",
    "left_right_sides": "|"
}

rounded = {
    "width": 80,
    "height": 40,
    "top_left_corner": "/",
    "top_right_corner": "\\",
    "bottom_left_corner": "\\",
    "bottom_right_corner": "/",
    "top_bottom_sides": "-",
    "left_right_sides": "|"
}


data = [''.join(random.choice(string.ascii_letters) for _ in range(random.randint(2, 10))) for i in range(80)]

print("Thick table")
draw_table(**thick, data=data)

print("Basic table")
draw_table(**basic, data=data)

print("Rounded table")
draw_table(**rounded, data=data)

print("Default table")
draw_table(data=data)

other = {k: '*' for k, v in thick.items() if k not in ("width", "height")}
print("Other table")
draw_table(**other, data=data)
