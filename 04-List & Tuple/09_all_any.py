# https://www.geeksforgeeks.org/any-all-in-python/

# All function

list1 = [13, 2, 9, 40, 51, 52, 22, 45]

if all(l := [i > 0 for i in list1]):
    print(l)
    print('All are greater than 0   V1... \n')

if all(l := [i for i in list1 if i > 0]):
    print(l)
    print('All are greater than 0   V2... \n')

if all(l := [i > 5 for i in list1]):
    print(l)
    print('All are greater than 5... \n')


# Any function

if any(l := [i for i in list1 if i % 2 == 0]):
    print(l)
    print('Atleast one is even... \n')

if any(l := [i for i in list1 if i > 100]):
    print(l)
    print('Atleast one is greater than 100... \n')
