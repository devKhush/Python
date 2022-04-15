# string formatting
# https://www.sololearn.com/learning/1073/2455/5083/1

l = [1, 2, 3, 4]

# Each argument of the format function is placed in the string at
# the corresponding position, which is determined using the curly braces { }.
str = "List is : [{}, {}, {}, {}]".format(l[0], l[1], l[2], l[3])
print(str)


l = ["a", "b", "c", "d"]
str = "List is : [{0}, {0}, {1}, {3}, {2}, {3}, {1}, {2}, {0}, {1}]".format(
    l[0], l[1], l[2], l[3]
)
print(str)


# String formatting can also be done with named arguments.
# Try changing ':.2f' to ':.0f'   CGPA will be rounded

my_name, my_age = "Khushdev", 19
my_place, my_cgpa = "New Delhi", 8.733333333333
my_college = "IIITD"
print()
intro = "My name is {name}. \nMy age is {age}. \nI live in {place}. \nMy study in {college}. \nMy CGPA is {cgpa:.0f}".format(
    name=my_name, age=my_age, college=my_college, cgpa=my_cgpa, place=my_place
)
print(intro)


# Round func
cgpa = 8.7861968
print(f"\nCGPA : {round(cgpa, 4)}")
