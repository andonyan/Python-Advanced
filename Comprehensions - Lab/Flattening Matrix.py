n = int(input())

print([number for i in range(n) for number in map(int, input().split(', '))])

