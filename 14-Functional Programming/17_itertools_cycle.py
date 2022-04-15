from itertools import repeat, cycle

# https://www.sololearn.com/learning/1073/2466/5116/1

list_ = [1, 2, 3, 4, 5]

obj = cycle(list_)
print(obj)

j = 0
for i in cycle(list_):
    print(i)

    j += 1
    if j == 24:
        break
print()


string = "Hello!"
j = 0
for i in (cycleObject := cycle(string)):
    print(i)

    j += 1
    if j == 13*len(string):
        break

print("\n", cycleObject)
