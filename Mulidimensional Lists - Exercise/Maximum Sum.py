import math


def generate_matrix(r, c):
    m = []
    for _ in range(r):
        m.append([0] * c)

    return m


rows, columns = list(map(int, input().split()))
matrix = generate_matrix(rows, columns)
matrix_highest_sum = generate_matrix(3, 3)
highest_sum = 0

for i in range(rows):
    matrix[i] = list(map(int, input().split()))

for i in range(rows - 2):
    for k in range(columns - 2):
        first_row_sum = sum(matrix[i][k: k + 3])
        second_row_sum = sum(matrix[i + 1][k: k + 3])
        third_row_sum = sum(matrix[i + 2][k: k + 3])

        if first_row_sum + second_row_sum + third_row_sum > highest_sum:
            matrix_highest_sum[0] = matrix[i][k: k + 3]
            matrix_highest_sum[1] = matrix[i + 1][k: k + 3]
            matrix_highest_sum[2] = matrix[i + 2][k: k + 3]
            highest_sum = first_row_sum + second_row_sum + third_row_sum

print(f'Sum = {highest_sum}')

for i in range(3):
    for number in matrix_highest_sum[i]:
        print(number, end=' ')
    print()
