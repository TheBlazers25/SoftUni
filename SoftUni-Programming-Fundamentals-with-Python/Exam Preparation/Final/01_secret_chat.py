data = input()

while True:
     command = input().split(':|:')
     current_command = command[0]

     if current_command == "Reveal":
         print(f"You have a new text message: {data}")

     elif current_command == "InsertSpace":
         index = int(command[1])
         data = data[:index] + ' ' + data[index:]
         print(data)

     elif current_command == "Reverse":
         substring = command[1]
         if substring in data:
             data = data.replace(substring, '', 1)
             data = data + substring[::-1]
             print(data)
         else:
             print("error")

     elif current_command == "ChangeAll":
         substring, replacement = command[1], command[2]
         data = data.replace(substring, replacement)
         print(data)




# concealed_message = input()
# command = input()
#
# def insert_spaces(index, concealed_message):
#     return concealed_message[:index] + " " + concealed_message[index:]
#
# def reverse(substring, concealed_message):
#     find_word = concealed_message.find(substring)
#     concealed_message = concealed_message[:find_word] + concealed_message[find_word + len(substring):]
#     concealed_message += substring[::-1]
#     return concealed_message
#
# def change_all(substring, replacement, concealed_message):
#     return concealed_message.replace(substring, replacement)
#
#




# import re
#
# concealed_message = input()
# concealed_message_list = list(concealed_message)
#
# while True:
#     command = input()
#
#     if command == "Reveal":
#         break
#
#     split_command = command.split(":|:")
#
#     if split_command[0] == "InsertSpace":
#         #concealed_message_list.insert(int(split_command[1]), " ")
#         concealed_message[:int(split_command[1])] + " " + concealed_message[int(split_command[1]):]
#         print(concealed_message)
#
#     if split_command[0] == "Reverse":
#         substring = split_command[1]
#         final_string = re.sub(substring, substring[::-1], concealed_message)
#
#
# print(concealed_message)
# print(final_string)
# print(concealed_message_list)
# print("".join(concealed_message_list))