name = input('Name : ')
marks = float(input('Marks (CGPA) : '))
phn_num = int(input('Phone number : '))

template = "The name of the student is {name}, his marks are {cgpa:.2f} and phone number is {phn} \n"

UserInfo = template.format(name=name, cgpa=marks, phn=phn_num)

print()
print(UserInfo)