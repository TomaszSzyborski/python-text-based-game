
align_spaces = 12
first = "first"
second= "second"
third = "third"
left = f"{first:<{align_spaces}}{second:<{align_spaces}}{third:<{align_spaces}}"
right = f"{first:>{align_spaces}}{second:>{align_spaces}}{third:>{align_spaces}}"
centered = f"{first:^{align_spaces}}{second:^{align_spaces}}{third:^{align_spaces}}"

for string in [left, right, centered]:
    print(string)
