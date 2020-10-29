def generate_matrix(r, c):
    m = []
    for _ in range(r):
        m.append([0] * c)

    return m


def get_diagonal_sum(m, s):
    if s == 'primary':
        diagonal = 0
        for i in range(len(m)):
            diagonal += m[i][i]

        return diagonal

    elif s == 'secondary':
        diagonal = 0
        for i in range(len(m)):
            diagonal += m[i][len(m) - 1 - i]

        return diagonal


n = int(input())
matrix = generate_matrix(n, n)

for i in range(len(matrix)):
    matrix[i] = list(map(int, input().split()))

diagonal_difference = abs(get_diagonal_sum(matrix, 'primary') - get_diagonal_sum(matrix, 'secondary'))

print(diagonal_difference)