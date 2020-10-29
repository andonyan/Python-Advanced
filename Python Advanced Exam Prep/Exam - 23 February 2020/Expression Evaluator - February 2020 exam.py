import math

from collections import deque


def evaluate_expression(characters_list):

    current_characters = deque()

    result = int()

    for character in characters_list:

        try:

            current_characters.append(int(character))

        except (ValueError, TypeError):

            if character == '+':

                temp_result = sum(current_characters)

                current_characters.clear()

                current_characters.append(temp_result)

            elif character == '-':

                if len(current_characters) > 1:

                    temp_result = current_characters.popleft()

                    for i in range(len(current_characters)):
                        temp_result = temp_result - current_characters.popleft()

                    current_characters.append(temp_result)

                else:

                    continue

            elif character == '*':

                if len(current_characters) > 1:

                    temp_result = current_characters.popleft()

                    for i in range(len(current_characters)):
                        temp_result = temp_result * current_characters.popleft()

                    current_characters.append(temp_result)

                else:

                    continue

            elif character == '/':

                if len(current_characters) > 1:

                    temp_result = current_characters.popleft()

                    for i in range(len(current_characters)):
                        temp_result = temp_result / current_characters.popleft()

                    current_characters.append(math.floor(temp_result))

                else:

                    continue

    return current_characters.pop()


provided_string_characters = input().split()
print(evaluate_expression(provided_string_characters))
