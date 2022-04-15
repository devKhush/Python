def greet(a, b) -> None:
    print(a)
    print(b)
    print('Hello...')


hi = greet
bye = hi

hi(10, 20)
print()
bye(10, 20)
