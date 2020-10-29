def generate_matrix(r, c):
    m = []
    for _ in range(r):
        m.append([0] * c)

    return m


def determine_neighbor_cells(m, bomb_row, bomb_col):
    neighbor_cells_coordinates = []

    if bomb_row == 0 and (bomb_col == 0 or bomb_col == n - 1):

        if bomb_col == 0:
            neighbor_cells_coordinates = [[bomb_row, bomb_col + 1], [bomb_row + 1, bomb_col],
                                          [bomb_row + 1, bomb_col + 1]]
            return neighbor_cells_coordinates

        elif bomb_col == n - 1:
            neighbor_cells_coordinates = [[bomb_row, bomb_col - 1], [bomb_row + 1, bomb_col - 1],
                                          [bomb_row + 1, bomb_col]]
            return neighbor_cells_coordinates

    elif bomb_row == n - 1 and (bomb_col == 0 or bomb_col == n - 1):

        if bomb_col == 0:
            neighbor_cells_coordinates = [[bomb_row - 1, bomb_col], [bomb_row - 1, bomb_col + 1],
                                          [bomb_row, bomb_col + 1]]
            return neighbor_cells_coordinates

        else:
            neighbor_cells_coordinates = [[bomb_row, bomb_col - 1], [bomb_row - 1, bomb_col - 1],
                                          [bomb_row - 1, bomb_col]]
            return neighbor_cells_coordinates

    elif 0 < bomb_row < n - 1 and (bomb_col == 0 or bomb_col == n - 1):

        if bomb_col == 0:
            neighbor_cells_coordinates = [[bomb_row - 1, bomb_col], [bomb_row - 1, bomb_col + 1],
                                          [bomb_row, bomb_col + 1], [bomb_row + 1, bomb_col + 1],
                                          [bomb_row + 1, bomb_col]]
            return neighbor_cells_coordinates
        else:
            neighbor_cells_coordinates = [[bomb_row - 1, bomb_col], [bomb_row - 1, bomb_col - 1],
                                          [bomb_row, bomb_col - 1], [bomb_row + 1, bomb_col - 1],
                                          [bomb_row + 1, bomb_col]]
            return neighbor_cells_coordinates
    elif 0 < bomb_col < n - 1 and (bomb_row == 0 or bomb_row == n - 1):

        if bomb_row == 0:
            neighbor_cells_coordinates = [[bomb_row, bomb_col - 1], [bomb_row + 1, bomb_col - 1],
                                          [bomb_row + 1, bomb_col], [bomb_row + 1, bomb_col + 1],
                                          [bomb_row, bomb_col + 1]]
            return neighbor_cells_coordinates
        else:
            neighbor_cells_coordinates = [[bomb_row, bomb_col + 1], [bomb_row - 1, bomb_col + 1],
                                          [bomb_row - 1, bomb_col], [bomb_row - 1, bomb_col - 1],
                                          [bomb_row, bomb_col - 1]]
            return neighbor_cells_coordinates

    else:

        neighbor_cells_coordinates = [[bomb_row - 1, bomb_col], [bomb_row - 1, bomb_col + 1], [bomb_row, bomb_col + 1],
                                      [bomb_row + 1, bomb_col + 1], [bomb_row + 1, bomb_col],
                                      [bomb_row + 1, bomb_col - 1], [bomb_row, bomb_col - 1],
                                      [bomb_row - 1, bomb_col - 1]]
        return neighbor_cells_coordinates


def inflict_damage(m, current_bomb_row, current_bomb_col):
    damage = m[current_bomb_row][current_bomb_col]

    coordinates = determine_neighbor_cells(m, current_bomb_row, current_bomb_col)
    for coordinate in coordinates:

        row, column = coordinate
        if m[row][column] <= 0:
            continue
        else:
            m[row][column] -= damage

    m[current_bomb_row][current_bomb_col] = 0


def determine_cells_alive_and_total_sum(m):
    cells = 0
    total = 0
    for j in range(len(m)):
        for z in range(len(m[j])):
            if m[j][z] > 0:
                cells += 1
                total += m[j][z]

    return cells, total


def print_matrix(m):
    for j in range(len(m)):
        for z in range(len(m[j])):
            print(m[j][z], end=' ')
        print()


n = int(input())
matrix = generate_matrix(n, n)
alive_cells = 0
total_sum = 0

for i in range(n):
    matrix[i] = list(map(int, input().split()))

bombs = input().split()

for bomb in bombs:
    bombs_row = int(bomb[0])
    bombs_col = int(bomb[2])
    if matrix[bombs_row][bombs_col] > 0:
        inflict_damage(matrix, bombs_row, bombs_col)
    else:
        continue

alive_cells, total_sum = determine_cells_alive_and_total_sum(matrix)
print(f'Alive cells: {alive_cells}')
print(f'Sum: {total_sum}')
print_matrix(matrix)
