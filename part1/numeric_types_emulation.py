from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector ({self.x}, {self.y})"

    def __abs__(self):
        # Return the Euclidean norm, sqrt(x*x + y*y). This is the length of the vector from the origin to point (x, y).
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, constant):
        return Vector(self.x * constant, self.y * constant)


v1 = Vector(3, 4)
v2 = Vector(2, 5)

v3 = v1 + v2  # __add__
print(v3)  # __repr__

v3 = v1 * 5  # __mul__
print(v3)

v3 = abs(v1)  # __abs__
print(v3)

v3 = bool(v1)  # __bool__
print(v3)
