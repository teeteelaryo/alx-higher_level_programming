#!/usr/bin/python3
"""Square related feature module."""


class Square:
    """Class that define a Square."""

    def __init__(self, size=0):
        """
            Args:
                size (int): size initializer
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Compute the area of the Square.

            Returns:
                The area. An (integer)
        """

        return (self.__size ** 2)

    @property
    def size(self):
        """__size property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """__size property setter.

            Args:
                value (int): new size value

            Raises:
                TypeError: if `value` is not an integer
                ValueError: if `value` is < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def __operr_msg(self, oper, instance):
        msg = "'{:s}' not supported between instances of '{:s}' and '{:s}'"
        return msg.format(oper, type(self).__name__, type(instance).__name__)

    def __eq__(self, instance):
        """square1 == square2"""
        if instance is not None and type(instance) is not Square:
            raise TypeError(self.__operr_msg('==', instance))
        return instance is not None and self.area() == instance.area()

    def __ne__(self, instance):
        """square1 != square2"""
        if instance is not None and type(instance) is not Square:
            raise TypeError(self.__operr_msg('!=', instance))
        return instance is not None and self.area() != instance.area()

    def __gt__(self, instance):
        """square1 > square2"""
        if type(instance) is not Square:
            raise TypeError(self.__operr_msg('>', instance))
        return self.area() > instance.area()

    def __ge__(self, instance):
        """square1 >= square2"""
        if type(instance) is not Square:
            raise TypeError(self.__operr_msg('>=', instance))
        return self.area() >= instance.area()

    def __lt__(self, instance):
        """square1 < square2"""
        if type(instance) is not Square:
            raise TypeError(self.__operr_msg('<', instance))
        return self.area() <= instance.area()

    def __le__(self, instance):
        """square1 <= square2"""
        if type(instance) is not Square:
            raise TypeError(self.__operr_msg('<=', instance))
        return self.area() <= instance.area()
