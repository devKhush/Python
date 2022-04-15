def readFile(fileName: str) -> None:
    try:
        with open(file=fileName) as file:
            print(f"Content of {fileName} : \"" + file.read() + '"')
    except FileNotFoundError as e:
        print('ERROR:')
        print(f'\'{fileName}\' not found in directory!')
    except Exception as e:          # can also use just 'except:'
        print('Some other Error ocurred')
        print(e)
    else:
        print(f'{fileName} sucessfully found in directory!')
    finally:
        print(f'{fileName} Question done')


# This will throw error if except clause is commented

readFile('1.txt')
print()
readFile('2.txt')
print()
readFile('3.txt')
