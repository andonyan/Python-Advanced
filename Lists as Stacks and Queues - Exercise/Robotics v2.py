from collections import deque


def format_time(time):
    hours = time // 3600
    minutes = (time - (hours * 3600)) // 60
    seconds = time - ((hours * 3600) + (minutes * 60))

    return f'[{hours:02d}:{minutes:02d}:{seconds:02d}]'


assembly_line = deque()
robots_queue = deque(
    [name, int(process_time)] for name, process_time in (item.split('-') for item in (input().split(';'))))
start_time = list(map(int, input().split(':')))
current_time = start_time[0] * 3600 + start_time[1] * 60 + start_time[2]
should_continue = True

for robot in robots_queue:
    robot.append(current_time + 1)

product = input()

while product != 'End':
    assembly_line.append(product)
    product = input()


while len(assembly_line) > 0:
    current_time += 1
    for robot in robots_queue:
        name = robot[0]
        processing_time = robot[1]
        finish_time = robot[2]

        if current_time >= finish_time:
            print(f'{name} - {assembly_line.popleft()} {format_time(current_time)}')
            robot[2] = current_time + processing_time
            robots_queue.append(robots_queue.popleft())
            break

        else:
            robots_queue.append(robots_queue.popleft())
            assembly_line.append(assembly_line.popleft())
            break



