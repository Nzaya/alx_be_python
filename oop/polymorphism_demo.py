import math

# Base Class - Shape
class Shape:
    def area(self):
        # Raises an error to ensure derived classes override this method
        raise NotImplementedError("Subclasses must override the area() method.")

# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # Override area method to calculate the area of a rectangle
        return self.length * self.width

# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Override area method to calculate the area of a circle
        return math.pi * (self.radius ** 2)
