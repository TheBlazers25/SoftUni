data = input()

while True:
     command = input().split('|')
     current_command = command[0]

     if current_command == 'Decode':
         print(f'The decrypted message is: {data}')
         break

     elif current_command == 'Move':
         letter = int(command[1])
         data = data[letter:] + data[:letter]

     elif current_command == 'Insert':
         index = int(command[1])
         data = data[:index] + command[2] + data[index:]

     elif current_command == 'ChangeAll':
         substring, replacement = command[1], command[2]
         data = data.replace(substring, replacement)
