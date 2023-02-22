import os

try:
    os.remove('text_file.txt')
except FileNotFoundError:
    print('File already deleted!')
    