# *********************************************** Demo 1 ***********************************************
print('='*30, 'Demo 1', '='*30)

i = 0

while i < 10:
    print("Hi " + str(i+1))
    i += 1

while i >= 100:
    print("Will not execute " + str(i))
    i -= 1

print()

# *********************************************** Demo 2 ***********************************************

print('='*30, 'Demo 2', '='*30)

x = [1, 2.3, 'dev']
length = 0
try:
    while x[length]:
        length += 1
except Exception as e:
    print('Error Description: ', e)

print('Length of list: ', length)

print('\nDone')
