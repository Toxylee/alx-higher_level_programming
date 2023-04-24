#!/usr/bin/python3

"""
Module contains a class that defines a student with their details.
"""


class Student:
    """Class defines a student
    Attributes:
        first_name: The first name of the student
        last_name: The last name of the student
        age: The student's age
        __init__(self, first_name, last_name, age)
        to_json(self, attrs=None)
        reload_from_json(self, json)
    """

    def __init__(self, first_name, last_name, age):
        """Initializes the class instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student
        Return: a dictionary conatining instance details
        """
        dict_2 = {}
        if isinstance(attrs, list):
            for i in attrs:
                if i in self.__dict__:
                    dict_2[i] = self.__dict__[i]
            return dict_2
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the student instance"""
        for i, j in json.items():
            setattr(self, i, j)
