# https://www.w3schools.com/python/python_ref_string.asp


story = "my name is Khushdev"


def func():
    pass


# String Functions
print(len(story))
print(story.startswith('my '))
print(story.endswith("notes"))
print(story.endswith("dev"))
print()

print(story.count("h"))
print()

print(story.capitalize())
print(story.lower())
print(story.upper())
print()

print(story.find("name"))
print(story.index("name"))
# print(story.index("upon"))
print(story.find("upon"))
print()

print(name := story.replace("Khushdev", "Khushdev Pandit"))
print(name := story.replace("my", "My"))
print(name)
print('Hello, me'.replace('me', 'World!'))
print()


print(l := 'spam, eggs, spam, eggs'.split(', '))
print(str := ', '.join(l))
print(str := '-'.join(l))
print(str := '~~'.join(l))
print(str)
print()

'''
Partition the string into three parts using the given separator.
This will search for the separator in the string, starting at the end. If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.
If the separator is not found, returns a 3-tuple containing two empty strings and the original string.
'''

str_ = 'Hello, how are you?'

tuple_ = str_.rpartition(' ar')
print(tuple_)

tuple_ = str_.rpartition(' a ')
print(tuple_)
