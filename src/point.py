from math import sqrt


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class EndPoint(Point):
    def __init__(self, x, y, id, contact_point):
        super(EndPoint, self).__init__(x, y)
        self.id = id
        self.contact_point = contact_point


