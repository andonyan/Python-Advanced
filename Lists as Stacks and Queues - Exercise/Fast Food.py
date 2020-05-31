from collections import deque

food_quantity = int(input())
orders = deque(map(int, input().split()))
print(max(orders))

while len(orders) > 0:
    if orders[0] <= food_quantity:
        food_quantity -= orders.popleft()
    else:
        print(f'Orders left: {" ".join(list(map(str, orders)))}')
        break
else:
    print('Orders complete')

