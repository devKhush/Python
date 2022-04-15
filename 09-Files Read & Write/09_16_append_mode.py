# writing into the file via append mode
f = open('09_16_append_mode.txt', 'a')


# Difference b/w write mode & append mode:
# Append mode simply append the contents to be written to the end each time file is runned
# & append mode doesn't care about contents previously present in the file
# While write mode clear the whole file (i.e, overwrites the content of file) & then write/append into it

# Try append multiples times (run this file multiple times & 09_03_write_mode.py multiple times)
# append also can be done multiple times
f.write('My name is Khushdev. ')
f.write("I am writing. ")
f.write("I am writing again. \n")
f.write("I am a good boy." + "\n")
f.write("Bye" + "\n")
f.write("")

f.close()

'''
# This ensures that the file is always closed, even if an error occurs.

try:
   f = open("filename.txt")
   print(f.read())
finally:
   f.close()
   

   '''
