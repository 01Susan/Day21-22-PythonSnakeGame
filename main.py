from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
# size of screen
screen.setup(width=600, height=600)
# manipulating the screen color
screen.bgcolor("black")
# giving a title
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
snake.extend()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # TODO Detect the collision of snake with food
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.extend()
        scoreboard.increase()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        is_game_on = False

    # Detect collision with tail

    for segments in snake.segment[1:]:
        if snake.head.distance(segments) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()
