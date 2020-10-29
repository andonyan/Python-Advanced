def generate_matrix(r, c):
    m = []
    snake_index = []
    burrows_index = []
    for i in range(r):
        row = input()
        for item in row:
            if item == 'S':
                snake_index = [i, row.index(item)]
            elif item == 'B':
                burrows.append([i, row.index(item)])
        m.append(row)

    return m, snake_index, burrows_index


def print_matrix(m):
    for i in range(len(m)):
        for k in range(len(m[i])):
            print(m[i][k], end=' ')
        print()


def next_field_coordinates(snake, direction):
    current_row = snake[0]
    current_col = snake[1]
    if direction == 'left':

        if 0 <= current_col - 1:
            new_col = current_col - 1
            return [current_row, new_col]
        else:
            return False

    elif direction == 'right':

        if current_col + 1 <= n - 1:
            new_col = current_col + 1
            return [current_row, new_col]
        else:
            return False

    elif direction == 'up':

        if current_row - 1 >= 0:
            new_row = current_row - 1
            return [new_row, current_col]
        else:
            return False

    elif direction == 'down':

        if current_row + 1 <= n - 1:
            new_row = current_row + 1
            return [new_row, current_col]
        else:
            return False


food_eaten = 0
n = int(input())
matrix, snake, burrows = generate_matrix(n, n)


while food_eaten < 10:

    command = input()
    result = next_field_coordinates(snake, command)

    if not result:
        matrix[snake[0]][snake[1]].replace('-', '.')
        print('Game over!')
        print(f'Food eaten: {food_eaten}')
        print_matrix(matrix)
        break

    else:
        snake_current_row, snake_current_col = snake
        snake_new_row, snake_new_col = result
        matrix[snake_current_row][snake_current_col] = matrix[snake_current_row][snake_current_col].replace('-')

        if matrix[snake_new_row][snake_new_col] == '*':

            food_eaten += 1
            matrix[snake_new_row][snake_new_col] = 'S'
            snake = [snake_new_row, snake_new_col]
            if food_eaten >= 10:
                print('You won! You fed the snake.')
                print(f'Food eaten: {food_eaten}')
                print_matrix(matrix)
                break

        elif matrix[snake_new_row][snake_new_col] == 'B':

            exit_point_list = [coordinates for coordinates in burrows if snake != coordinates]
            exit_point = exit_point_list[0]
            matrix[snake_current_row][snake_current_col] = '.'
            matrix[snake_new_row][snake_new_col] = 'S'
            snake = [exit_point[0], exit_point[1]]

        else:

            matrix[snake_current_row][snake_current_col] = '.'
            matrix[snake_new_row][snake_new_col] = 'S'
            snake = [snake_new_row, snake_new_col]