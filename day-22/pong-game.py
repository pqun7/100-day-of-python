from turtle import Screen, Turtle
from square import Square_Rival
from square_me import Square_Me
from ball import Ball
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)
screen.title("Pong game")

square_rival = Square_Rival()
square_me = Square_Me()
ball = Ball()
score = ScoreBoard()


screen.onkeypress(square_me.Up, ("w"))
screen.onkeypress(square_me.Down, ("s"))

screen.onkeypress(square_rival.Up, ("Up"))
screen.onkeypress(square_rival.Down, ("Down"))

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.xcor() > 390:
        ball.move_again()
        score.add_score1()

    if ball.xcor() < -390:
        ball.move_again()
        score.add_score2()

    if ball.distance(square_rival.op) < 15:
        ball.bounce_back()
    if ball.distance(square_me.op) < 15:
        ball.bounce_back()


screen.exitonclick()
