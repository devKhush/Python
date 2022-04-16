import array as arr

# https://www.geeksforgeeks.org/python-arrays/

# Ararys are container that holds values of the same type
# In Python, Array's size can be changed just as list
# Syntax => arr = array(type_code, [elements])


# ***************************** Integer arrays *****************************

arr1 = arr.array('i', [0, 1, 1, 2, 5, 6])
print(arr1)
print()

print('********************************************** Itertion using for loop 1 **********************************************')
for i in arr1:
    print(i, end=' ')
print('\n')

print('********************************************** Itertion using for loop 2 **********************************************')
for i in range(0, len(arr1)):
    print(arr1[i], end=' ')
print('\n')


# ***************************** String arrays *****************************

arr2 = arr.array('u', ['a', 'b', 'c', 'd', 'e'])
print(arr2)
arr3 = arr.array('u', 'Khushdev Pandit')
print(arr3)
print()

for i in arr3:
    print(i, end='')
print('\n')

# arr2 = arr.array('u', ['a', 'b', 'c', 1])     # TypeError as array item must be (type-code type) character only


# ***************************** Integer arrays *****************************

arr4 = arr.array('I', [0, 1, 2, 3, 4])
print(arr4)

# TypeError as array item must be (type-code type) character only
# arr4 = arr.array('I', [1, 2, 3, 4, -1])             # 'I' for unsigned int (non-neg value)
