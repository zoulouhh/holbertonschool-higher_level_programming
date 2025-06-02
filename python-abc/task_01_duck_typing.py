#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math

# Classe abstraite Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calcule et retourne l'aire de la forme"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calcule et retourne le périmètre de la forme"""
        pass

class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Classe concrète Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Fonction shape_info utilisant le duck typing
def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

