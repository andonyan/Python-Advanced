queue = []

while True:
    name = input()
    if name != 'End' and name != 'Paid':
        queue.append(name)
    else:
        if name == 'Paid':
            queue.reverse()
            while len(queue) > 0:
                print(queue.pop())
        else:
            print(f'{len(queue)} people remaining.')
            break
