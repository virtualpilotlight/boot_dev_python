class Rectangle:
    def __init__(self, length: int, width: int) -> None:
        self.__length = length
        self.__width = width

    def get_area(self) -> int:
        area = self.__length * self.__width
        return area

    def get_perimeter(self) -> int:
        perim = 2 * (self.__length + self.__width)
        return perim


class Square(Rectangle):
    def __init__(self, length: int) -> None:
        width = length
        super().__init__(length, width)

