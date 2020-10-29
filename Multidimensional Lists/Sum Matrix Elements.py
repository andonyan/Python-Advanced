def generate_matrix(r, c):
    m = []
    for _ in range(r):
        m.append([0] * c)

    return m


rows, columns = list(map(int, input().split(', ')))
matrix_sum = 0

matrix = generate_matrix(rows, columns)

for i in range(rows):
    matrix[i] = list(map(int,input().split(', ')))
    matrix_sum += sum(matrix[i])

print(matrix_sum)
print(matrix)
