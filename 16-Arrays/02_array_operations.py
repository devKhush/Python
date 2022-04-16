import array as arr

list_ = [1, 2, 3, 4, 5]
arr1 = arr.array('i', list_)
print(arr1)
print()

# Return a tuple (address, length) giving the current memory address and the length in items
# of the buffer used to hold array's contents.
print(arr1.buffer_info())
print()

# Array Indexing (same as normal indexing of list or strings)
print(arr1[-1])
print(arr1[1])
print(arr1[1:-1])       # reutrns an array & not a list
print()

# reverse array
arr1.reverse()
print(arr1)


# Arrays almost have all elements as present in case of list

arr1.append(6)
print(arr1)

arr1.insert(1, 10)
print(arr1)

arr1.remove(1)
print(arr1)

# arr1.sort()               # sort() not present, you can implement your own XD


print()
arr2 = arr.array('u', [])           # empty array   
print(arr2)
