n = int(input())
odd_numbers = set()
even_numbers = set()


for i in range(1, n + 1):
    name = input()
    current_sum = 0
    for char in name:
        current_sum += ord(char)

    number = current_sum // i

    if number % 2 == 0:
        even_numbers.add(number)
    else:
        odd_numbers.add(number)

if sum(odd_numbers) == sum(even_numbers):
    print(', '.join(list(map(str, odd_numbers.union(even_numbers)))))

elif sum(odd_numbers) > sum(even_numbers):
    print(', '.join(list(map(str, odd_numbers.difference(even_numbers)))))

else:
    print(', '.join(list(map(str, odd_numbers.symmetric_difference(even_numbers)))))
