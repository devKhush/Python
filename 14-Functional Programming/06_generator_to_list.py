
def evenTill(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


for num in evenTill(10):
    print(num)

evenList = list(evenTill(10))
print(evenList)
