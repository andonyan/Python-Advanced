def generate_matrix(r, c):
    m = []
    for _ in range(r):
        m.append([0] * c)

    return m


n = int(input())
matrix = generate_matrix(n, n)
diagonal_sum = 0

for i in range(n):
    matrix[i] = [char for char in input()]

symbol = input()
symbol_found = False

for i in range(n):
    for k in range(n):
        if matrix[i][k] == symbol:
            print(f'({i}, {k})')
            symbol_found = True
            break

    if symbol_found:
        break
else:
    print(f'{symbol} does not occur in the matrix')
