n = int(input())
longest_intersection = []
intersections = {}

for i in range(n):
    ranges = input().split('-')
    first_start, first_finish = ranges[0].split(',')
    second_start, second_finish = ranges[1].split(',')

    set_a = set(range(int(first_start), int(first_finish) + 1))
    set_b = set(range(int(second_start), int(second_finish) + 1))

    intersection = set_a.intersection(set_b)
    if len(intersection) > len(longest_intersection):
        longest_intersection = list(intersection)

print(f'Longest intersection is {longest_intersection} with length {len(longest_intersection)}')
