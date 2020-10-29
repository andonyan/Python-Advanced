def generate_matrix(r, c):
    m = []
    coal_count = 0
    start_index = []
    end_index = []
    for i in range(r):
        row = input().split()
        for item in row:
            if item == 'c':
                coal_count += 1
            elif item == 's':
                start_index = [i, row.index(item)]
            elif item == 'e':
                end_index = [i, row.index(item)]

        m.append(row)

    return m, start_index, end_index, coal_count


def next_field_coordinates(miner, direction):
    current_row = miner[0]
    current_col = miner[1]
    if direction == 'left':

        if 0 <= current_col - 1:
            new_col = current_col - 1
            return [current_row, new_col]
        else:
            return False

    elif direction == 'right':

        if current_col + 1 <= n - 1:
            new_col = current_col + 1
            return [current_row, new_col]
        else:
            return False

    elif direction == 'up':

        if current_row - 1 >= 0:
            new_row = current_row - 1
            return [new_row, current_col]
        else:
            return False

    elif direction == 'down':

        if current_row + 1 <= n - 1:
            new_row = current_row + 1
            return [new_row, current_col]
        else:
            return False


coal_found = 0

n = int(input())

commands = input().split()

matrix, miner_coordinates, end, coal = generate_matrix(n, n)

for command in commands:

    result = next_field_coordinates(miner_coordinates, command)

    if result:

        miner_new_row, miner_new_col = result
        miner_coordinates = [miner_new_row, miner_new_col]
        if matrix[miner_new_row][miner_new_col] == 'c':

            coal_found += 1
            matrix[miner_new_row][miner_new_col] = '*'
            if coal_found == coal:

                print(f'You collected all coals! ({miner_new_row}, {miner_new_col})')
                break

        elif matrix[miner_new_row][miner_new_col] == 'e':

            print(f'Game over! ({miner_new_row}, {miner_new_col})')
            break

    else:

        continue

else:

    print(f'{coal - coal_found} coals left. ({miner_coordinates[0]}, {miner_coordinates[1]})')