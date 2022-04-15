n = 3

# OP Harry bhai
for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1), end="")
    print(" " * (n-i))


print()
for i in range(1, n+1):
    for k in range(1, n-i+1):
        print(' ', end="")
    for k in range(1, 2*i):
        print('*', end="")
    for k in range(1, n-i+1):
        print(' ', end="")
    print()
