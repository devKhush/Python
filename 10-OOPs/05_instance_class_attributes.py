class Employee:
    company = "Google"          # static/class attribute
    salary = 100                # static/class attribute


harry = Employee()
rajni = Employee()

# This is Creating instance attribute salary for both the objects
# harry.salary = 300
# rajni.salary = 400

harry.salary = 45       # instance attribute gets created for 'harry'
print(harry.salary)     # instance variable 'salary' gets preferred for harry
# Below class attribute gets preferred for 'rajini' as instance attribute 'salary' is not present for rajini
print(rajni.salary)

# Below line throws an error as address is not present in instance/class
# print(rajni.address)
