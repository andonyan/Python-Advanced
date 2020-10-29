def numbers_searching(*args):
    received_sequence = []
    for arg in args:
        received_sequence.append(arg)

    received_sequence.sort()

    unique_values = set()
    duplicate_values = []
    for number in received_sequence:
        if number in unique_values:
            duplicate_values.append(number)
        else:
            unique_values.add(number)

    missing_number = [num for num in range(received_sequence[0], received_sequence[-1] + 1) if num not in unique_values]

    return [missing_number[0], sorted(list(set(duplicate_values)))]