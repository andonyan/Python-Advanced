Wn = int(input())

print([[val for val in map(int, (input().split(', '))) if val % 2 == 0] for i in range(n)])