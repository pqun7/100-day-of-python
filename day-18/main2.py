import random
import turtle as t
from turtle import Screen
timmy = t.Turtle()
t.colormode(255)
timmy.pensize(2)
timmy.speed(10)


def random_color():
    r = random.randint(1.0, 255)
    g = random.randint(1.0, 255)
    b = random.randint(1.0, 255)
    random_color = (r, g, b)
    return random_color


timmy.speed(100)
d = 1.23


def drow(size_of_gef):
    for i in range(round(360 / size_of_gef)):
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gef)
        timmy.color(random_color())


drow(5)
screen = Screen()
screen.exitonclick()
