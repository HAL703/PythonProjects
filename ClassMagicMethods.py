"""CONSTRUCTOR"""
class Point:
    default_color = "red"
    #above is a class attribute
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #instance attributes would go here, and belong only to instances
    def draw(self):
        print("draw")
        #instead can do the following
        print(f"Point ({self.x}, {self.y})")

Point.default_color = "yellow"


point = Point(1,2)
print(point.x) #is rendered useless by the following
#with the following, can do this
point.draw()




"""COMPARATIVES"""

class PointAgain:
    def __init(self,x,y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __gt__(self, other):
        return self.x > other.x and self.y > other.x

"""ARITHMATIC OPERATORS"""
GOTO https://rszalski.github.io/magicmethods/


