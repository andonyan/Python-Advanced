from collections import deque


def format_time(time):
    hours = time // 3600
    minutes = (time - (hours * 3600)) // 60
    seconds = time - ((hours * 3600) + (minutes * 60))

    return f'[{hours:02d}:{minutes:02d}:{seconds:02d}]'


assembly_line = deque()
robots_queue = deque(
    [name, int(process_time)] for name, process_time in (item.split('-') for item in (input().split(';'))))
busy_robots = deque()
start_time = list(map(int, input().split(':')))
current_time = start_time[0] * 3600 + start_time[1] * 60 + start_time[2]
new_list = []

for robot in robots_queue:
    robot.append(0)

product = input()

while (len(assembly_line)) >= 0 and product != 'End':
    current_time += 1

    if product == 'End':
        continue

    assembly_line.append(product)

    if busy_robots:
        for i in range(len(busy_robots)):
            if current_time == busy_robots[i][2]:
                robots_queue.append(busy_robots[i])
            else:
                new_list.append(busy_robots[i])
        else:
            busy_robots = new_list

    if len(robots_queue) > 0:
        print(f'{robots_queue[0][0]} - {assembly_line.popleft()} {format_time(current_time)}')
        robots_queue[0][2] += current_time + robots_queue[0][1]
        busy_robots.append(robots_queue.popleft())
    else:
        while len(robots_queue) == 0:
            new_list.clear()
            assembly_line.append(assembly_line.popleft())
            current_time += 1
            for i in range(len(busy_robots)):
                if current_time == busy_robots[i][2]:
                    robots_queue.append(busy_robots[i])
                else: 
                    new_list.append(busy_robots[i])

        else:
            print(f'{robots_queue[0][0]} - {assembly_line.popleft()} {format_time(current_time)}')
            robots_queue[0][2] = robots_queue[0][1] + current_time
            busy_robots.append(robots_queue.pop())

    product = input()
