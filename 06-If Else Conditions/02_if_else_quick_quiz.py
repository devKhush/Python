# use of Walrus operator

if age := int(input("Enter your age: ")):
    print("Yes")
    if age > 25 and age < 35:
        print('You can marry')
else:
    print("No")
