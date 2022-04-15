with open('09_08_pr_04_donkey_file.txt', 'r+') as readFile:
    text = readFile.read()
    text = text.replace('Donkey', '#')
    readFile.write('')
    readFile.write(text)

# with open('09_08_pr_04_donkey_file.txt', 'w') as writeFile:
#     writeFile.write(text)

'''
You can use the + sign with each of the modes above to give 
them extra access to files. For example, r+ opens the file 
\for both reading and writing.'''
