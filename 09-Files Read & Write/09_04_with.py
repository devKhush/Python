# Use of Indentation in 'with' statement:
# File object which is opened, is usable within that indented (scope present) block
# outside that scope/indented block file object can't be used (gives error)
# as it is automatically closed after indentaion or its scope gets over
# file.close() is automatically called

# This creates a temporary variable (often called f),
# which is only accessible in the indented block of the with statement.

with open('09_04_with.txt', 'r') as f:      # also called as 'Context manager'
    data = f.read()
print(data)
# f.read()          # -> error as f is not visible/accessible outside scope

with open('09_04_with.txt', 'w') as f:
    b = f.write("Writing into the file...\n")
    f.write("Writing into the file...\n")
    f.write("Writing into the file...\n")
    print('Hi')
print(b)

with open('09_04_with.txt', 'a') as f:
    b = f.write("Appending into the file...\n")
print(b)

with open('09_04_with.txt', 'r') as f:
    c = f.read()
print(c)

# The file is automatically closed at the end of the 'with' statement,
# even if exceptions occur within it.
