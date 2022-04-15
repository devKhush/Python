class Sample:
    def __init__(slf, name):        # Yes we can do that, but never do this!!!
        slf.name = name


obj = Sample("Harry")
print(obj.name)
