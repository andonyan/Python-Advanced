start = int(input())
end = int(input())

print([num for num in {i for i in range(start, end + 1) for k in range(2, 11) if i % k == 0}])