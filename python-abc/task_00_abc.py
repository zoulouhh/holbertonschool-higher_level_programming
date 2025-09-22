#!/usr/bin/env python3
"""
This module defines an abstract base class Animal,
and two concrete subclasses: Dog and Cat.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract base class for animals.

    Subclasses must implement the sound() method.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to return the sound an animal makes.
        Must be implemented by subclasses.
        """
        pass


class Dog(Animal):
    """Concrete class representing a dog."""

    def sound(self):
        """Return the sound made by a dog."""
        return "Bark"


class Cat(Animal):
    """Concrete class representing a cat."""

    def sound(self):
        """Return the sound made by a cat."""
        return "Meow"
