# Solution to problem 1

file = open('09_05_pr_01_poems.txt')
text = file.read()

print(text)
print()

# Two ways to print via Ternary operator, Remember u can always use if-else statements
print("'twinkle' is present" if 'twinkle' in text else "'twinkle' is not present")

print("'twinkle' is present") if 'twinkle' in text else print(
    "'twinkle' is not present")

file.close()

print()
print('*'*100)
for x in open('09_05_pr_01_poems.txt'):
    print(x)
