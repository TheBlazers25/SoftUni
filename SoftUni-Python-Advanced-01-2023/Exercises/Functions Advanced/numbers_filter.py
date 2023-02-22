def even_odd_filter(**kwargs):
    filtered_dictionary = {}

    for number_type, numbers in kwargs.items():
        if number_type == "even":
            filtered_dictionary[number_type] = [x for x in numbers if x % 2 == 0]

        elif number_type == "odd":
            filtered_dictionary[number_type] = [x for x in numbers if x % 2 != 0]

    return dict(sorted(filtered_dictionary.items()))

print(even_odd_filter(
odd=[1, 2, 3, 4, 10, 5],
even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))