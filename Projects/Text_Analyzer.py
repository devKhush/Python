def countCharacter(text: str, char: str):
    return text.count(char)


with open('text.txt') as file:
    data = file.read().lower()

length = len(data)
total = 0

# Ignoring the case of data (A, a) as same

for i in "abcdefghijklmnopqrstuvwxyz~!@#$%^&*()_+`1234567890-.,'= \n":
    percentage = countCharacter(data, i)*100/length
    print("Percentage of '{char}' is : {p:.3f} ".format(char=i, p=percentage))
    total += percentage

print('\nTotal Percentage = ', total)
print(set(data))
