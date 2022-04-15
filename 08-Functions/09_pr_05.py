
def pattern(n):
    for i in range(n, 0, -1):
        print('*'*i)


n = 5
for i in range(n):
    print("*" * (n-i))      # Prints * n-i times

print()
pattern(n)
