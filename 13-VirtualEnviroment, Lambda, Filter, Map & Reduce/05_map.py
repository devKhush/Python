def square(num):
    return num * num


'''
The function map() takes a function and an iterable as arguments, 
and returns a new iterable with the function applied to each argument.
'''

list1 = [1, 2, 4]

# Method 1
l2 = []
for item in list1:
    l2.append(square(item))
print(l2)

# Method 2
print(list(map(square, list1)))

# Method 3
print(map(lambda x: x**2, list1))
print()

print(tuple(list1))
print(result := list(map(lambda x: x**2, list1)))
print(result := tuple(map(lambda x: x**2, list1)))
print(result := set(map(lambda x: x**2, list1)))
print(result)


print('\nEnter Integer Value:')
l = list(map(int, input().split()))
print(l)
