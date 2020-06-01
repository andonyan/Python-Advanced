from collections import deque

n = int(input())
pumps = deque()
circle_complete = False

for _ in range(n):
    pumps.append(list(map(int, input().split())))

for i in range(n):
    head = i
    tail = i + n
    fuel = 0

    for k in range(head, tail):
        if k <= n - 1:
            fuel += pumps[k][0]
            distance = pumps[k][1]
            if fuel >= distance:
                fuel -= distance
                continue
            else:
                break
        else:
            fuel += pumps[k - n][0]
            distance = pumps[k - n][1]
            if fuel >= distance:
                fuel -= distance
                continue
            else:
                break
    else:
        circle_complete = True

    if circle_complete:
        print(i)
        break
