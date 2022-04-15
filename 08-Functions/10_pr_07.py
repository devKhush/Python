def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()


this = "     Harry is a good      "
n = remove_and_split(this, "Harry")
print(n)
print(this)
print(this.strip())
print()


# My experience:
# Adding data types next to the parameters inside function is a good practise
# & allows us to use their suggested methods in VS code or Intellij

def my_remove_from_string(inp_str: str, word: str):
    return inp_str.replace(word, '').strip()


string = "        Hello Khushdev is a coder    "
print(string.strip())       # trim() in java
print(my_remove_from_string(string, 'Hello'))

print()
print(string.split())
print(string.split(' '))
string = "Khushdev-is-a-coder"
print(string.split('-'))
