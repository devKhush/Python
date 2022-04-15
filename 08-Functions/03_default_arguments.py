def greet(name="Stranger"):
    print("Good Day, " + name)


def sum(a, b, c=5, d=10):       # Always Default argument follows non-default argument
    return a+b+c+d


greet("Harry")
greet()
print()

print(sum(1, 2, 3))
print(sum(10, 20))
print(sum(10, 20, c=100))
print(sum(10, 20, d=200))
