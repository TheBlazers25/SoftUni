event = ""
coffee = 0
while event != "END":
    event = input()
    if event.lower() == "coding" or \
            event.lower() == "cat" or \
            event.lower() == "dog" or \
            event.lower() == "movie":
            if event.islower():
                coffee += 1
            else:
                coffee += 2
if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)
