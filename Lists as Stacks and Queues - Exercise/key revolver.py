from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = deque(map(int, input().split()))
locks = deque(map(int, input().split()))
intel_price = int(input())
counter = 0

for i in range(len(bullets) - 1, -1, -1):
    if bullets[i] <= locks[0]:
        bullets.pop()
        print('Bang!')
        locks.popleft()
        counter += 1
    else:
        bullets.pop()
        counter += 1
        print('Ping!')

    if counter % barrel_size == 0 and bullets:
        print('Reloading!')

    if bullets and not locks:
        print(f'{len(bullets)} bullets left. Earned ${intel_price - (counter * bullet_price)}')
        break
    elif locks and not bullets:
        print(f'Couldn\'t get through. Locks left: {len(locks)}')
        break
    elif not locks and not bullets:
        print(f'0 bullets left. Earned ${intel_price - (counter * bullet_price)}')
        break
