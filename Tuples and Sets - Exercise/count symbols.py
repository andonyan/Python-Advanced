characters = {}

for char in input():
    if char in characters:
        characters[char] += 1
    else:
        characters[char] = 1

for char, count in sorted(characters.items()):
    print(f'{char}: {count} time/s')
