number_of_names = int(input())
names = set()

for _ in range(number_of_names):
    name = input()
    names.add(name)

for name in names:
    print(name)
