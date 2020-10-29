from collections import deque


def format_time(time):
    hours = time // 3600
    minutes = (time - (hours * 3600)) // 60
    seconds = time - ((hours * 3600) + (minutes * 60))

    if hours < 24:
        return f'[{hours:02d}:{minutes:02d}:{seconds:02d}]'
    else:
        return f'[{hours % 24:02d}:{minutes:02d}:{seconds:02d}]'


assembly_line = deque()
robots_queue = deque(
    [name, int(process_time), 0] for name, process_time in (item.split('-') for item in (input().split(';'))))
start_time = list(map(int, input().split(':')))
waiting_queue = deque()
current_time = start_time[0] * 3600 + start_time[1] * 60 + start_time[2]

product = input()

while product != 'End':
    assembly_line.append(product)
    product = input()

while len(assembly_line) > 0:
    current_time += 1

    for robot in waiting_queue:
        if current_time == robot[2] and robot[1] != 0:
            robots_queue.append(robot)
        elif robot[1] == 0:
            robots_queue.append(robot)

    waiting_queue = deque([robot for robot in waiting_queue if robot[2] > current_time and robot[1] != 0])

    if robots_queue:
        name = robots_queue[0][0]
        print(f'{name} - {assembly_line.popleft()} {format_time(current_time)}')
        robots_queue[0][2] = robots_queue[0][1] + current_time
        waiting_queue.append(robots_queue.popleft())

    else:
        assembly_line.append(assembly_line.popleft())
