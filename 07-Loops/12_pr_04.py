import math as m
from tkinter import N

num = int(input("Enter the number: "))
prime = True

for i in range(2, int(m.sqrt(num))+1):      # stop as num//2 also works
    if(num % i == 0):
        prime = False
        print("This number is not Prime")
        break
else:
    print("This number is Prime")
