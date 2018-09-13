class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.length = width_WE
        self.width = width_NS
        self.height = height
        self.north = self.south + self.width
        self.east = self.west + self.length

    def corners(self):
        s = self.south
        n = self.north
        w = self.west
        e = self.east
        return {'north-east': [n, e], 'south-east': [s, e],
                'south-west': [s, w], 'north-west': [n, w]}

    def area(self):
        return self.length * self.width  # S = a*b

    def volume(self):
        return self.area() * self.height  # V = a*b*c

    def __repr__(self):
        return f"Building({self.south}, {self.west}, {self.length}, {self.width}, {self.height})"


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())


    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"
