import random
import string


def draw_table(width: int = 80, height: int = 40,
               top_left_corner: str = "", top_right_corner: str = "",
               bottom_left_corner: str = "", bottom_right_corner: str = "",
               top_bottom_sides: str = "", left_right_sides: str = ""):
    for i in range(height):
        random_range = random.randint(2, 10)
        data = ''.join(random.choice(string.ascii_letters) for _ in range(random_range))
        if i == 0:
            print(f"{top_left_corner}{top_bottom_sides*(width-2)}{top_right_corner}")
        elif i == height - 1:
            print(f"{bottom_left_corner}{top_bottom_sides*(width-2)}{bottom_right_corner}")
        else:
            to_print = data.center(width, ' ')
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

print("Thick table")
draw_table(**thick)

print("Basic table")
draw_table(**basic)

print("Rounded table")
draw_table(**rounded)

print("Default table")
draw_table()

other = {k: '*' for k, v in thick.items() if k not in ("width", "height")}
print("Other table")
draw_table(**other)
