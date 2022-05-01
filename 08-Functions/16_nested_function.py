
def cube1(n):
    answer = n*n

    def cube2(ans, n):
        return ans*n

    return cube2(answer, n)


print(cube1(3))
print(cube1(4))
print(cube1(5))
