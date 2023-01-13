#!/usr/bin/python3

""" base module """
import json
import os
import csv


class Base:
    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):

        content = []
        if list_objs is not None and len(list_objs) != 0:
            for obj in list_objs:
                content.append(obj.to_dictionary())

        content = cls.to_json_string(content)
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.seek(0)
            f.write(content)
            f.truncate()

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Square":
            dummy = cls(size=1)
        else:
            dummy = cls(width=1, height=1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        f_name = "{}.json".format(cls.__name__)

        if not os.access(f_name, os.F_OK):
            return []

        instances = []
        with open(f_name, "r", encoding="utf-8") as f:
            j_data = f.read()
            j_data = cls.from_json_string(j_data)
            for d in j_data:
                instances.append(cls.create(**d))

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save_to_file_csv function """

        if list_objs is not None and len(list_objs) != 0:
            if cls.__name__ == "Rectangle":
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            else:
                fieldnames = ['id', 'size', 'x', 'y']

        content = []
        if list_objs is not None and len(list_objs) != 0:
            for obj in list_objs:
                content.append(obj.to_dictionary())

        with open("{}.csv".format(cls.__name__), 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for data in content:
                writer.writerow(data)

    @classmethod
    def load_from_file_csv(cls):
        """ load_from_file_csv """

        f_name = "{}.csv".format(cls.__name__)

        if not os.access(f_name, os.F_OK):
            return []

        instances = []
        with open(f_name, "r") as f:
            csv_data = csv.DictReader(f)
            for d in csv_data:
                for k in d:
                    d[k] = int(d[k])
                instances.append(cls.create(**d))

        return instances
