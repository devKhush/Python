import os

oldname = "renamed_by_python_pr_11.txt"
newname = "renamed_by_python.txt"

with open(oldname) as f:
    content = f.read()

with open(newname, "w") as f:
    f.write(content)

os.remove(oldname)
print('File removed')
