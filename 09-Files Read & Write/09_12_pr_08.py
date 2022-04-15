
with open('09_12_pr_08_this.txt') as file:
    content = file.read()

with open('09_12_pr_08_copy.txt', 'w') as file:
    file.write(content)
