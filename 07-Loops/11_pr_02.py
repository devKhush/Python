l1 = ["Harry", "Sohan", "Sachin", "Rahul"]

for name in l1:
    if name[0].lower() == 's':
        print('Hello', name)

    if name.startswith("S"):
        print("Hello " + name)

    print()
