number_of_electrons = int(input())
filled_shell = []
i = 0

while 0 < number_of_electrons:
    i += 1
    shell = 2 * i ** 2

    if number_of_electrons >= shell:
        filled_shell.append(shell)
        number_of_electrons -= shell
    else:
        filled_shell.append(number_of_electrons)
        number_of_electrons = 0

print(filled_shell)