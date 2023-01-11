elements = input().split()
indexes = input()
number_of_moves = 0
while indexes != "end":
    first_index, second_index = [int(x) for x in indexes.split()]
    len_elements = len(elements)
    number_of_moves += 1

    if first_index == second_index or not 0 <= first_index < len_elements or not 0 <= second_index < len_elements:
        cut_in_half = int(len_elements/2)
        element_to_insert = f"-{number_of_moves}a"
        elements = elements[:cut_in_half] + [element_to_insert, element_to_insert] + elements[cut_in_half:]

        # elements.insert(cut_in_half, element_to_insert)
        # elements.insert(cut_in_half, element_to_insert)


        # for x in range(2):
        #     elements.insert(cut_in_half, element_to_insert)

        print("Invalid input! Adding additional elements to the board")

    elif elements[first_index] == elements[second_index]:
        print(f"Congrats! You have found matching elements - {elements[first_index]}!")
        del elements[first_index]
        if first_index < second_index:
            second_index -= 1
        del elements[second_index]

    else:
        print("Try again!")

    if not elements:
        break

    indexes = input()


if elements:
    print("Sorry you lose :(\n", *elements)

else:
    print(f"You have won in {number_of_moves} turns!")
