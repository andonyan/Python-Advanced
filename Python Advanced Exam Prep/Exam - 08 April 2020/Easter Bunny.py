cells_on_path = {'up': [], 'down': [], 'left': [], 'right': []}


def generate_matrix(height, width):
    m = []
    bunny_coordinates = []
    for i in range(height):
        row = input().split()
        for k in range(width):
            if row[k].isdigit():
                row[k] = int(row[k])
            elif row[k] == 'X':
                row[k] = -1
            else:
                bunny_coordinates.append(i)
                bunny_coordinates.append(k)
        m.append(row)

    return m, bunny_coordinates


def determine_possible_directions(field, bunny_location):
    y = bunny_location[0]
    x = bunny_location[1]
    matrix_size = len(field)
    possible_directions = []

    if 0 < x < matrix_size - 1:
        if field[y][x - 1] != -1:
            possible_directions.append('left')
        if field[y][x + 1] != -1:
            possible_directions.append('right')
    elif x == 0 and field[y][x + 1] != -1:
        possible_directions.append('right')
    elif x == matrix_size - 1 and field[y][matrix_size - 2] != -1:
        possible_directions.append('left')

    if 0 < y < matrix_size - 1:
        if field[y - 1][x] != -1:
            possible_directions.append('up')
        if field[y + 1][x] != -1:
            possible_directions.append('down')
    elif y == 0 and field[y + 1][x] != -1:
        possible_directions.append('down')
    elif y == matrix_size - 1 and field[matrix_size - 2][x] != -1:
        possible_directions.append('up')

    return possible_directions


def calculate_eggs_on_path(field, bunny_location, directions):
    y = bunny_location[0]
    x = bunny_location[1]
    matrix_size = len(field)
    eggs_per_path = []
    accumulated_eggs = 0

    initial_y = y
    initial_x = x

    for direction in directions:

        y = initial_y
        x = initial_x

        if direction == 'up':

            y -= 1

            while y >= 0:

                eggs_in_cell = field[y][x]

                if eggs_in_cell != -1:
                    accumulated_eggs += eggs_in_cell
                    cells_on_path[direction].append([y, x])
                    y -= 1
                    continue

                else:
                    eggs_per_path.append([direction, accumulated_eggs])
                    accumulated_eggs = 0
                    break
            else:

                eggs_per_path.append([direction, accumulated_eggs])
                accumulated_eggs = 0

        elif direction == 'down':

            y += 1

            while y <= matrix_size - 1:

                eggs_in_cell = field[y][x]

                if eggs_in_cell != -1:
                    accumulated_eggs += eggs_in_cell
                    cells_on_path[direction].append([y, x])
                    y += 1

                    continue

                else:
                    eggs_per_path.append([direction, accumulated_eggs])
                    accumulated_eggs = 0
                    break

            else:

                eggs_per_path.append([direction, accumulated_eggs])
                accumulated_eggs = 0

        elif direction == 'left':

            x -= 1

            while x >= 0:
                eggs_in_cell = field[y][x]

                if eggs_in_cell != -1:
                    accumulated_eggs += eggs_in_cell
                    cells_on_path[direction].append([y, x])
                    x -= 1

                    continue

                else:
                    eggs_per_path.append([direction, accumulated_eggs])
                    accumulated_eggs = 0
                    break
            else:

                eggs_per_path.append([direction, accumulated_eggs])
                accumulated_eggs = 0

        elif direction == 'right':

            x += 1

            while x <= matrix_size - 1:

                eggs_in_cell = field[y][x]

                if eggs_in_cell != -1:
                    accumulated_eggs += eggs_in_cell
                    cells_on_path[direction].append([y, x])
                    x += 1

                    continue

                else:
                    eggs_per_path.append([direction, accumulated_eggs])
                    accumulated_eggs = 0
                    break

            else:

                eggs_per_path.append([direction, accumulated_eggs])
                accumulated_eggs = 0

    return eggs_per_path


field_size = int(input())
matrix, bunny = generate_matrix(field_size, field_size)

available_directions = determine_possible_directions(matrix, bunny)
eggs_on_paths = calculate_eggs_on_path(matrix, bunny, available_directions)

best_path = max(eggs_on_paths, key=lambda x: x[1])

print(best_path[0])
for cell in cells_on_path[best_path[0]]:
    print(cell)
print(best_path[1])
