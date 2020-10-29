def generate_matrix(r, c):
    m = []
    for _ in range(r):
        m.append([0] * c)

    return m


def print_matrix(m):
    for j in range(len(m)):
        for z in range(len(m[j])):
            print(m[j][z], end='')
        print()


rows, columns = list(map(int, input().split()))
matrix = generate_matrix(rows, columns)

snake = input()
snake_index = 0
snake_max_index = len(snake) - 1

for i in range(rows):
    if i % 2 == 0:
        for k in range(columns):
            if snake_index > snake_max_index:
                snake_index = 0
                matrix[i][k] = snake[snake_index]
                snake_index += 1
            else:
                matrix[i][k] = snake[snake_index]
                snake_index += 1
    else:
        for k in range(1, columns + 1):
            if snake_index > snake_max_index:
                snake_index = 0
                matrix[i][-k] = snake[snake_index]
                snake_index += 1
            else:
                matrix[i][-k] = snake[snake_index]
                snake_index += 1


print_matrix(matrix)