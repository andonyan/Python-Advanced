def generate_matrix(r, c):
    m = []
    for _ in range(r):
        m.append([0] * c)

    return m


n = int(input())
matrix = generate_matrix(n, n)
diagonal_sum = 0

for i in range(n):
    matrix[i] = list(map(int, input().split()))

for k in range(n):
    diagonal_sum += matrix[k][k]

print(diagonal_sum)