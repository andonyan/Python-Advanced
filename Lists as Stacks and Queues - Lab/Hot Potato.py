from collections import deque

queue = deque(input().split())
step = int(input())

while len(queue) > 1:
    for i in range(1, step):
        queue.append(queue.popleft())
    else:
        print(f'Removed {queue.popleft()}')
else:
    print(f'Last is {queue.pop()}')