def number_to_string(agrument):
    match agrument:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
        case _:
            return 'Unknown'

# another approach is Dictionaries


if __name__ == "__main__":
    agrument = 6
    print(number_to_string(agrument))
