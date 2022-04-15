# The assert can take a second argument that is passed to the
# AssertionError raised if the assertion fails.

# AssertionError can also be handled

age = 10

try:
    assert age > 18, 'Age should be grater than zero'
except AssertionError:
    print('Assertion error thrown')
except:
    print('Some other error thrown')
else:
    print('Assertion not error thrown')
finally:
    print('Done 1')
print()


try:
    assert age > 18, 'Age should be grater than zero'
finally:
    print('Done 2')
