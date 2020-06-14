class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def weight(self):
        return self._length * self._width


class W(Road):
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume


r = W(25, 10000, 125)
print(r.weight())