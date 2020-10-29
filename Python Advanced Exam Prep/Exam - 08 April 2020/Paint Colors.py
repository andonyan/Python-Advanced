main_colors = ['red', 'yellow', 'blue']
secondary_colors = {'purple': ['blue', 'red'], 'orange': ['red', 'yellow'], 'green': ['yellow', 'blue']}

discovered_colors = []
kept_colors = []

provided_string = input().split()

while provided_string:

    first_substring = provided_string.pop(0)
    second_substring = provided_string.pop() if provided_string else ''

    if first_substring + second_substring in main_colors:
        discovered_colors.append(first_substring + second_substring)
        continue

    elif first_substring + second_substring in secondary_colors:
        discovered_colors.append(first_substring + second_substring)
        continue

    elif second_substring + first_substring in main_colors:
        discovered_colors.append(second_substring + first_substring)
        continue

    elif second_substring + first_substring in secondary_colors:
        discovered_colors.append(second_substring + first_substring)
        continue

    else:

        first = first_substring[:-1]
        second = second_substring[:-1]

        if first:

            provided_string.insert(len(provided_string) // 2, first)

        if second:
            provided_string.insert(len(provided_string) // 2, second)


secondary_colors_found = [color for color in discovered_colors if color in secondary_colors.keys()]

for color in secondary_colors_found:
    for required_color in secondary_colors[color]:
        if required_color not in discovered_colors:
            discovered_colors.remove(color)

print(discovered_colors)

