import math

class Location(object):
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.pos = (self.x, self.y, self.z)

    def distance(self, ot_location) -> float:
        x_squared = (self.x - ot_location.x) * (self.x - ot_location.x)
        y_squared = (self.y - ot_location.y) * (self.y - ot_location.y)
        z_squared = (self.z - ot_location.z) * (self.z - ot_location.z)
        dist = math.sqrt(x_squared + y_squared + z_squared)
        return dist


class Node(object):

    def __init__(self, key: int, pos: tuple) -> None:
        self.key = key
        self.pos = pos
        self.parent_weight = dict()
        self.child_weight = dict()

    def __str__(self):
        return "{}: |edges out| {} |edges in| {}".format(self.key, self.child_weight.__len__(),
                                                         self.parent_weight.__len__())

    def __repr__(self):
        return self.__str__()

if __name__ == '__main__':
    nd = Node(0, None)
    nd1 = Node(1, None)
    nd2 = Node(2, None)
    nd3 = Node(3, None)
    nd4 = Node(4, None)
    nd5 = Node(5, None)
    nd6 = Node(6, None)
    print(nd)
    print(nd1)
