# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# https://www.w3schools.com/python/python_ref_dictionary.asp
# https://www.sololearn.com/learning/1073/2450/5068/1
# https://www.sololearn.com/learning/1073/2451/5071/1

myDict = {
    "fast": "In a Quick Manner",
    "harry": "A Coder",
    "marks": [1, 2, 5],
    "anotherdict": {'harry': 'Player'},
    'hola': 'ka Gola',
    1: 2
}

myDict.setdefault('Hello')      # adds a key with value 'None'
print(myDict)

# remove specified key and return the corresponding value
value = myDict.pop('Hello')
print(value)

# delete key & value with given given key
del myDict['hola']


# Dictionary Methods
print('\nKeys:')
print(myDict.keys())            # Prints the keys of the dictionary
print(list(myDict.keys()))      # Prints the keys of the dictionary
print()

print('\nValues:')
print(myDict.values())          # Prints the values of the dictionary
print(list(myDict.values()))    # Prints the values of the dictionary
print()

# Prints the (key, value) for all contents of the dictionary
print('\nDict values: ')
print(myDict.items())
print(list(myDict.items()))
print()


updateDict = {
    "Lovish": "Friend",
    "Divya": "Friend",
    "Shubham": "Friend",
    "harry": "A Dancer"
}

# Updates the dictionary by adding key-value pairs from 'updateDict'
myDict.update(updateDict)
print('\nUpadted Dictionary:')
print(myDict)
print()


print(myDict.get("harry"))   # Prints value associated with key "harry"
print(myDict["harry"])       # Prints value associated with key "harry"


# The difference between .get and [] sytax in Dictionaries?
# Returns None as 'lmao' is not present in the dictionary
print(myDict.get("lmao", 'lmao not found'))
print()

# throws an error as 'lmao' is not present in the dictionary
# print(myDict["lmao"])

# remove the last item in dictionary    
itemPop = myDict.popitem()
print(itemPop)
print(myDict)

print('\nCleared dict:')
myDict.clear()
print(myDict)
