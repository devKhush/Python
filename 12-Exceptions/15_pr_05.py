num = int(input('Enter the number for multiplication table: '))

table = [num*i for i in range(1, 11)]
print(table)

with open('table.txt', 'a') as file:
    file.write('Multiplication Table of ' + str(num) + ' : ')
    file.write(str(table))
    file.write('\n\n')
