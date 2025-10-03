#!/usr/bin/python3
"""
Defines a class Student.
"""


class Student:
    """
    Class that defines a student by first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiation of Student.
        Args:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.
        Returns:
            dict: dictionary representation of the instance
        """
        return self.__dict__
