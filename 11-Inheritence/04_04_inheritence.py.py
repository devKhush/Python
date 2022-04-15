class GameObject:
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name + " is " + self.desc


class Goblin(GameObject):
    class_name = "goblin"
    desc = "a foul creature"


goblin = Goblin("Gobbly")
print(goblin.class_name)
print(goblin.desc)
print(goblin.get_desc())
print()

print(GameObject.objects)
print(Goblin.objects)
print(goblin.objects)
