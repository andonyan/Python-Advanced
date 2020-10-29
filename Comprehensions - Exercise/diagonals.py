n = int(input())
matrix = [list(map(int, input().split(', '))) for i in range(n)]
first_diagonal = [matrix[i][i] for i in range(n)]
second_diagonal = [matrix[i][n - 1 - i] for i in range(n)]
print(f'First diagonal: {", ".join([str(k) for k in first_diagonal])}. Sum: {sum(first_diagonal)}')
print(f'Second diagonal: {", ".join([str(k) for k in second_diagonal])}. Sum: {sum(second_diagonal)}')




