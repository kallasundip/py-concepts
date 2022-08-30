'''
    --- A constructor is a function that gets called at the time of creating an object
    --- we call point object with out object it throws an error noattributes called x
                // print(point.x)
'''


class Point:
    # constrector
    def __init__(self, x, y):   # init means initilazation shot cut
        self.x = x              # wehen we create a new object in memory self references  that object in memeory
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20);
print(point.x)
print(point.y)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi Iam {self.name}")


john = Person("John Smith")
bob = Person("Bob Smith")
john.talk()
bob.talk()
