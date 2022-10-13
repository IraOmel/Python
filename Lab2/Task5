class Rectangle:

    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def get_attributes(self):
        return self.perimeter(), self.area()

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width
    @length.setter
    def length(self, length):

        if not isinstance(length, float):
            raise TypeError("Incorrect data")
        if length < 0.0 or length > 20.0:
            raise ValueError("Incorrect data")
        self._length = length

    @width.setter
    def width(self, width):
        if not isinstance(width, float):
            raise TypeError("Incorrect data")
        if width < 0.0 or width > 20.0:
            raise ValueError("Incorrect data")
        self._width = width


obj1 = Rectangle(2.4,1.3)
print(obj1.get_attributes())
