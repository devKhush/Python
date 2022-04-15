n = num = 62982
reversedNumber = 0

while n > 0:
    remainder = n % 10
    reversedNumber = reversedNumber*10 + remainder
    n = n//10

print(num)
print(reversedNumber)
