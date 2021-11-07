import Point
class Point3D(Point.Point):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        if type(z) is not int and type(z) is not float:
            raise TypeError(f"z should be int or float (not {type(z)})")
        self.__z=z

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self,value):
        if type(value) is int or type(value) is float:
            self.__z = value
        else:
            raise TypeError(f"Incorrect type {type(value)}")

    def __add__(self, other):
        if isinstance(other,Point3D):
            return Point3D(self.x+other.x,self.y+other.y,self.z+other.z)
        else:
            raise NotImplementedError(f"Operation '+' is not implemented for type 'Point3D' and '{type(other)}'")

    def __str__(self):
        return str((self.x,self.y,self.__z))