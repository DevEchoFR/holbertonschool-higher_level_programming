#!/usr/bin/python3
"""9-rectangle.py"""


class Rectangle:
    """Defines a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width with validation."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height with validation."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area."""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return the printable rectangle using print_symbol."""
        if self.width == 0 or self.height == 0:
            return ""
        sym = str(self.print_symbol)
        return "\n".join(sym * self.width for _ in range(self.height))

    def __repr__(self):
        """Return a string to recreate the instance with eval()."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Handle deletion of an instance."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on area (or rect_1 if equal)."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance where width == height == size."""
        return cls(size, size)
