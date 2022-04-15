# https://www.sololearn.com/learning/1073/2472/5145/1

'''
So properties could be dynamically created when accessed
So the code is shorter
'''


class Pizza:
    def __init__(self, toppings) -> None:
        self.toppings = toppings
        self.__toppingsHasPineapple = False

    @property
    def toppingsHasPineapple(self):
        return self.__toppingsHasPineapple

    @toppingsHasPineapple.setter
    def toppingsHasPineapple(self, val):
        if input('Enter Password : ') == '2005':
            self.__toppingsHasPineapple = val
        else:
            raise ValueError('Alert! Intruder!')


pizza = Pizza(['cheese', 'tomato'])
print(pizza.toppings)
print(pizza.toppingsHasPineapple)
print()

pizza.toppingsHasPineapple = True
print(pizza.toppingsHasPineapple)
