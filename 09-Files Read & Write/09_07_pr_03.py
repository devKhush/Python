
for i in range(1, 21):

    # Open the required directory
    with open(f'Multiplication_Tables/table_of_{i}.txt', 'w') as file:
        file.write(f'Multiplication Table of {i}:\n\n')

        # writes table
        for j in range(1, 11):
            file.write(f'{i} X {j} = {i*j} \n')
