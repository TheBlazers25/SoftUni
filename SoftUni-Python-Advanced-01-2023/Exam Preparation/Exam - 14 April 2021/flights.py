def flights(*args):
    result = {}
    for i in range(0, len(args), 2):
        if args[i] == 'Finish':
            break
        destination, passengers = args[i], args[i + 1]
        result[destination] = result.get(destination, 0) + passengers
    return result


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))