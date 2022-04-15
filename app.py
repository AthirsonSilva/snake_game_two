from food import Food
from scoreboard import Scoreboard
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

# Creating food
food = Food()

# Creating the scoreboard
scoreboard = Scoreboard()

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
    scoreboard.write_score(arg=f'Score: {scoreboard.score}', align='center', x=0, y=270)
    sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        scoreboard.clear()
        snake.extend()
        scoreboard.score += 1

    # Detect collision with walls
    if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290 or snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1::]:
        if snake.snake_head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# Closing the screen onclick
screen.exitonclick()
