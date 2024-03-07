import random
from turtle import Turtle, Screen, colormode

color = ['tomato', "orange", "cornflower blue", "green", "yellow", "hot pink",
         "burlywood", "cyan", "light sky blue", "steel blue", "light salmon"]
timmy = Turtle()
num = 3
for i in range(0, 9):
    sh = 360 / num
    for i in range(0, num):
        timmy.forward(100)
        timmy.right(sh)
    num += 1
    timmy.color(random.choice(color))

screen = Screen()
screen.exitonclick()
