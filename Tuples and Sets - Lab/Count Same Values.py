def count_values(values):
    values_dict = {}
    for value in values:
        if value in values_dict:
            values_dict[value] += 1
        else:
            values_dict[value] = 1

    return values_dict


def print_values(dictionary):
    for key , value in dictionary.items():
        print(f'{key:.1f} - {value} times')


values_list = list(map(float, input().split()))
print_values(count_values(values_list))