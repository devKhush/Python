# https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/

#  Generator-Function
def simpleGeneratorFunction(n: int) -> int:
    for i in range(n):
        yield i*i

    yield 10
    yield 20
    yield 30


for value in simpleGeneratorFunction(6):
    print(value)
