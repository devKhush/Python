# writing into the file
f = open('09_03_write_mode.txt', 'w')
# If a such a file is not present, automatically creates one with same name


# Difference b/w write mode & append mode:
# Append mode simply append the contents to be written, to the end each time file is runned
# & append mode doesn't care about contents previously present in the file
# While write mode clear the whole file (i.e, overwrites the content of file) & then write/append into it


# write can be done multiple times
#  write() functions returns length of string written into file
f.write('My name is Khushdev. ')
print(f.write("I am writing. "))
f.write("I am writing again. \n")
f.write("I am a good boy." + "\n")
print(f.write("Bye" + "\n"))
f.write(" ")

f.writelines(['I ', 'am ', 'a ', 'good ', 'boy\n'])
f.write("I am a legend." + "\n")

f.close()
