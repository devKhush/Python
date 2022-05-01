import os


def currentWorkingDirectory():
    cwd = os.getcwd()
    print(cwd)


def filePath(fileName) -> None:
    path = os.path.abspath(fileName)
    print(path)

    path = os.path.relpath(fileName)
    print(path)


currentWorkingDirectory()

file = "text.txt"
filePath(file)
print()

print(os.listdir())
