from turtle import Turtle


class Scoreboard(Turtle):
    """ Scoreboard that displays current score class """

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()

    def write_score(self):
        self.write(arg=f'Score: {self.score}', align='center', font='Arial')
        self.color('white')
        self.goto(0, 270)
