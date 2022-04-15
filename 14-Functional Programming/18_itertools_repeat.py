import itertools

# https://www.sololearn.com/learning/1073/2466/5116/1

# Python code to demonstrate the working of
# repeat()

string = 'Hello!'
repeated = list(itertools.repeat(string, 5))
print(repeated)


# using repeat() to repeatedly print string
print(list(map(str.upper, itertools.repeat('khushdev', 3))))

print(list(itertools.repeat(25, 5)))
