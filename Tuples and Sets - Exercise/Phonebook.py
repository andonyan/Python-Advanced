def has_numbers(string):
    return any(char.isdigit() for char in string)


phonebook = {}
should_continue = True

while should_continue:

    entry = input()
    if has_numbers(entry) and len(entry) > 1:
        name, phone = entry.split('-')
        phonebook[name] = phone

    elif has_numbers(entry) and len(entry) == 1:
        for _ in range(int(entry)):
            searched_name = input()
            if searched_name in phonebook:
                print(f'{searched_name} -> {phonebook[searched_name]}')
            else:
                print(f'Contact {searched_name} does not exist.')
        else:
            should_continue = False
