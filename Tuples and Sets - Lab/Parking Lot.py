n = int(input())
parking_lot = set()

for _ in range(n):
    (direction, license_plate) = input().split(', ')

    if direction == 'IN':
        parking_lot.add(license_plate)
    elif direction == 'OUT' and license_plate in parking_lot:
        parking_lot.remove(license_plate)
else:
    if parking_lot:
        for car in parking_lot:
            print(car)
    else:
        print('Parking Lot is Empty')
