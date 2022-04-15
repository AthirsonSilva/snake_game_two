from snake import Snake
from time import sleep
from turtle import Screen
from turtle import Turtle

# Declaring the necessary variables
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake game')
screen.tracer(0)

# Creating the snake
snake = Snake()

# Key strokes
screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')

# Making the game screen looping
game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)

    snake.move()


# Closing the screen onclick
screen.exitonclick()
