#!/usr/bin/python3
"""
Custom object serialization and deserialization using pickle.
"""

import pickle


class CustomObject:
    """
    A custom Python class that supports serialization and deserialization
    using the pickle module.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize the CustomObject instance.

        Args:
            name (str): The name of the object.
            age (int): The age value.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print the attributes of the object.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object and save it to a file using pickle.

        Args:
            filename (str): Path to the file to save the object.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a pickled object from a file.

        Args:
            filename (str): Path to the file containing the pickled object.

        Returns:
            CustomObject: The deserialized object, or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except Exception:
            return None
