try:
    text_file = open('lore.txt', 'r')
    print('File found')
except FileNotFoundError:
    print('File not found')