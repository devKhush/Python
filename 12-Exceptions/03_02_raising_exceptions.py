'''

Different exceptions are raised for different reasons.
Common exceptions:
ImportError: an import fails;
IndexError: a list is indexed with an out-of-range number;
NameError: an unknown variable is used;
SyntaxError: the code can't be parsed properly;
TypeError: a function is called on a value of an inappropriate type;
ValueError: a function is called on a value of the correct type, but with an inappropriate value.'''

a = 1
print('Hello')

# In except blocks, the raise statement can be used without arguments to re-raise whatever exception occurred.

try:
    num = 5/0
except:
    print('An error occured')
    raise       # re-throw the thrown exception

raise MemoryError               # Both works
raise MemoryError()               # Both works

raise SyntaxError('Lol!')
raise ValueError("Eg, converting '23rf' to int")
raise TypeError("Eg,  '23rf' + 13")
raise ArithmeticError('Use Description')
raise AttributeError('Use Description')
raise IndentationError('Indentation problem')
raise IndexError('Index out of bound')
raise MemoryError('Memory Exhausted')
raise Exception('Use Description')
raise FileNotFoundError('For unknoen files')
raise Name('For undefined variables')
#  and so on

print('Hi')
