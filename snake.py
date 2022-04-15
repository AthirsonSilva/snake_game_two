from turtle import Turtle

# Direction and moving
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """ Snake character class"""

    def __init__(self):
        """ Snake class basic body list """
        self.segments = list()
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        """ Looping through the starting 3 pieces of the snake character """

        for position in STARTING_POSITION:
            new_segment = Turtle(shape='square')
            new_segment.color('green')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        """ Move the snake """
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)

        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        """ Move the snake up """
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        """ Move the snake down """
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        """ Move the snake left """
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        """ Move the snake right """
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
