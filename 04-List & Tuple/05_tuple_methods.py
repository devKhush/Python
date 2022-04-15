# https://www.w3schools.com/python/python_ref_tuple.asp

# Creating a tuple using ()
t1 = (1, 5, 2, 4, 5, 4, 1, 2, 1)
t2 = (10, 20, 30)


print('count of 1 in tuple is', t1.count(1))
print('index of 5 is', t1.index(5))
print('length of tuple is', len(t1))
print(max(t1))
print(min(t1))
print(sum(t1))

print()
print(3 in t1)
print(2 in t1)
print('a' in t1)

# Tuple concatenation
print('\nConcatenated Tuple:')
print(d := t1+t2[1:4])

# Tuple multiplication
print('\nTuple multiplication:')
print(e := (t1[0:2]+t2[2:])*3)
print()

list1 = [11,22,33]
tuple1 = tuple(list1)
print(tuple1)

