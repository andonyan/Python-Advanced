regulars = set()
vips = set()

guest_count = int(input())

for _ in range(guest_count):
    name = input()
    if name[0].isdigit():
        vips.add(name)
    else:
        regulars.add(name)

while True:
    arrived_guest = input()

    if arrived_guest != 'END':

        if arrived_guest[0].isdigit() and arrived_guest in vips:
            vips.remove(arrived_guest)
        elif not arrived_guest[0].isdigit() and arrived_guest in regulars:
            regulars.remove(arrived_guest)

    else:
        print(f'{len(regulars) + len(vips)}')

        if vips:
            for vip in sorted(vips):
                print(vip)

        if regulars:
            for regular in sorted(regulars):
                print(regular)
        break
