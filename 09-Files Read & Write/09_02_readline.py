f = open('09_01_read_mode.txt')   # by default mode is 'rt'

# read first line
data = f.readline()         # Readline() also reads backslash '\n' also as a character
print(data)                 # that's why extra spaces are there in the output

# Read second line
data = f.readline()
print(data)

# Read third line
data = f.readline()
print(data)

# Read 4th line
data = f.readline()         # How to avoid '\n'? Below trick
print(data[:-1])            # Slicing trick works

# Read 5th line... and so on...
data = f.readline()
print(data[:-1])
f.close()


# The readlines() method, which returns a list containing
# the lines of the file. Also, remember that all lines, except
# the last one, contain a \n at the end, which should not be
# included in the character count.
