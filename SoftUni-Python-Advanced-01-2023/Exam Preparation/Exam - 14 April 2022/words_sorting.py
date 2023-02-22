def words_sorting(*args):
    words_dictionary = {}
    final_string = []
    total_sum = 0

    for words in args:
        words_dictionary[words] = []

        for word in words:
            sum_value = sum([ord(word) for word in words])
        total_sum += int(sum_value)
        words_dictionary[words] = sum_value

    if total_sum % 2 == 0:
        even_sorted_values = sorted(words_dictionary.items())
        for word, value in even_sorted_values:
            final_string.append(f"{word} - {value}")

    elif total_sum % 2 != 0:
        odd_sorted_values = sorted(words_dictionary.items(), key=lambda x: -x[1])
        for word, value in odd_sorted_values:
            final_string.append(f"{word} - {value}")

    return "\n".join(final_string)


print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
