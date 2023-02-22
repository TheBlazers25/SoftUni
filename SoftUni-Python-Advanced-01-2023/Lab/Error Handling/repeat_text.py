text = input()


while True:
    try:
        repeat_number = int(input())
        for i in range(repeat_number):
            print(text, end='')
        break

    except ValueError:
        print("Value")
        break
