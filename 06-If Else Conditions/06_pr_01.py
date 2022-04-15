a = 1
b = 200
c = 10
d = 100

if a > b:
    max1 = a
else:
    max1 = b

if c > d:
    max2 = c
else:
    max2 = d

# ternary operator
print('Maimum number is', max1 if max1 > max2 else max2)
