list1 = [3, 53, 2, False, 6.2, "Harry"]

# How to get index of data inside list using for each loop?
# index = 0
# for item in list1:
#     print(item, index)
#     index += 1

print(enumerate(list1))
print(type(enumerate(list1)))
print()

for index, item in enumerate(list1):
    print(item, ",", index)
