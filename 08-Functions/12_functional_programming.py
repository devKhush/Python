# https://www.sololearn.com/learning/1073/2459/5097/1
# https://en.wikipedia.org/wiki/Pure_functions

'''If the answer to all questions is "yes", your function is pure. 
1. Does my function depend only on its arguments and nothing else? OR Does my function always return 
   the same result given the same arguments? 
2. Can I run my function anywhere in the script without causing any trouble or side effects whatsoever? 
3. Can I run my function with the same arguments many times and still return the same result each time? 
4. Is it true that my function does not change anything outside it, but only returns something? 
5. Can my function be used by other functions or scripts with equal success?'''


# Pure function:
def pure_function(x, y):
    temp = x + 2*y
    return temp / (2*x + y)


# Impure function:

some_list = []


def impure(arg):
    some_list.append(arg)
