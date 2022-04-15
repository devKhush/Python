# n! = 1 * 2 * 3 * 4...*(n-1)*n
# n! = n * (n-1)!

def factorial_iterative(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product


def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n-1)


f = factorial_iterative(5)
print(f)
f = factorial_recursive(5)
print(f)
