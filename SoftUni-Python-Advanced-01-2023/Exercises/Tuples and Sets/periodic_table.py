number_of_elements = int(input())

chemical_elements_set = set([])

for _ in range(number_of_elements):
    chemical_element = input().split()
    for element in chemical_element:
        chemical_elements_set.add(element)


print(*chemical_elements_set, sep="\n")

