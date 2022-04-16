# https://www.sololearn.com/learning/1073/2467/5125/1

# Class is a blueprint for similar objects
# Methods are function ties/ called form an object
# Every instance in python (int, float, string, list, etc) is an object

class Number:
    def sum(self):
        return self.a + self.b


sumObject1 = Number()
sumObject1.a = 10
sumObject1.b = 20

s = sumObject1.sum()
print(sumObject1.a)
print(sumObject1.b)
print(s)
print()


# Some object of same classes in python may have attributes that
# other objects (of same class) doesn't have (Eg here below)
# Such attributes need to be defines externally in the program (not inside the Class)
# But this work may become tedious for every instance for that class (use constructors)
sumObject2 = Number()
# print(sumObject2.a)       # error
# print(sumObject2.b)       # error


'''
PascalCase 
EmployeeName -->PascalCase 

camelCase
isNumeric, isFloatOrInt -->camelCase
'''
