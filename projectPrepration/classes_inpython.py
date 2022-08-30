'''
    --- class are extreamly importeant in rogaraming that not sepcific to pyhotn
    --- In this class we define new type. In this new type we create new objects.
    --- objects is an instance of a class. A class simply defines a blue print or a templet for
        creating objects and objects are actival instance of the blue print
'''


class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point();
point1.x = 10
print(point1.x)
print(point1.y)
print(point1.move())