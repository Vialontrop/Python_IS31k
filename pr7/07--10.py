import math

class Point2D:
    def __init__(self):
        self._x = 0
        self._y = 0

    def set_coordinates(self, x, y):
        self._x = x
        self._y = y

    def get_coordinates(self):
        return (self._x, self._y)

    def distance_from_origin(self):
        return math.sqrt(self._x ** 2 + self._y ** 2)

point = Point2D()
point.set_coordinates(3, 4)
print(point.get_coordinates())
print(point.distance_from_origin())
