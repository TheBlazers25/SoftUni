def sorting_cheeses(**cheeses):
    cheeses = sorted(cheeses.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []

    for (cheese_name, quantity) in cheeses:
        result.append(cheese_name)
        quantity_list = sorted(quantity, reverse=True)
        result += quantity_list

    return "\n".join([str(x) for x in result])
