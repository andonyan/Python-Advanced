from collections import deque

opening_brackets = ['{', '[', '(']
closing_brackets = ['}', ']', ')']
text = input()
stack = deque()

if len(text) % 2 != 0:
    print('NO')
else:
    for char in text:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            bracket = stack.pop()
            if bracket == '(' and ord(char) != 41:
                print('NO')
                break
            elif bracket == '[' and ord(char) != 93:
                print('NO')
                break
            elif bracket == '{' and ord(char) != 125:
                print('NO')
                break

    else:
        print('YES')

