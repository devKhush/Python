# https://docs.python.org/3/tutorial/datastructures.html
# https://www.w3schools.com/python/python_ref_list.asp

l1 = [1, 8, 7, 2, 21, 15]
print(l1)

l1.sort()            # sorts the list
print(l1)

l1.reverse()         # reverses the list
print(l1)

l1.append(45)        # adds 45 at the end of the list
print(l1)

l1.insert(2, 50)    # inserts 544 at index 2
print(l1)

l1.pop()            # removes element at index len(list)-1, i.e, last element & return it
print(l1)


returned_element = l1.pop()      # removes the last element & return it
print('returned_element:', returned_element, ' & l1:', l1)

returned_element = l1.pop(2)     # removes element at index 2 & return it
print('returned_element:', returned_element, ' & l1:', l1)

# Remove first occurrence of value.
l1.remove(21)        # removes 21 from the list
print(l1)

# NOTE: append() ('at the end') & pop() can used as together as stack

l1[3] = 100
index = l1.index(100)
print(index)

# index = l1.index(10)      # -> error
# print(index)

print('list 2:', l2 := l1.copy())

print('\ncount of 90 in l1:', l1.count(90))

l1.extend([11, 22, 33, 44])     # adds at the end
print(l1)

print(3 in l1)
print(2 in l1)
print('a' in l1)

print('max value in 11 is', max(l1))
print('min value in 11 is', min(l1))
print('sum of value in 11 is', sum(l1))
