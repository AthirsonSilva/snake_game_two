from turtle import Turtle


class Scoreboard(Turtle):
    """ Scoreboard that displays current score class """

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()

    def write_score(self, arg, align, x, y):
        """ Prints the score on screen """

        self.write(arg=arg, align=align, font='Arial')
        self.color('white')
        self.goto(x, y)

    def game_over(self):
        """ Prints the game over screen """
        self.goto(0, 0)
        self.write_score(arg=f'GAME OVER', align='center', x=0, y=0)
