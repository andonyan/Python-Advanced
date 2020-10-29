def generate_matrix(r, c):
    m = []
    for _ in range(r):
        m.append([0] * c)

    return m


rows, columns = list(map(int, input().split()))
matrix = generate_matrix(rows, columns)
perfect_matrix = 0

for i in range(rows):
    matrix[i] = input().split()

for i in range(rows - 1):
    for k in range(columns - 1):
        if matrix[i][k] == matrix[i + 1][k] and matrix[i][k] == matrix[i][k + 1] and matrix[i][k] == matrix[i + 1][k + 1]:
            perfect_matrix += 1

print(perfect_matrix)