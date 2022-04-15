class Employee:
    company = "Google"          # static/class attribute
    salary = 100                # static/class attribute


# NOTE: MUST READ

harry = Employee()
rajni = Employee()

print(harry.company)        # this is a class variable
print(rajni.company)        # this is a class variable
print(harry.salary)         # this is a class variable
print(rajni.salary)         # this is a class variable
# print(harry.age)      # error as there is no class or instance attribute with name 'age'
# print(rajni.age)
print()

# NOTE:Instance variables get preferrence on class attributes over Assignment and Retrival
# assigning a value to a variable/attributes of objects (in OOPs) always creates a instance variable
# So, if we want to change Class-type variable, use ClassName.VariabelName
Employee.company = "YouTube"        # this is a class variable

# Some object of same classes in python may have attributes that
# other objects (of same class) doesn't have (Eg here below)
# Such attributes need to be defines externally in the program (not inside the Class)
# But this work may become tedious for every instance for that class (use constructors)

# NOTE: Instance variable takes preference on Class Variables over Assignment and Retrival
# a new instance variable is added in this case with name same as the class-vatiable name
# this adds a new instance variable/attribute even though class variable exits with this name and
# this willn't change class varaible, bcoz direcly assigning creates instance variable
harry.salary = 300      # Now, this is a instance variable due to preference
harry.age = 19          # Now, this is a instance variable due to preference
rajni.salary = 400      # Now, this is a instance variable || Try uncommenting & see output


print(harry.company)    # this is a class variable
print(rajni.company)    # this is a class variable
print(harry.salary)     # Now, this is a instance variable due to preference
print(rajni.salary)     # Now, this is a instance variable due to preference
print(harry.age)        # Now, this is a instance variable due to preference
# print(rajni.age)      # error as rajni's age is still not defined


# NOTE:
# How varaibles are retrived?
# 1) First checks for Instance variable/attributes
# 2) If Instance variable not found, then checks for Class attributes
# 3) If class attribute also not found, then gives error
