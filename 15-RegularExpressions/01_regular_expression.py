# https://www.sololearn.com/learning/1073/2475/5155/1

import re

pattern = r'spam'

if matchObj := re.match(pattern, 'spam is Spam'):
    print('Match')
else:
    print('No match')

print(matchObj)
