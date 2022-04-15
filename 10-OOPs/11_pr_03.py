class MyClass:
    a = "Class Variable"

    def __init__(self) -> None:
        # self.a = 'Instance variable inside constructor'
        pass


obj = MyClass()
print(MyClass.a)
print(obj.a)        # class variable gets preferred
print()

# This creates a Instance varaible
obj.a = 'Instance Variable'  # Instance variable gets preferred
print(MyClass.a)
print(obj.a)


# No class attribute will not change when instance varaible with same name is assigned
