#!/usr/bin/python3
"""
    `Base` class Module
"""

import csv
import json


class Base:
    """
        Defines Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initialization attributes for Base class
            Args:
                id: public instance attribute
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Returns JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Writes the JSON string representation of list_objs into file
        """
        obj_arr = []
        if list_objs is not None:
            for obj in list_objs:
                obj_arr.append(cls.to_dictionary(obj))
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(obj_arr))

    @staticmethod
    def from_json_string(json_string):
        """
            Returns the list of the JSON string representation json_string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            Returns an instance with attributes already set
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
            Returns a list of instances
        """
        filename = cls.__name__ + ".json"
        obj_arr = []
        try:
            with open(filename, "r") as f:
                instances = cls.from_json_string(f.read())
            for i, instance in enumerate(instances):
                obj_arr.append(cls.create(**instances[i]))
        except FileNotFoundError:
            pass
        return obj_arr

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for ob in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([ob.id, ob.width, ob.height, ob.x, ob.y])
                if cls.__name__ == "Square":
                    writer.writerow([ob.id, ob.size, ob.x, ob.y])

    @classmethod
    def load_from_file_csv(cls):
        obj_arr = []
        filename = cls.__name__ + ".csv"
        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    dic = {"id": int(row[0]),
                           "width": int(row[1]),
                           "height": int(row[2]),
                           "x": int(row[3]),
                           "y": int(row[4])}
                if cls.__name__ == "Square":
                    dic = {"id": int(row[0]),
                           "size": int(row[1]),
                           "x": int(row[2]),
                           "y": int(row[3])}
                obj = cls.create(**dic)
                obj_arr.append(obj)
        return obj_arr
