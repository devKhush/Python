# https://www.w3schools.com/python/python_ref_set.asp

# Creating an empty set
b = set()
print(type(b))


# Adding values to an empty set
b.add(4)
b.add(4)
b.add(5)
b.add(5)  # Adding a value repeatedly does not changes a set
b.add((4, 5, 6))

# Accessing Elements
# b.add([4, 5])         # Can't add list as list are hashable/changeable
# b.add({4:5, 6:8})     # Cannot add list or dictionary to sets, but 'tuple' can be added
print(b)

# Length of the Set
print('\nlength of set:', len(b), '\n')       # Prints the length of this set


# Removal of an Item from set
b.remove(5)  # Removes 5 from set b
# throws an error while trying to remove 15 (which is not present in the set)
# b.remove(15)
print(b)


b.add(100)
print(b)
print(b.pop())      # removes any random value form the 'set'
print(b)

print('\nUnion of sets:')
print(union := b.union({1, 2, 3, 4}))

print('\nIntersection of sets:')
print(intersection := b.intersection({(4, 5, 6, 1), 2}))
print(intersection := b.intersection({(4, 5, 6), 2}))

print('\nSubset check in sets:')
print(b.issubset({1, 2, 3, 4, 5, 6, (4, 5, 6)}))

print('\nCleared set:')
b.clear()
print(b)
