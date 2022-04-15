greeting = "Good Morning, "
name = "Khushdev"

# Concatenating two strings
c = greeting + name
print(c)


#       01234567
name = "Khushdev"
#       87654321    All minus
print(name[4])
# print(name[8])    # -> error Index out of range
# name[3] = "d"     # -> Does not work
print()


print(name[1:6])
print(name[:7])  # is same as name[0:7]
print(name[:8])  # is same as name[0:8]
print(name[:9])  # is same as name[0:9]
print(name[:len(name)])  # is same as name[0:len(name)]
print("Copy of name:", name[:])
print(name[1:])  # is same as name[1:len(name)]
print(name[0:-1])
c = name[-4:-1]
print(c)
print()


name = "Khushdev is good"
d = name[0::3]
print(d)
d = name[::-1]
print(d)
d = name[::-1]
print(d)
