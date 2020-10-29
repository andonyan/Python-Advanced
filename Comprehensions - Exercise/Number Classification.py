data = list(map(int, input().split(', ')))

print('Positive: ' + ', '.join([str(number) for number in data if number >= 0]))
print('Negative: ' + ', '.join([str(number) for number in data if number < 0]))
print('Even: ' + ', '.join([str(number) for number in data if number % 2 == 0]))
print('Odd: ' + ', '.join([str(number) for number in data if number % 2 != 0]))