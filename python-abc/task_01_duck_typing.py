#!/usr/bin/env python3
"""
This module defines an abstract base class `Shape`
for geometric shapes, enforcing area and perimeter methods.
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Abstract base class for geometric shapes.
    """

    @abstractmethod
    def area(self):
        """
        Return the area of the shape.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Return the perimeter of the shape.
        Must be implemented by subclasses.
        """
        pass

class Rectangle(Shape):
    """
    Concrete class representing a rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize the rectangle with width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Return the area of the rectangle.
        Formula: width * height
        """
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.
        Formula: 2 * (width + height)
        """
        return 2 * (self.width + self.height)
        
