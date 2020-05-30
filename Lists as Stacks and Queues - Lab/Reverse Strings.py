def reverse_string(string):
    stack = list(string)
    reversed_string = ''
    for _ in range(len(stack)):
        reversed_string += stack.pop()

    return reversed_string


print(reverse_string(input()))
