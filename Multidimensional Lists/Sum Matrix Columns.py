def generate_matrix(r, c):
    m = []
    for _ in range(r):
        m.append([0] * c)

    return m


rows, columns = list(map(int, input().split(', ')))

matrix = generate_matrix(rows, columns)
for i in range(rows):
    matrix[i] = list(map(int, input().split()))

for i in range(columns):
    column_sum = 0
    for k in range(rows):
        column_sum += matrix[k][i]

    print(column_sum)