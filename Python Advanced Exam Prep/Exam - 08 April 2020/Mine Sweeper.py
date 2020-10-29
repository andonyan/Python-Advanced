def generate_matrix(r, c):
    m = []
    for _ in range(r):
        m.append([0] * c)

    return m


def check_neighbor(coord1, coord2):
    neighbouring_bombs = 0
    # if bomb in first row
    if coord1 == 0:
        # if bomb in start of column
        if coord2 == 0:
            coords_to_check = [[coord1 + 1, coord2], [coord1 + 1, coord2 + 1], [coord1, coord2 + 1]]
            for coordinate in coords_to_check:
                y_coord = coordinate[0]
                x_coord = coordinate[1]
                if matrix[y_coord][x_coord] == '*':
                    neighbouring_bombs += 1

            return neighbouring_bombs

        # if bomb in end of column
        elif coord2 == matrix_size - 1:
            coords_to_check = [[coord1 + 1, coord2], [coord1 + 1, coord2 - 1], [coord1, coord2 - 1]]
            for coordinate in coords_to_check:
                y_coord = coordinate[0]
                x_coord = coordinate[1]
                if matrix[y_coord][x_coord] == '*':
                    neighbouring_bombs += 1

            return neighbouring_bombs
        # if bomb in the middle of column
        elif 0 < coord2 < matrix_size - 1:
            coords_to_check = [[coord1, coord2 - 1], [coord1, coord2 + 1], [coord1 + 1, coord2 - 1], [coord1 + 1, coord2], [coord1 + 1, coord2 + 1]]
            for coordinate in coords_to_check:
                y_coord = coordinate[0]
                x_coord = coordinate[1]
                if matrix[y_coord][x_coord] == '*':
                    neighbouring_bombs += 1

            return neighbouring_bombs

    # if bomb in last row
    elif coord1 == matrix_size - 1:
        # if bomb in start of column
        if coord2 == 0:
            coords_to_check = [[coord1 - 1, coord2], [coord1 - 1, coord2 + 1], [coord1, coord2 + 1]]
            for coordinate in coords_to_check:
                y_coord = coordinate[0]
                x_coord = coordinate[1]
                if matrix[y_coord][x_coord] == '*':
                    neighbouring_bombs += 1

            return neighbouring_bombs
        # if bomb in end of column
        elif coord2 == matrix_size - 1:
            coords_to_check = [[coord1 - 1, coord2], [coord1 - 1, coord2 - 1], [coord1, coord2 - 1]]
            for coordinate in coords_to_check:
                y_coord = coordinate[0]
                x_coord = coordinate[1]
                if matrix[y_coord][x_coord] == '*':
                    neighbouring_bombs += 1

            return neighbouring_bombs
        # if bomb in the middle of column
        elif 0 < coord2 < matrix_size - 1:
            coords_to_check = [[coord1, coord2 - 1], [coord1, coord2 + 1], [coord1 - 1, coord2 - 1],[coord1 - 1, coord2], [coord1 - 1, coord2 + 1]]
            for coordinate in coords_to_check:
                y_coord = coordinate[0]
                x_coord = coordinate[1]
                if matrix[y_coord][x_coord] == '*':
                    neighbouring_bombs += 1

            return neighbouring_bombs

    # if bomb in middle row
    elif 0 < coord1 < matrix_size - 1:
        # if bomb in start of column
        if coord2 == 0:
            coords_to_check = [[coord1 - 1, coord2], [coord1 - 1, coord2 + 1], [coord1, coord2 + 1],[coord1 + 1, coord2 + 1], [coord1 + 1, coord2]]
            for coordinate in coords_to_check:
                y_coord = coordinate[0]
                x_coord = coordinate[1]
                if matrix[y_coord][x_coord] == '*':
                    neighbouring_bombs += 1

            return neighbouring_bombs
        # if bomb in end of column
        elif coord2 == matrix_size - 1:
            coords_to_check = [[coord1 - 1, coord2], [coord1 - 1, coord2 - 1], [coord1, coord2 - 1],[coord1 + 1, coord2 - 1], [coord1 + 1, coord2]]
            for coordinate in coords_to_check:
                y_coord = coordinate[0]
                x_coord = coordinate[1]
                if matrix[y_coord][x_coord] == '*':
                    neighbouring_bombs += 1

            return neighbouring_bombs
        # if bomb in the middle of column
        elif 0 < coord2 < matrix_size - 1:
            coords_to_check = [[coord1 - 1, coord2 - 1], [coord1 - 1, coord2], [coord1 - 1, coord2 + 1],[coord1, coord2 + 1], [coord1 + 1, coord2 + 1], [coord1 + 1, coord2],[coord1 + 1, coord2 - 1], [coord1, coord2 -1]]
            for coordinate in coords_to_check:
                y_coord = coordinate[0]
                x_coord = coordinate[1]
                if matrix[y_coord][x_coord] == '*':
                    neighbouring_bombs += 1

            return neighbouring_bombs


matrix_size = int(input())
matrix = generate_matrix(matrix_size, matrix_size)

bombs_amount = int(input())
bombs_coordinates = []

for _ in range(bombs_amount):
    bomb_coordinates = input().split(', ')
    bomb_coordinates[0] = bomb_coordinates[0].replace('(', '')
    bomb_coordinates[1] = bomb_coordinates[1].replace(')', '')
    bomb_coordinates[0] = int(bomb_coordinates[0])
    bomb_coordinates[1] = int(bomb_coordinates[1])
    bombs_coordinates.append(bomb_coordinates)

#if bombs_coordinates:

for coordinates in bombs_coordinates:
    y = coordinates[0]
    x = coordinates[1]
    matrix[y][x] = '*'

for i in range(matrix_size):
    for k in range(matrix_size):
        if matrix[i][k] != '*':
            result = check_neighbor(i, k)
            matrix[i][k] = result

for i in range(matrix_size):
    for k in range(matrix_size):
        print(matrix[i][k], end=' ')

    print()



