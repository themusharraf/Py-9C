from uuid import uuid4


class Author:
    def __init__(self, name, age, gender, password, id=None):
        self.id = uuid4()
        self.name = name
        self.__age = age
        self.gender = gender
        self.__password = password


object = Author("Musharraf", 23, "Male", "Alls90")

num = list(range(0, 31, 2))

print(num)
