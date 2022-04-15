# n! = (n-1)! * n
# sum(n) = sum(n-1) + n

def my_sum(n):
    if n == 0:
        return 0
    return n + my_sum(n-1)


print(my_sum(100))
