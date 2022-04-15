my_list = [i for i in range(1, 101)]

# print(my_list)

divisible_by = 5

filtered_list = list(filter(lambda number: number % divisible_by == 0,
                            my_list))
print(filtered_list)