from itertools import takewhile, accumulate, chain
import operator
import math
import functools

# https://www.geeksforgeeks.org/python-itertools-chain/
# https://www.geeksforgeeks.org/python-itertools-takewhile/
# https://www.geeksforgeeks.org/python-itertools-accumulate/

# https://www.sololearn.com/learning/1073/2466/5117/1


# **************************************** itertools.acumulate() ****************************************
print('*'*40, 'itertools.acumulate()', '*'*40)

# Return series of accumulated sums (or other binary function results).
nums = list(accumulate(range(10)))      # by default it performs sum
print(nums)

list_ = [1, 2, 3, 4, 5]
nums = list(accumulate(list_, operator.pow))
print(nums)

nums = list(accumulate(list_, math.pow))
print(nums)

nums = list(accumulate(list_, operator.sub))
print(nums)

nums = list(accumulate(list_, max))
print(nums)

nums = list(accumulate(list_, min))
print(nums)


# **************************************** itertools.takwhile() ****************************************
print('\n', '*'*40, 'itertools.takwhile()', '*'*40)

# Return successive entries from an iterable as long as the predicate evaluates to true for each entry
list_ = [0, 2, 4, 8, 22, 11, 34, 6, 60, 80, 100]
nums = list(takewhile(lambda x: x % 2 == 0, list_))
print(nums)


def isDigit(x: str) -> bool:
    return x.isdigit()


string = '12323asfer81294691'
digits = list(takewhile(isDigit, string))
print(digits)


# **************************************** itertools.chain() ****************************************
print('\n', '*'*40, 'itertools.chain()', '*'*40)

# Return a chain object whose .__next__() method returns elements from the first iterable until it is exhausted, then elements from the next iterable, until all of the iterables are exhausted.

odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8, 10]
# chaining odd and even numbers
numbers = list(chain(odd, even))
print(numbers)

consonants = ['d', 'f', 'k', 'l', 'n', 'p']
vowels = ['a', 'e', 'i', 'o', 'u']
res = list(chain(consonants, vowels))
print(res)

res = list(chain(s1 := 'ABC', s2 := 'DEF', s3 := 'GHI', s4 := 'JKL'))
print(res)

res = list(chain('ABC', vowels))
print(res)

nums = ['123', '456', '789']
result = list(chain(nums))
print(result)

nums = ['123', '456', '789']    
result = list(chain(*nums))
print(result)
result = functools.reduce(lambda a, b: a+b, list(map(int, result)))
print(result)
