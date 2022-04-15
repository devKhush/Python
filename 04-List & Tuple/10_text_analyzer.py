def countCharacter(text: str, char: str):
    count = 0
    for ch in text:
        if ch == char:
            count += 1
    return text.count(char) if text.count(char) == count else -1


total_percentage = 0
myText = "sjdrgfskeuralieralkwirgfserukghskrrgkeruitgabsczdbdfaliergakfvafawkefakevaksdfacd"

for x in set(myText):
    percentage = countCharacter(myText, x)*100/len(myText)
    print("Percentage of '{ch}' is {percentage:.2f}".format(
        ch=x, percentage=percentage))
    total_percentage += percentage

print('Total percentage = ', total_percentage)
