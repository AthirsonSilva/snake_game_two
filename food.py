from random import randint
from turtle import Turtle


class Food(Turtle):
    """ Food that appear and can be eaten class """

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('red')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed('fastest')
        random_x, random_y = randint(-200, 200), randint(-200, 200)
        self.goto(random_x, random_y)

    def refresh(self):
        """ Refresh the food location """
        random_x, random_y = randint(-200, 200), randint(-200, 200)
        self.goto(random_x, random_y)
