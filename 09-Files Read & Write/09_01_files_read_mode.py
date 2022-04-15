# Use open function to read the content of a file!
# If a such a file is not present, gives error in read mode

# https://www.sololearn.com/learning/1073/2446/5053/1

# by default the mode is 'r' & not even 'r', it is 'rt' (read in text mode)
# f = open('sample.txt', 'r')
# f = open('read_mode.txt', 'rt')
f = open('09_01_read_mode.txt')

print('***********************************Full read Start***********************************')
data = f.read()     # f.read() returns data in string format
print(data)
print('***********************************Full read Done***********************************\n\n')

# Data is only read only once (one time f.read() only) from the file,
# for multiple reads use open() again
# But f.read(int) can be done many times, after each call of f.read(int)
# it returns next remaining number of characters specified

f = open('09_01_read_mode.txt')

# f.read(10) returns first 10 charcters of data in string format
data = f.read(10)
print(data)
print("...\n")

# f.read(10) returns next 15 charcters of data in string format
data = f.read(15)
print(data)
print("...\n")

# f.read() returns whatever left remaining charcters of data in string format
data = f.read()     # f.read() returns data in string format
print(data)
print()

print(type(f))
print(type(data))
f.close()
