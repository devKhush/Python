# List slicing
# https://www.sololearn.com/learning/1073/2453/5076/1

# string unpacking into list
listt = list('Hello, Khushdev')
print(listt)
print()

friends = ["Harry", "Tom", "Rohan", "Sam", "Divya", 45]

friend1, friend2, *remaining = friends
print(friend1, friend2, remaining)
print()

print(friends[0:4])
print(friends[-4:])

print(friends[:])
print(friends[::-1])

# same as strings
