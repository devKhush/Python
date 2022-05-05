# use of Walrus operator

if age := int(input("Enter your age: ")):
    print("Yes")
    if age > 25 and age < 35:
        print('You can marry')
else:
    print("No")
print()


# another quiz
x = True
y = False
z = False

# exrpession/consitions are evaluated from left to right
if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)
