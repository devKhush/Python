l = [
    "Camera", "Laptop", "Phone", "ipad", "Hard Disk",
    "Nvidia Graphic 3080 card"
]

sentence = "~~".join(l)
print(sentence)

sentence = "==".join(l)
print(sentence)

sentence = " and ".join(l)
print(sentence)

sentence = "\n".join(l)
print(sentence)

print(type(sentence))

print('join using list done\n')

tuple = tuple(l)
print(' '.join(tuple))

set = set(l)
print(set)
print(' '.join(set))
