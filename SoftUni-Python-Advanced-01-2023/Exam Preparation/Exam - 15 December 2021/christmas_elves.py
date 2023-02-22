from collections import deque

elf_energy = deque(int(n) for n in input().split())
number_of_materials_in_box = [int(n) for n in input().split()]

toys = 0
time = 0
total_used_energy = 0

while True:

    if not elf_energy:
        break

    if not number_of_materials_in_box:
        break

    while elf_energy[0] < 5:
        current_elf = elf_energy.popleft()
        if len(elf_energy) == 0:
            break
    if len(elf_energy) == 0:
        break

    time += 1

    if time % 3 != 0:
        if elf_energy[0] >= number_of_materials_in_box[-1]:
            if time % 5 == 0:
                elf_energy[0] -= number_of_materials_in_box[-1]
            else:
                elf_energy[0] -= number_of_materials_in_box[-1] - 1
                toys += 1

            total_used_energy += number_of_materials_in_box[-1]
            number_of_materials_in_box.pop()
            elf_energy.append(elf_energy.popleft())
        else:
            elf_energy[0] *= 2
            elf_energy.append(elf_energy.popleft())
    elif time % 3 == 0:
        if elf_energy[0] >= number_of_materials_in_box[-1] * 2:
            if time % 5 == 0:
                elf_energy[0] -= number_of_materials_in_box[-1] * 2
            else:
                elf_energy[0] -= number_of_materials_in_box[-1] * 2 - 1
                toys += 2
            total_used_energy += number_of_materials_in_box[-1] * 2
            number_of_materials_in_box.pop()
            elf_energy.append(elf_energy.popleft())
        else:
            elf_energy[0] *= 2
            elf_energy.append(elf_energy.popleft())

    # if time % 3 == 0:
    #     needed_energy = current_number_of_materials * 2
    #     if needed_energy <= current_elf:
    #         left_over_elf_energy = (current_elf - needed_energy)
    #         total_used_energy += (current_elf - left_over_elf_energy)
    #         elf_energy.append(left_over_elf_energy + 1)
    #         toys += 2
    #
    #     else:
    #         elf_energy.append(current_elf * 2)
    #         number_of_materials_in_box.append(current_number_of_materials)
    #
    # elif time % 5 == 0:
    #     if current_elf > current_number_of_materials:
    #         left_over_elf_energy = (current_elf - current_number_of_materials)
    #         total_used_energy += (current_elf - left_over_elf_energy)
    #     total_used_energy += current_elf
    #
    # elif current_elf >= current_number_of_materials:
    #     left_over_elf_energy = (current_elf - current_number_of_materials)
    #     total_used_energy += (current_elf - left_over_elf_energy)
    #     elf_energy.append(left_over_elf_energy + 1)
    #     toys += 1
    #
    # else:
    #     left_over_elf_energy = current_elf * 2
    #     elf_energy.append(left_over_elf_energy)
    #     number_of_materials_in_box.append(current_number_of_materials)

print(f'Toys: {toys}')
print(f'Energy: {total_used_energy}')
if elf_energy:
    print(f'Elves left: {", ".join(map(str, elf_energy))}')
if number_of_materials_in_box:
    print(f'Boxes left: {", ".join(map(str, number_of_materials_in_box))}')
