from lab4.Point import Point
from math import atan


class Complex(Point):

    @property
    def angle(self):
        return atan(self.y/self.x)

    def __str__(self):
        return f"{self.x}+{self.y}i"

    def __repr__(self):
        return f"Complex "+self.__str__()
