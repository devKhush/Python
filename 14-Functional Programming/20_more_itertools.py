from itertools import product, permutations

# https://www.geeksforgeeks.org/python-itertools-product/
# https://www.geeksforgeeks.org/python-itertools-permutations/

# ******************************************** product ********************************************
arr1 = [1, 2, 3]
arr2 = [5, 6, 7]
arr3 = [2, 5, 8, 9]

cartasien_product = list(product(arr1, arr2))
print(cartasien_product)

cartasien_product = list(product(arr1, arr2, arr3))
print(cartasien_product)
print()

cartasien_product = list(product(arr1, repeat=2))
print(cartasien_product)

cartasien_product = list(product(arr1, repeat=3))
print(cartasien_product)
print('\n')

# ******************************************** permutation ********************************************
arr1 = ['d', 'e', 'v']
permutation = list(permutations(arr1))
print(permutation)
print(len(permutation))
print()

permutation = list(permutations('dev!'))
print(permutation)
print(len(permutation))
print()

# compare with permutation formula n!/(n-k)!

arr1 = ['d', 'e', 'v']
permutation = list(permutations(arr1, 2))
print(permutation)
print(len(permutation))

permutation = list(permutations('dev!', 2))
print(permutation)
print(len(permutation))
print()
