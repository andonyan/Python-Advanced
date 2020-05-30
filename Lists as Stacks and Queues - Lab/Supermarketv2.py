from collections import deque

queue = deque()

while True:
    name = input()
    if name != 'End' and name != 'Paid':
        queue.append(name)
    else:
        if name == 'Paid':
            while len(queue) > 0:
                print(queue.popleft())
        else:
            print(f'{len(queue)} people remaining.')
            break
