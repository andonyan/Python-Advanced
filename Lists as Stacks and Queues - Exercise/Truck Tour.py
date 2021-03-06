from collections import deque
n = int(input())
pumps = deque()
copy = deque()
fuel = 0
for _ in range(n):
    pump = list(map(int, input().split()))
    pumps.append(pump)
    copy.append(pump)

for i in range(n):

    fuel = 0
    is_valid = True
    for _ in range(n):
        current = pumps.popleft()
        fuel += current[0] - current[1]
        if fuel < 0:
            is_valid = False
        pumps.append(current)

    if is_valid:
        print(i)
        break

    pumps.append(pumps.popleft())