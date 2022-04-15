
with open('09_10_pr_06_log.txt') as file:
    text = file.read()

# print(text)

print('Yes, file contains word \'Python\'' if 'python' in text.lower()
      else 'No, file doesn\'t contains word \'Python\'')
