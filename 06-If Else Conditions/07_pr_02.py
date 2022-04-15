sub1 = int(input('Marks in subject 1:'))
sub2 = int(input('Marks in subject 2:'))
sub3 = int(input('Marks in subject 3:'))

total = (sub1+sub2+sub3)/3


if True:
    pass
if sub1 >= 33 and sub2 >= 33 and sub3 >= 33 and total >= 40:
    print('You passed')
    print('Total marks = {marks:.2f}'.format(marks=total))
else:
    print('You Fail')
    print('Total marks = {marks:.2f}'.format(marks=total))
