letter = '''Dear {NAME},
Greetings from Amazon. I am happy to tell you about your selection
Package -> 20+ LPA
You are selected!
Have a great day ahead!

Thanks and regards,
Bill Gates
Date: {DATE}
'''

name = input("\nEnter Your Name\n> ")
date = input("Enter Date\n> ")
# returns a copy of the function acted on letter variable
letter = letter.replace("{NAME}", name)
letter = letter.replace("{DATE}", date)

print("\n" + letter)
