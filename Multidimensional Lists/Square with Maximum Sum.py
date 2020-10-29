def generate_matrix(r, c):
    m = []
    for _ in range(r):
        m.append([0] * c)

    return m


largest_sum = 0

rows, columns = list(map(int, input().split(', ')))
matrix = generate_matrix(rows, columns)
submatrix = generate_matrix(2, 2)

for i in range(rows):
    matrix[i] = list(map(int, input().split(', ')))

for i in range(rows - 1):
    for k in range(columns - 1):
        if matrix[i][k] + matrix[i][k + 1] + matrix[i + 1][k] + matrix[i + 1][k + 1] > largest_sum:
            largest_sum = matrix[i][k] + matrix[i][k + 1] + matrix[i + 1][k] + matrix[i + 1][k + 1]

            submatrix = [[matrix[i][k], matrix[i][k + 1]], [matrix[i + 1][k], matrix[i + 1][k + 1]]]

for i in range(2):
    print(f' '.join([str(x) for x in submatrix[i]]))

print(largest_sum)
