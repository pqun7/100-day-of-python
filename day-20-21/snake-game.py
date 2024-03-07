from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


snake = Snake()
food = Food()
board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, ("Up"))
screen.onkey(snake.down, ("Down"))
screen.onkey(snake.left, ("Left"))
screen.onkey(snake.right, ("Right"))

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.hade.distance(food) < 15:
        food.refresh()
        snake.exdend()
        board.add_score()

    if snake.hade.xcor() > 290:
        snake.hade.goto(-290, snake.hade.ycor())
    elif snake.hade.xcor() < -290:
        snake.hade.goto(290, snake.hade.ycor())

    if snake.hade.ycor() > 290:
        snake.hade.goto(snake.hade.xcor(), -290)
    elif snake.hade.ycor() < -290:
        snake.hade.goto(snake.hade.xcor(), 290)
    for segment in snake.segments[1:]:
        # if segment == snake.hade:
        #     pass
        if snake.hade.distance(segment) < 10:
            board.reset()
            snake.reset()
            board.reset_scoer()

screen.exitonclick()
