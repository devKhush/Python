file1 = '09_12_pr_08_this.txt'
# file1 = '09_01_read_mode.txt'
file2 = '09_12_pr_08_copy.txt'

with open(file1) as file:
    content1 = file.read()

with open(file2) as file:
    content2 = file.read()

print(
    f'\nContent of "09_12_pr_08_copy.txt" & "09_12_pr_08_this.txt" matches ? {content1==content2}\n')
