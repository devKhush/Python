dict1 = {}
dict2 = dict()
print(dict1)
print(dict2)
print()

myDict = {
    "Fast": "Quick",
    "Dev": "A Coder",
    "Marks": [1, 2, 5],
    "anotherdict": {'harry': 'Player'},
    10: 20
}

anyDict = {(1, 2, 3): 'key'}

# Only immuttable keys are allowed like str, int, bool, tuple, etc,
# (list, dict as keys not allowed) as they are not hashble
# Coz key can be changed

print(myDict['Fast'])
print(myDict['Dev'])
print()
# print(myDict['Harry'])        # -> error

myDict['Marks'] = [10, 20]
myDict['CGPA'] = [8.4, 8.4, 9.4]
print(myDict)
print()

print(myDict['Marks'])
print(myDict['anotherdict']['harry'])
print()

myDict['anotherdict'] = {'a': 1, 'b': 2}
print(myDict)
