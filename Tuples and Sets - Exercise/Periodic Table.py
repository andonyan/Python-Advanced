n = int(input())
chemical_compounds = set()

for _ in range(n):
    for element in input().split():
        chemical_compounds.add(element)
else:
    for element in chemical_compounds:
        print(element)