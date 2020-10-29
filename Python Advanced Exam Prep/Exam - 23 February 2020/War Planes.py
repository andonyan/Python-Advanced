character_to_digit = {'x': 0, '.': 1, 'p': 2, 't': 3}
digit_to_character = {0: 'x', 1: '.', 2: 'p', 3: 't'}
plane_coordinates = []


def move_valid(coordinates_list, direction, steps):
    x = coordinates_list[1]
    y = coordinates_list[0]

    if direction == 'up':
        if y - steps >= 0 and (matrix[y - steps][x] == 1 or matrix[y - steps][x] == 2):
            return True
        else:
            return False

    elif direction == 'down':
        if y + steps < n and (matrix[y + steps][x] == 1 or matrix[y + steps][x] == 2):
            return True
        else:
            return False

    elif direction == 'left':
        if x - steps >= 0 and (matrix[y][x - steps] == 1 or matrix[y][x - steps] == 2):
            return True
        else:
            return False

    elif direction == 'right':
        if x + steps < n and (matrix[y][x + steps] == 1 or matrix[y][x + steps] == 2):
            return True
        else:
            return False


def target_valid(coordinates_list, direction, steps):
    x = coordinates_list[1]
    y = coordinates_list[0]

    if direction == 'up' and y - steps >= 0:
        return True
    elif direction == 'down' and y + steps < n:
        return True
    elif direction == 'left' and x - steps >= 0:
        return True
    elif direction == 'right' and x + steps < n:
        return True
    else:
        return False


def move_plane(coordinates_list, direction, steps):
    x = coordinates_list[1]
    y = coordinates_list[0]

    if direction == 'up':
        new_y = y - steps
        matrix[y][x] = 1
        matrix[new_y][x] = 2
        plane_coordinates[0] = new_y

    elif direction == 'down':
        new_y = y + steps
        matrix[y][x] = 1
        matrix[new_y][x] = 2
        plane_coordinates[0] = new_y

    elif direction == 'left':
        new_x = x - steps
        matrix[y][x] = 1
        matrix[y][new_x] = 2
        plane_coordinates[1] = new_x

    elif direction == 'right':
        new_x = x + steps
        matrix[y][x] = 1
        matrix[y][new_x] = 2
        plane_coordinates[1] = new_x


def shoot_target(coordinates_list, direction, steps):
    x = coordinates_list[1]
    y = coordinates_list[0]

    if direction == 'up':
        new_y = y - steps
        target_hit = False
        if matrix[new_y][x] == 3:
            target_hit = True
            matrix[new_y][x] = 0
        else:
            matrix[new_y][x] = 0

    elif direction == 'down':
        new_y = y + steps
        target_hit = False
        if matrix[new_y][x] == 3:
            target_hit = True
            matrix[new_y][x] = 0
        else:
            matrix[new_y][x] = 0

    elif direction == 'left':
        new_x = x - steps
        target_hit = False
        if matrix[y][new_x] == 3:
            target_hit = True
            matrix[y][new_x] = 0
        else:
            matrix[y][new_x] = 0

    elif direction == 'right':
        new_x = x + steps
        target_hit = False
        if matrix[y][new_x] == 3:
            target_hit = True
            matrix[y][new_x] = 0
        else:
            matrix[y][new_x] = 0

    return target_hit


def convert_symbols(symbol):
    if type(symbol) == str:
        return character_to_digit[symbol]
    else:
        return digit_to_character[symbol]


def generate_matrix(height, width):
    m = []
    targets = 0
    for i in range(height):
        row = input().split()
        for k in range(width):
            if row[k] == 'p':
                plane_coordinates.append(i)
                plane_coordinates.append(k)
            elif row[k] == 't':
                targets += 1
            row[k] = convert_symbols(row[k])
        m.append(row)

    return m, targets


def print_matrix(provided_matrix):

    for i in range(len(provided_matrix)):
        row_symbols = []
        for k in range(len(provided_matrix[i])):
            row_symbols.append(convert_symbols(provided_matrix[i][k]))
        print(' '.join(row_symbols))



n = int(input())
matrix, targets_count = generate_matrix(n, n)
initial_targets_count = targets_count
commands_count = int(input())

for _ in range(commands_count):
    command = input().split()
    action = command[0]
    selected_direction = command[1]
    steps_amount = int(command[2])

    if action == 'move' and move_valid(plane_coordinates, selected_direction, steps_amount):
        move_plane(plane_coordinates, selected_direction, steps_amount)
        continue

    elif action == 'shoot' and target_valid(plane_coordinates, selected_direction, steps_amount):
        if shoot_target(plane_coordinates, selected_direction, steps_amount):
            targets_count -= 1
            if targets_count == 0:
                print(f'Mission accomplished! All {initial_targets_count} targets destroyed.')
                print_matrix(matrix)
                break
else:
    print(f'Mission failed! {abs(targets_count)} targets left.')
    print_matrix(matrix)
