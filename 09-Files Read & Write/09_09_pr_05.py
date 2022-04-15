
list = ['Donkey', 'ola', 'gola', 'seen']

with open('09_09_pr_05_file.txt') as readFile:
    text = readFile.read()


with open('09_09_pr_05_file.txt', 'w') as writeFile:
    for word in list:
        text = text.replace(word, 'XXX')

    writeFile.write(text)
