r, c = map(int, input().split())
matrix = [[f'{chr(i + 97)}{chr(i + k + 97)}{chr(i + 97)}' for k in range(c)] for i in range(r)]

[print(' '.join(row)) for row in matrix]


# matrix =
# print(matrix)
# for i in range(r):
#     for k in range(c):
#         print("".join([chr(i + 97), chr(i + k + 97), chr(i + 97)]), end=' ')
#     print()


