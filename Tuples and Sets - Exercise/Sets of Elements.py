(length_n, length_m) = (map(int, input().split()))
set_n = set()
set_m = set()

for _ in range(length_n):
    set_n.add(int(input()))

for _ in range(length_m):
    set_m.add(int(input()))

for number in (set_n.intersection(set_m)):
    print(number)