def percentage(marks) -> float:

    percent = sum(marks) * 100 / (len(marks)*100)
    # marks1 = [1, 2]
    marks1[0] = 100
    # marks2[0] = 90
    return percent
    print('This will never execute')

# error -> bcoz python is interpreted language
# gives error when func is called on marks1 as marks2 isn't defined yet


marks1 = [45, 78, 86, 77]
percentage1 = percentage(marks1)

marks2 = [98, 85, 87.5, 89, 95]
percentage2 = percentage(marks2)


print(marks1)
print(marks2)
print('Percentage 1:', percentage1)
print('Percentage 2:', percentage2)
