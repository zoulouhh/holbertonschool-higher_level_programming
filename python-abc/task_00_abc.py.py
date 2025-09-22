#!/usr/bin/env python3
"""
This module defines an abstract class `Animal` and its subclasses.

The `Animal` class uses the abc module to define an abstract method `sound`
that must be implemented by all subclasses.
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
        Abstract method that must be implemented by all animal subclasses.
        Should return the sound made by the animal.
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
