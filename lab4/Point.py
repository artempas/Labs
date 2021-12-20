class Point:
    def __init__(self, x:float, y:float):
        if not (type(x) is float or type(x) is int )or not (type(y) is float or type(y) is int):
            raise TypeError(f"x and y should be float or int (not"
                            f" {str(type(x))* ( type(x) is not int and type(x) is not float)} "
                            f"{'and'*(not (type(x) is float or type(x) is int )and not (type(y) is float or type(y) is int))}"
                            f" {str(type(y))* ( type(y) is not int and type(y) is not float)})")
        self.__x = x
        self.__y = y


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is int or type(value) is float:
            self.__x = value
        else:
            raise TypeError(f"Incorrect type {type(value)}")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is int or type(value) is float:
            self.__y = value
        else:
            raise TypeError(f"Incorrect type {type(value)}")

    def __add__(self, other):
        if isinstance(other,Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise NotImplementedError(f"unsupported operand type for +: 'Point' and '{type(other)}'")


    def __repr__(self):
        return f"Point obj {self.__x=} , {self.__y=}"

    def __str__(self):
        return str((self.x, self.y))
