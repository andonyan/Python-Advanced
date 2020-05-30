from collections import deque

queue = deque()
water_quantity = int(input())

while True:
    name = input()
    if name != 'Start' and name != 'End':
        queue.append(name)
    else:
        if name == 'Start':
            while len(queue) > 0:
                quantity_required = input().split()
                if 'refill' not in quantity_required:

                    if int(quantity_required[0]) <= water_quantity:
                        print(f'{queue.popleft()} got water')
                        water_quantity -= int(quantity_required[0])
                    else:
                        print(f'{queue.popleft()} must wait')
                else:
                    water_quantity += int(quantity_required[1])
        else:
            print(f'{water_quantity} liters left')
            break
