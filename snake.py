from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    """ Snake character class"""

    def __init__(self):
        """ Snake class basic body list """
        self.segments = list()
        self.create_snake()

    def create_snake(self):
        """ Looping through the starting 3 pieces of the snake character """

        for position in STARTING_POSITION:
            new_segment = Turtle(shape='square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        """ Move the snake """
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)
