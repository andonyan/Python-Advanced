stack = list(map(int, input().split()))
rack_capacity = int(input())
current_load = 0
required_racks = 1

while len(stack) > 0:
    current_item = stack.pop()
    current_load += current_item
    if current_load < rack_capacity:
        continue
    elif current_load == rack_capacity and len(stack) > 0:
        current_load = 0
        required_racks += 1
    elif current_load == rack_capacity and len(stack) == 0:
        print(required_racks)
        break
    else:
        required_racks += 1
        current_load = current_item
else:
    print(required_racks)