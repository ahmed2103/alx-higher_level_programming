class Square:
    """Class Square that defines a square"""

    def __init__(self, size=0):
        """Instantiation with size"""
        self.size = size

    @property
    def size(self):
        """Property to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter to set the size"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size ** 2

    def __eq__(self, other):
        """Equal comparator"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal comparator"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparator"""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal to comparator"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparator"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal to comparator"""
        return self.area() >= other.area()
