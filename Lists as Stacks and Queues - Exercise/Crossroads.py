from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())
car_queue = deque()
cars_passed = 0
crash_occurred = False
crashed_car_index = None
crashed_car_character = None

while True:
    command = input()

    if command == 'END':
        print('Everyone is safe.')
        print(f'{cars_passed} total cars passed the crossroads.')
        break

    elif command == 'green':
        car_queue_copy = car_queue.copy()
        time_remaining = green_light_duration
        bonus_time_remaining = free_window_duration

        for i in range(len(car_queue_copy)):

            if len(car_queue_copy[i]) <= time_remaining:
                time_remaining -= len(car_queue_copy[i])
                cars_passed += 1
                if time_remaining == 0:
                    car_queue.popleft()
                    break
                else:
                    car_queue.popleft()
                    continue

            else:
                if time_remaining + bonus_time_remaining >= len(car_queue_copy[i]):
                    cars_passed += 1
                    car_queue.popleft()
                    break
                else:
                    crash_occurred = True
                    crashed_car_character = car_queue_copy[i][-(len(car_queue_copy[i]) - (time_remaining + bonus_time_remaining))]
                    crashed_car_index = car_queue_copy[i]
                    break


    else:
        car_queue.append(command)

    if crash_occurred:
        print('A crash happened!')
        print(f'{crashed_car_index} was hit at {crashed_car_character}.')
        break
