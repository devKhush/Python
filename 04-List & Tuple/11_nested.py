
nested_tuple = ((1,2,3), (4,5), (7,8,9))
print(nested_tuple)
nested_tuple = (1,2,3), (4,5), (7,8,9)
print(nested_tuple)
print()

nested_list = [[1,2,3], [4,5,6], [7], ['kdev', 'p','khush', 9]]
print(nested_list) 
print(list(nested_tuple))
print()

nested = [(1,2), ['a', 'b', (11,22,33)]]
print(nested)
print()

nested1 = [nested_list, nested_tuple]
print(nested1)
print()

# Tuples inside list
nested2 = [(1,2),(3,4)]
nested2.append((5,6))
print(nested2)
print()

# List inside tuple
nested3 = ([1,2],[3,4])
nested3[0].append((5,6))
print(nested3)