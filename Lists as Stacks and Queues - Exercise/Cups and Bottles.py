from collections import deque

cups = deque(map(int, input().split()))
bottles = deque(map(int, input().split()))
waste = 0

cups.reverse()

for i in range(len(cups) - 1, -1, -1):
    for k in range(len(bottles) - 1, -1, -1):

        if bottles[k] >= cups[i]:
            bottles[k] -= cups[i]
            waste += bottles[k]
            bottles.pop()
            cups.pop()
            break

        else:
            cups[i] -= bottles[k]
            bottles.pop()
            continue

    if bottles and not cups:
        print(f'Bottles: {" ".join(deque(map(str, bottles)))}')
        print(f'Wasted litters of water: {waste}')
        break
    elif cups and not bottles:
        print(f'Cups: {" ".join(reversed(deque(map(str, cups))))}')
        print(f'Wasted litters of water: {waste}')
        break
