#!/usr/bin/python3
"""base module"""
import json
import csv
import turtle


class Base:
    """number of constructor"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initalize
        Args:
            id(int) = id attribute
        """
        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects

        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json str representation"""
        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """json string representation of list_objs to a file"""

        filename = cls.__name__ + ".json"
        with open(filename, "w") as jasonfile:
            if list_objs is None:
                jasonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jasonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """json str to dict"""
        if json_string is None or json_string == "[]":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class initiated with attr alredy set
        Args:
           dictionary = key/value pair attribute to intialize
        """

        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns list of instance"""
        filname = cls.__name__ + '.json'
        new = []

        try:
            with open(filname) as f:
                content = f.read()

        except:
            return new

        json_file = Base.from_json_string(content)
        for obj in json_file:
            new.append(cls.create(**obj))
        return new

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the csv deserialization of an object"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())


    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
