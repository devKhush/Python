# https://www.geeksforgeeks.org/iterators-in-python/

list = [1,2,3,4,5]
iteratorObject = iter(list)

for _ in range(len(list)):
    val = iteratorObject.__next__()
    print(val, end=' ')

print('\n', '*'*40, 'Example 1 Done', '*'*40, '\n')


# Here is an example of a python inbuilt iterator
# value can be anything which can be iterate
iterable_value = 'Geeks'
iterable_obj = iter(iterable_value)
halted = False

while not halted:
    try:
        value = next(iterable_obj)
        print(value)
    except StopIteration as e:
        print('IterationError Ocurred') 
        halted = True
print('*'*40, 'Example 2 Done', '*'*40, '\n')


iterable_value = ['a','b','c','d']
iterable_obj = iter(iterable_value)

while True:			# exception will happen when iteration will over
    item = next(iterable_obj)
    print(item)

