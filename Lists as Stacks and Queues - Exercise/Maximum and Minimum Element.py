n = int(input())
stack = list()

for _ in range(n):
    command = list(map(int, input().split()))
    if command[0] == 1:
        stack.append(command[1])
    elif command[0] == 2 and len(stack) > 0:
        stack.pop()
    elif command[0] == 3 and len(stack) > 0:
        print(max(stack))
    elif command[0] == 4 and len(stack) > 0:
        print(min(stack))
    elif command[0] != 2 and command[0] != 3 and command[0] != 4:
        stack.append(command[0])
else:
    print(', '.join(list(map(str, stack[::-1]))))

