n = 5

multiplication_table = [f'{n} X {i} = {n*i}' for i in range(1, 11)]
print(multiplication_table)
print()

multiplication_table_in_string = '\n'.join(multiplication_table)
print(multiplication_table_in_string)