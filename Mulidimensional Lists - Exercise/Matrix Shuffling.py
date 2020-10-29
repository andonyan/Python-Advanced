def generate_matrix(r, c):
    m = []
    for _ in range(r):
        m.append([0] * c)

    return m


def swap_matrix_element(m, first_row, first_column, second_row, second_column):

    if 0 <= (first_row and second_row) <= rows - 1 and 0 <= (first_column and second_column) <= columns - 1:
        temp = m[first_row][first_column]
        m[first_row][first_column] = m[second_row][second_column]
        m[second_row][second_column] = temp
        return m
    else:
        return None


def print_matrix(m):
    for i in range(len(m)):
        for k in range(len(m[i])):
            print(m[i][k], end=' ')
        print()


rows, columns = list(map(int, input().split()))
matrix = generate_matrix(rows, columns)

for i in range(rows):
    matrix[i] = input().split()

while True:
    swap_command = input().split()

    if swap_command[0] == 'END':
        break

    else:

        if swap_command[0] != 'swap' or len(swap_command) != 5:
            print('Invalid input!')
            continue

        else:

            row_one = int(swap_command[1])
            col_one = int(swap_command[2])
            row_two = int(swap_command[3])
            col_two = int(swap_command[4])

            if swap_matrix_element(matrix, row_one, col_one, row_two, col_two):
                print_matrix(matrix)
            else:
                print('Invalid input!')
