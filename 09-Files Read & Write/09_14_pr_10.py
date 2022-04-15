filename = '09_14_pr_10_content.txt'

with open('09_14_pr_10_content.txt') as f:
    print(f'Present content in this file: \n"{f.read()}"')

with open('09_14_pr_10_content.txt', 'w') as f:
    f.write('')
    print('\nContent deleted successfully')
