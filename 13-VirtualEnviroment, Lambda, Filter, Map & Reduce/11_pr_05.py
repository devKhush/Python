from random import randint as randomNumber
from functools import reduce
'''
Return random integer in range [a, b], including both end points
'''

list_of_num = [randomNumber(1, 1000) for i in range(1, 101)]
print(max(list_of_num))
print(min(list_of_num))
print()

max_num = reduce(lambda a, b: max(a, b), list_of_num)
print(max_num)

# Another way for max()
max_num = reduce(max, list_of_num)
print(max_num)

# Same way for min() (Inbuilt func)
min_num = reduce(min, list_of_num)
print(min_num)
