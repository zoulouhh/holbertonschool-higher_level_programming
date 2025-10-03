#!/usr/bin/python3
"""
Defines a class Student (based on 9-student.py).
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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only those attributes are retrieved.
        Otherwise, all attributes are retrieved.
        Args:
            attrs (list, optional): list of attribute names to retrieve
        Returns:
            dict: dictionary representation of the instance
        """
        if isinstance(attrs, list) and all(isinstance(el, str) for el in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__
