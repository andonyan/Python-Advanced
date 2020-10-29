bomb_effects = [int(x) for x in input().split(', ')]
bomb_casings = [int(x) for x in input().split(', ')]
bombs_created = {'Cherry Bombs': 0, 'Datura Bombs': 0, 'Smoke Decoy Bombs': 0}
bomb_effects.reverse()

while len(bomb_effects) > 0 and len(bomb_casings) > 0:




    if bomb_effects[-1] + bomb_casings[-1] == 40:
        bomb_effects.pop()
        bomb_casings.pop()
        bombs_created['Datura Bombs'] += 1

    elif bomb_effects[-1] + bomb_casings[-1] == 60:
        bomb_effects.pop()
        bomb_casings.pop()
        bombs_created['Cherry Bombs'] += 1

    elif bomb_effects[-1] + bomb_casings[-1] == 120:
        bomb_effects.pop()
        bomb_casings.pop()
        bombs_created['Smoke Decoy Bombs'] += 1

    else:
        bomb_casings[-1] -= 5
        if bomb_casings[-1] < 0:
            bomb_casings.pop()



    if all(x >= 3 for x in list(bombs_created.values())):
        print('Bene! You have successfully filled the bomb pouch!')
        if len(bomb_effects) > 0:
            print(f'Bomb Effects: {", ".join(map(str, reversed(bomb_effects)))}')
        else:
            print('Bomb Effects: empty')

        if len(bomb_casings) > 0:
            print(f'Bomb Casings: {", ".join(map(str, bomb_casings))}')
        else:
            print('Bomb Casings: empty')

        for key, value in sorted(bombs_created.items(), key=lambda item: item[0]):
            print(f'{key}: {value}')

        break


else:

    print('You don\'t have enough materials to fill the bomb pouch.')
    if len(bomb_effects) > 0:
        print(f'Bomb Effects: {", ".join(map(str, reversed(bomb_effects)))}')
    else:
        print('Bomb Effects: empty')

    if len(bomb_casings) > 0:
        print(f'Bomb Casings: {", ".join(map(str, bomb_casings))}')
    else:
        print('Bomb Casings: empty')

    for key, value in sorted(bombs_created.items(), key=lambda item: item[0]):
        print(f'{key}: {value}')
