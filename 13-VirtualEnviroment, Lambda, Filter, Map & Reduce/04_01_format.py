name = "Harry"
channel = "CodeWithHarry"
type = "Coding"

# a = f"This is {name}"
# a = "This is {}".format(name)
# a = "This is {} and his channel is {}".format(name, channel)
a = "This is {} and his {} channel is {}".format(name, channel, type)
print(a)

a = "This is {0} and his {2} channel is {1}".format(name, channel, type)
print(a)

# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
d['def'] = 789
for i in d:
    print("%s  %d" % (i, d[i]))
