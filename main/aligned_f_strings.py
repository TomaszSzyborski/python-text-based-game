
align_spaces = 12
first = "first"
second= "second"
third = "third"
left = f"{first:<{align_spaces}}{second:<{align_spaces}}{third:<{align_spaces}}"
right = f"{first:>{align_spaces}}{second:>{align_spaces}}{third:>{align_spaces}}"
centered = f"{first:^{align_spaces}}{second:^{align_spaces}}{third:^{align_spaces}}"

for string in [left, right, centered]:
    print(string)

filler = '*'
left = f"{first:{filler}<{align_spaces}}{second:{filler}<{align_spaces}}{third:{filler}<{align_spaces}}"
right = f"{first:{filler}>{align_spaces}}{second:{filler}>{align_spaces}}{third:{filler}>{align_spaces}}"
centered = f"{first:{filler}^{align_spaces}}{second:{filler}^{align_spaces}}{third:{filler}^{align_spaces}}"

for string in [left, right, centered]:
    print(string)

for align, text in zip('<^>', ['left', 'center', 'right']):
    # this is equal to:
    print('{0:{fill}{align}16}'.format(text, fill=align, align=align))
    # that:
    # text:fill alignment  number_of_chars
    # print(f"{text:{align}{align}{16}}")
    print(f"{text:{align}{align}{16}}")


width = 8
for num in range(5,12):
    for base in 'dXob':
       print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print()

