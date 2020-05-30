def find_matching_brackets(text):
    index_stack = []
    for index in range(len(text)):
        if text[index] == '(':
            index_stack.append(index)
        elif text[index] == ')':
            print(text[index_stack.pop():index + 1:])


find_matching_brackets(input())
