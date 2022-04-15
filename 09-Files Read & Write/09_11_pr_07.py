content = True
i = 1
with open("09_10_pr_06_log.txt") as f:
    while content:
        content = f.readline()      # content is true if, it is present in file
        if 'python' in content.lower():
            print(content[:-1])
            print(f"Yes python is present on line number {i}\n")
        i += 1

print()
print()

# Another approach via readlines() which gives all lines in the file
with open('09_10_pr_06_log.txt') as file:
    list_of_lines = file.readlines()

    for i in range(len(list_of_lines)):
        if 'python' in list_of_lines[i].lower():
            print(list_of_lines[i][:-1])
            print("'Python' present in line number", (i+1))
            print()
