f1 = input("Enter Fruit Number 1: ")
f2 = input("Enter Fruit Number 2: ")
f3 = input("Enter Fruit Number 3: ")
f4 = input("Enter Fruit Number 4: ")
f5 = input("Enter Fruit Number 5: ")
f6 = input("Enter Fruit Number 6: ")
f7 = input("Enter Fruit Number 7: ")

myFruitList = [f1, f2, f3, f4, f5, f6, f7]
print(myFruitList)


# OP shortcut 1 ### (with list comprehension)
fruits = [input(f"Fruit name {i+1}: ") for i in range(5)]
print(fruits)

# OP shortcut 2 ###  (with walrus operator & list comprehension)
print(fruits := [input(f"Fruit name {i+1}: ") for i in range(5)])
