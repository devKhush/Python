text = input("Enter the text\n> ")

spams_words = []
spams_words.append('make a lot of money')
spams_words.append('buy now')
spams_words.append('click this')
spams_words.append("subscribe this")

spam = False
for words in spams_words:
    if words in text:
        spam = True
        break

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")
